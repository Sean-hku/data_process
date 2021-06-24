import os
import shutil

txt_file = '/media/hkuit164/WD20EJRX/yolov3-channel-and-layer-pruning/merge_result_filtered_name.txt'
img_pre = '/media/hkuit164/WD20EJRX/yolov3-channel-and-layer-pruning/data/ensemble/black/JPEGImages'
with open(txt_file,'r') as f:
    file_name = f.readlines()
    file_name = map(lambda x:x.strip(),file_name)
for name in file_name:
    if name != '':
        img_path = os.path.join(img_pre, name)
        shutil.copy(img_path, '/media/hkuit164/WD20EJRX/yolov3-channel-and-layer-pruning/data/ensemble/black/1/')
    # print(list(file_name))