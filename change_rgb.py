import cv2
import os
import copy

folder_name = '/media/hkuit164/WD20EJRX/yolov3_train/data/rgb_test/JPEGImages/'
for name in os.listdir(folder_name):
    img_path = os.path.join(folder_name,name)
    frame = cv2.imread(img_path)
    frame_copy = copy.deepcopy(frame)
    rgb = cv2.resize(frame_copy,(608,608))
    # cv2.imshow("gray", gray)
    # cv2.waitKey(0)
    if rgb.shape == (608,608,3):
        pass
    else:
        print(name)
    cv2.imwrite(os.path.join(folder_name + name), rgb)