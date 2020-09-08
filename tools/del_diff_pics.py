# -*- coding: utf-8 -*-
import os


img_path = '/media/hkuit164/WD20EJRX/underwater_detection/black_img/train_data/JPEGImages'
anno_path = '/media/hkuit164/WD20EJRX/underwater_detection/black_img/train_data/txt'

def contrastDir(img_path,anno_path):
    jpg_list = []
    xml_list = []
    for root, dirs, files in os.walk(img_path):
        for file in files:
            if os.path.splitext(file)[1] == '.jpg':
                jpg_list.append(os.path.splitext(file)[0])
    for root, dirs, files in os.walk(anno_path):
        for file in files:
            if os.path.splitext(file)[1] == '.txt':
                xml_list.append(os.path.splitext(file)[0])
#对比xml与jpg
    # diff = set(xml_list).difference(set(jpg_list))
    # print(len(diff))
    # for name in diff:
    #     print("No corresponding image file", name + ".txt")
# 对比jpg与xml
#     print(len(jpg_list))
    # diff2 = set(jpg_list).difference(set(xml_list))
    diff2 = set(jpg_list).difference(set(xml_list))
    print(len(diff2))
    # for name in diff2:
        # print("No corresponding XML file", name + ".jpg")
        #删除没有的对应xml的图像
        # os.remove(anno_path+'/'+ name+'.txt')
        # os.remove(img_path + '/' + name + '.jpg')
    # return jpg_list,xml_list

if __name__ == '__main__':

    contrastDir(img_path,anno_path)
