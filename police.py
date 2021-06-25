import cv2
import numpy as np
import copy
import time
from numpy import mean
from matplotlib import pyplot as plt
import seaborn as sns
import os



def demo(cell_num, history,video_path):
    # cell_num = 4
    height = 680
    width = 980
    # history = 5
    major_thresh = 6
    minor_thresh = 4
    save_size = (980, 680)

    cell_height, cell_width = height//cell_num, width//cell_num
    # video_path = "/media/hkuit164/TOSHIBA/mmdetection/New_floder/output.mp4"
    cap = cv2.VideoCapture(video_path)
    _, frame1 = cap.read()
    frame = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('{}.mp4'.format(video_path.split('/')[-1]),fourcc, 20.0, save_size)
    previous_frame = frame[:,:]
    diff_list = []
    time_list = []
    while True:
        begin_time = time.time()
        ret, frame1 = cap.read()

        if ret:
            frame = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
            diff = cv2.absdiff(frame, previous_frame)
            diff = cv2.resize(diff, (width, height))
            diff_list.append(diff)
            previous_frame = frame[:,:]
            if len(diff_list) > history:
                diff_list.pop(0)
                final_frame = np.rint(np.array(diff_list).mean(axis=0)).astype(np.uint8)
                cp_frame = copy.deepcopy(final_frame)

                final_frame = cv2.cvtColor(final_frame, cv2.COLOR_GRAY2BGR)
                frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)

                frame1 = cv2.resize(frame1, (width, height))
                for i in range(cell_num):
                    for j in range(cell_num):
                        tmp = np.sum(cp_frame[(height * i//cell_num):(height * (i+1)//cell_num),
                                     (width * j//cell_num):(width * (j+1)//cell_num)]) / ((width//cell_num) * (height//cell_num))
                        cv2.putText(final_frame, str(round(tmp,2)), (width * j//cell_num + 20, height * i//cell_num + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                    (0, 0, 255), 1)
                        if tmp > major_thresh:
                            cv2.rectangle(frame1, (width * j // cell_num , height * i // cell_num ),
                                          (width * j // cell_num + cell_width - 1, height * i // cell_num + cell_height - 1), (0, 0, 255), thickness=2)

                        elif tmp > minor_thresh:
                            cv2.rectangle(frame1, (width * j // cell_num, height * i // cell_num),
                                          (width * j // cell_num + cell_width - 1,
                                           height * i // cell_num + cell_height - 1), (0, 255, 255), thickness=2)

                        # cv2.waitKey(0)
                # img = np.hstack([frame1,final_frame])
                out.write(frame1)
                cv2.imshow('img', frame1)
                cv2.waitKey(1)
                time_list.append(time.time() - begin_time)
                print("Time spent for current frame: {}".format(time.time() - begin_time))
        else:
            return mean(time_list)
            # break

if __name__ == '__main__':
    # name = os.listdir('/home/hkuit164/Downloads/lokeyewhall/')
    # for i in name:
    a = '/home/hkuit164/Downloads/lokeyewhall/' + 'IMG_2041.MOV'
    demo(30,10,a)
    # data = []
    # count = 0
    # xLabel = ['5','10','15','20','25','30','35','40','45','50','55','60','65','70','75','80','85','90','95','100']
    # yLabel = ['5','10','15','20','25','30','35','40','45','50','55','60','65','70','75','80','85','90','95','100']
    # # [5, 10, 15, 20, 25, 30, 35]
    # for i in [5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]:
    #     tmp = []
    #     for j in [5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]:
    #         count+=1
    #         print(count)
    #         a = demo(i,j)
    #         tmp.append(a)
    #     data.append(tmp)
    # print(data)
    # fig = plt.figure()
    # # 定义画布为1*1个划分，并在第1个位置上进行作图
    # ax = fig.add_subplot(111)
    # # 定义横纵坐标的刻度
    # ax.set_yticks(range(len(yLabel)))
    # ax.set_yticklabels(yLabel)
    # ax.set_xticks(range(len(xLabel)))
    # ax.set_xticklabels(xLabel)
    # plt.xlabel('cell_num')
    # plt.ylabel('frame_num')
    # # 作图并选择热图的颜色填充风格，这里选择hot
    # im = ax.imshow(data, cmap=plt.cm.hot_r)
    # # 增加右侧的颜色刻度条
    # plt.colorbar(im)
    # # 增加标题
    # plt.title("x:cell_num y:history_frame")
    # # show
    # plt.show()


    '''
    a = [[0.033007752236879524, 0.03595875576588955, 0.038202357082846236, 0.04069175519243452, 0.04350249947583534, 0.04594117758337889, 0.04867391095377852], [0.03439656521595392, 0.037314770659916056, 0.039689947755416885, 0.04233419786734318, 0.04493599693861335, 0.04737338605008276, 0.05006475423916861], [0.03665518386465453, 0.03936678106291839, 0.042302827708041925, 0.04536694024388468, 0.04830297292853575, 0.0508711144436885, 0.0538536415861178], [0.03960414138618928, 0.04273328022916487, 0.04580719442826634, 0.04861884062184645, 0.05130946929426567, 0.05459304940671526, 0.05738315588085164], [0.043910550236378125, 0.047023314518680595, 0.049781762719912276, 0.05264912300792299, 0.05534461070946057, 0.058574059728868394, 0.06117269755353878], [0.04913168776765749, 0.05103342334189179, 0.05399028979898257, 0.05719099693980775, 0.05957649719233647, 0.0620202705662906, 0.06435941211922373], [0.054293675758023296, 0.05731611845715302, 0.059928449615723356, 0.06286997380149661, 0.06496897490959272, 0.06808435336806769, 0.07040499638683216]]
    sns.set()
    ax = sns.heatmap(a)
    plt.show()
    '''


    # data = [[0.025283599100193056, 0.028343842740644488, 0.03102655148287432, 0.03365202591969417, 0.03674718105431759, 0.038722837224919746, 0.04158933510941066, 0.044707360721769784, 0.049352995957000344, 0.0491893194817208, 0.05976512812185979, 0.058941952884197235, 0.05797960394519871, 0.06518924677813495, 0.06032725742885044, 0.06108835068616, 0.08159935168730907, 0.06739846397848691, 0.0689349338926118, 0.07016770044962566], [0.02605670440096815, 0.029171100833959747, 0.03182864407880591, 0.0344198804635268, 0.03679899495057385, 0.038964487136678494, 0.04157151265090771, 0.04401516630536034, 0.04597291765333731, 0.04915409152572219, 0.053229055542876755, 0.054910991340875626, 0.058437480764873956, 0.060864664890148024, 0.06157567549724968, 0.062610539523038, 0.06542293230692546, 0.06761255685020895, 0.07037383112414129, 0.07407105962435405], [0.028299588115275408, 0.03114196083001923, 0.033592267867622025, 0.03664936927648691, 0.039104565225466334, 0.04111922548172322, 0.04401255457588796, 0.0463219199861799, 0.049348387537123284, 0.05182231439126504, 0.055115976195404495, 0.05770348384976387, 0.06056757296546031, 0.06405398580763075, 0.06590598943282147, 0.06805177710273048, 0.07011040051778157, 0.07518905751845416, 0.07475073584194841, 0.07845438520113628], [0.03281138123584395, 0.03583010665157385, 0.038159742267853625, 0.04128672526432918, 0.04337096455121281, 0.045296037450749824, 0.048454874017265406, 0.05130842469987415, 0.05392311192766021, 0.05595067385080699, 0.05924045175745867, 0.06183197349309921, 0.0670098490634207, 0.06757099098629421, 0.07025378577563228, 0.07198834961110895, 0.0737920296497834, 0.07763151561512667, 0.08025235143201105, 0.08055747548739116], [0.03555294044879304, 0.04302499168797543, 0.04296296233430915, 0.044924600766255304, 0.04687960460932568, 0.0505658210592067, 0.05305078860079305, 0.05541753485089257, 0.05805830110477496, 0.06112086450731432, 0.06763857689456663, 0.0673595555126667, 0.06947681055230609, 0.07202784220377605, 0.07559449818669534, 0.07513841715725986, 0.07994566819606683, 0.09359500688665054, 0.08503328520676186, 0.08673132459322612], [0.04127049646457704, 0.04465589606971072, 0.047973949974829996, 0.04941461636469914, 0.05332547004776771, 0.05533871244876943, 0.05892743153518505, 0.06014818520773025, 0.06289027914216247, 0.06495532796189592, 0.06915261088937953, 0.07099095359444618, 0.07423215801432981, 0.07659416728549534, 0.07833699790798888, 0.08135439590974287, 0.08417000526036972, 0.08510858171126422, 0.08772591064716208, 0.08927682042121887], [0.04763999906908564, 0.050077005436545925, 0.05355063928376644, 0.05641915247990535, 0.05843970029041021, 0.061486827566268595, 0.06293995996539513, 0.06613650776091076, 0.06934327717068829, 0.07018061264141186, 0.07585387990094614, 0.07687228545546532, 0.08141855466163765, 0.0816407910099736, 0.08453144832533233, 0.087562311779369, 0.09128904953981057, 0.09246271498063031, 0.09535614375410409, 0.09422142306963603], [0.05480337343296083, 0.056802465204606974, 0.05919655528637247, 0.0628356750194843, 0.06454790240586405, 0.06798859099124341, 0.06970253419340326, 0.07211147319702875, 0.07629956776582741, 0.07903582340962179, 0.0809709161951922, 0.08511177450418472, 0.08579248897099899, 0.08863495897363734, 0.09117850478814572, 0.09476834535598755, 0.09661085789020245, 0.10168002633487477, 0.09896409100499647, 0.10121723016103108], [0.0616126681576256, 0.0640650569346913, 0.067610311945644, 0.06984359255203834, 0.07284113614246099, 0.07468612143333922, 0.07847418410054753, 0.08065912269410633, 0.08391196516495716, 0.084692797145328, 0.09031692795131517, 0.09189864248037338, 0.09457546977673546, 0.09735474321577284, 0.09980959794959243, 0.10244272513823076, 0.10404606354542267, 0.1078274460399852, 0.11009660260430698, 0.1097966730594635], [0.07139794566050298, 0.07365655689908747, 0.07575280731971111, 0.0783079404097337, 0.08147768540815874, 0.08375656351130059, 0.08833206905407852, 0.08875392448334467, 0.09141160868391206, 0.0941329356786367, 0.09900680832240892, 0.10166819393634796, 0.10290183859356379, 0.11147545002124927, 0.11116333397067323, 0.11149957505139438, 0.1137990462474334, 0.11881634067086612, 0.12123432652703647, 0.12273143728574117], [0.07974521452639283, 0.08317475988153826, 0.08425949910365113, 0.09425982374411362, 0.08905595721620502, 0.0914599210657972, 0.0948897586779648, 0.09809102047057379, 0.10104420215268678, 0.103803631421682, 0.10568595623624498, 0.10967344045639038, 0.11309675442970406, 0.11391100177058468, 0.11952475625641491, 0.12086632034995339, 0.12292865606454703, 0.12649473723243265, 0.12904206637678475, 0.133244256178538], [0.08936831931106183, 0.09283308397259629, 0.0957928206942497, 0.09971440526155326, 0.1027577453189426, 0.10250181086519931, 0.10592793078904741, 0.10837815489087786, 0.11255825923967964, 0.11429274404371106, 0.11938625833262569, 0.12052002549171448, 0.1240935648901988, 0.1256241621794524, 0.12930499290933414, 0.13171863014047797, 0.1332223231975849, 0.13625001206117518, 0.14051656887449068, 0.14487444361050925], [0.10029221182109929, 0.10399399305644788, 0.10654330034868432, 0.10905069342026344, 0.11174023271811129, 0.11295094895870128, 0.11772438113609057, 0.11894486631665911, 0.12372889096223855, 0.12428727021088472, 0.12807096605715546, 0.13110456988215446, 0.13455453969664494, 0.13478071159786648, 0.13900773865836008, 0.1407072110609575, 0.14535194788223657, 0.14922421118792364, 0.1586543033862936, 0.15183844168980917], [0.11258194025825052, 0.11671920408282363, 0.12089696499185824, 0.12142362732153672, 0.12475932487333664, 0.12750218523309587, 0.13201238064283735, 0.13352479253496444, 0.13562052762961085, 0.1375694854839428, 0.14400620391403418, 0.14690979570150375, 0.1470256740764036, 0.15043862660725912, 0.15287977821972906, 0.15475818785754117, 0.15712789388803336, 0.16161755954518037, 0.1656198994866733, 0.16558710734049478], [0.12536973913176722, 0.1300437094872458, 0.13133018826125958, 0.13355414454753584, 0.13860210987052532, 0.13867101517129451, 0.14330694648656953, 0.14558412347521102, 0.1490811305710032, 0.1495608864603816, 0.15467354871224667, 0.1585603468120098, 0.16107199555736476, 0.1618268887201945, 0.16468573103145678, 0.16970134323293512, 0.16883598229823968, 0.1718234384761137, 0.1747764307877113, 0.18086896340052286], [0.1383914707087669, 0.1420888670703821, 0.14551417543253767, 0.14878371816415054, 0.1522473060723507, 0.1551301377884885, 0.15717162443010996, 0.16092057738985335, 0.16484870789926262, 0.16599151250478383, 0.17284978990969452, 0.17506709694862366, 0.1719135106620142, 0.1766991791901765, 0.17818286467571648, 0.1789419867775657, 0.18276821038661858, 0.18568356598124786, 0.1872594767603381, 0.18891472617785135], [0.15102515501134536, 0.15535426976387962, 0.15916908771619884, 0.1624956108056582, 0.16375040767168758, 0.16751939438759011, 0.16899073257874908, 0.170412472316197, 0.17832150036775613, 0.1756769644247519, 0.18353258008542267, 0.18324825167655945, 0.18490490266832255, 0.18699057896931967, 0.19275000144024285, 0.1923679546876387, 0.19376019942454803, 0.19732749462127686, 0.1996970012270171, 0.20694110790888467], [0.16586971082607238, 0.17003133840728224, 0.17286187136938813, 0.17436836316035345, 0.17929537850196917, 0.18413448080103448, 0.1831887491633383, 0.18819279613949003, 0.19100138809107528, 0.19685248748676196, 0.1968509909035503, 0.20600836724042892, 0.2108762870400639, 0.2124237440250538, 0.21276399554038533, 0.2163202166557312, 0.21579906879327235, 0.22320526487687053, 0.2212512493133545, 0.23299649357795715], [0.18431838620610597, 0.18568271921392074, 0.1875026707255512, 0.19408981158183172, 0.19342572520477602, 0.20030208090518384, 0.206895466600911, 0.20761587506248838, 0.21405432797685453, 0.21419958166173986, 0.21760501377824423, 0.218849066644907, 0.21998525069931807, 0.22431954631098994, 0.22514034290702975, 0.22621100599115546, 0.23173119471623346, 0.2322356280158548, 0.23185857411088615, 0.2346560855706533], [0.2030486579702682, 0.20916407359273811, 0.2117248893877782, 0.21563220024108887, 0.22012268894850606, 0.21975271498903315, 0.22241824128654566, 0.2249100378581456, 0.22995945773547208, 0.22910892641222155, 0.2372263549030691, 0.23399903625249863, 0.23678363783884857, 0.24255513261865685, 0.24520090648106166, 0.24383002519607544, 0.24705646588252142, 0.2531706164864933, 0.2503945334204312, 0.26079373558362323]]
    # fig = plt.figure()
    # 定义画布为1*1个划分，并在第1个位置上进行作图
    # ax = fig.add_subplot(111)
    # 定义横纵坐标的刻度
    # ax.set_yticks(range(len(yLabel)))
    # ax.set_yticklabels(yLabel)
    # ax.set_xticks(range(len(xLabel)))
    # ax.set_xticklabels(xLabel)
    # plt.xlabel('cell_num')
    # plt.ylabel('frame_num')
    # 作图并选择热图的颜色填充风格，这里选择hot
    # im = ax.imshow(data, cmap=plt.cm.hot_r)
    # 增加右侧的颜色刻度条
    # plt.colorbar(im)
    # 增加标题
    # plt.title("x:cell_num y:history_frame")
    # show
    # plt.show()