'''
split pics from a mixed folder to a specific folder
'''
# coding=utf-8
import os
import shutil
import glob
#目标文件夹，此处为相对路径，也可以改为绝对路径
folder_1 = '/media/hkuit164/WD20EJRX/underwater_detection/black_img/2019'
all_img = '/media/hkuit164/WD20EJRX/underwater_detection/black_img/JPEGImages'
# folder_2 = '2019'
# folder_3 = '0605'
# folder_4 = '0612'
# folder_5 = '0619'
# determination = '/../../目标文件夹/'

if not os.path.exists(folder_1):
    os.makedirs(folder_1)

#源文件夹路径
img_name = glob.glob(os.path.join(all_img,'??_*'))
# path = '/../../源文件夹'
# folders = os.listdir(path)
for img in img_name:
    shutil.copy(img, folder_1)