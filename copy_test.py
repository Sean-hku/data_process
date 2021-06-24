import os
import shutil

more_one = '/media/hkuit164/WD20EJRX/underwater_detection/black_img/JPEGImages'
less_one = '/media/hkuit164/TOSHIBA/test/mul'
tar_dir = '/media/hkuit164/WD20EJRX/underwater_detection/test/mul'
if not os.path.exists(tar_dir):
    os.makedirs(tar_dir)
name = os.listdir(less_one)
for i in name:
    path = os.path.join(more_one,i)
    if os.path.exists(os.path.join(more_one,i)):
        shutil.copy(path,os.path.join(tar_dir,i))