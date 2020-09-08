'''
find same pics according to another folder
'''
import os
import shutil
less_one = '/media/hkuit164/WD20EJRX/ceiling_detection/test'
more_one = '/media/hkuit164/WD20EJRX/ceiling_detection/ceiling/JPEGImages'
tar_dir = '/media/hkuit164/WD20EJRX/underwater_detection/rgb_img/train11'
# if not os.path.exists(tar_dir):
#     os.makedirs(tar_dir)
name = os.listdir(less_one)
for i in name:
    # path = os.path.join(more_one,i)
    # shutil.copy(os.path.join(more_one,i),os.path.join(tar_dir,i))
    if os.path.exists(os.path.join(more_one,i)):
        os.remove(os.path.join(less_one, i))
    # else:

#         os.remove(os.path.join(less_one, i))