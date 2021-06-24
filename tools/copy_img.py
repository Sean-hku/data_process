import shutil
import os



pre_path = '/media/hkuit164/TOSHIBA/nanodet/data/COCO/annotations/val'
dest_path = '/media/hkuit164/TOSHIBA/nanodet/data/COCO/annotations/txt/'
name = os.listdir(pre_path)
for i in name:
    shutil.copy(os.path.join(pre_path,i),dest_path)