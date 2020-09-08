'''
delete txt file if it strats with 1
'''
import os
import re
name = os.listdir('/media/hkuit164/WD20EJRX/yolov3-channel-and-layer-pruning/data/fish/txt')
for i in range(len(name)):
    path = os.path.join('/media/hkuit164/WD20EJRX/yolov3-channel-and-layer-pruning/data/fish/txt',name[i])
    with open(path,'a+') as f:
        a= f.readlines()
        print(a)
    # f = open(path, 'r')
    # alllines = f.readlines()
    # f.close()
    # f = open(path, 'w+')
    # for eachline in alllines:
    #     a = re.sub('1 ', '0 ', eachline)
    #     f.writelines(a)
    # f.close()