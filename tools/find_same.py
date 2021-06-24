'''
find same pics according to another folder
'''
import os
import shutil
import tqdm
less_one = '/media/hkuit164/WD20EJRX/yolov3-channel-and-layer-pruning/data/ensemble/black_all'
more_one = '/media/hkuit164/WD20EJRX/yolov3-channel-and-layer-pruning/data/ensemble/JPEGImages'
tar_dir = '/media/hkuit164/WD20EJRX/yolov3-channel-and-layer-pruning/data/ensemble/gray_tar'
# if not os.path.exists(tar_dir):
#     os.makedirs(tar_dir)
name = os.listdir(less_one)
for i in tqdm.tqdm(name):
    path = os.path.join(more_one,i)
    try:
        shutil.copy(os.path.join(more_one,i),os.path.join(tar_dir,i))
    except:
        FileNotFoundError
    # if os.path.exists(os.path.join(more_one,i)):
    #     os.remove(os.path.join(less_one, i))
    # else:

#         os.remove(os.path.join(less_one, i))