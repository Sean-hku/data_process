from v_process import *
import config
import os

def data_process():
    for folder_name in os.listdir(config.video_folder):
        print(folder_name)
        if 'train_without' in folder_name :
            pro = Process(config.video_folder + folder_name + '/')
            pro.rename()
            # if 'gray' in config.process_color:
            print('process train_without')
            pro.cut_gray_img()
            pro.cut_rgb_img()
            pro.cut_black_img()
        if 'train_with' in folder_name and 'train_without' not in folder_name:
            print('process train_with')
            pro = Process(config.video_folder + folder_name + '/')
            pro.rename()
            pro.cut_gray_img()
            pro.cut_rgb_img()
        if 'test_without' in folder_name:
            print('process test_without')
            pro = Process(config.video_folder + folder_name + '/')
            pro.rename()
            pro.cut_gray_img()
            pro.cut_rgb_img()
            pro.cut_black_img()
        if 'test_with' in folder_name and 'test_without' not in folder_name:
            print('process test_with')
            pro = Process(config.video_folder + folder_name + '/')
            pro.rename()
            pro.cut_gray_img()
            pro.cut_rgb_img()


            # if 'black' in config.process_color:
            #     print('process black_imgs')
            #     pro.cut_black_img()
            # if 'rgb' in config.process_color:
            #     print('process rgb_imgs')
            #     pro.cut_rgb_img()

data_process()