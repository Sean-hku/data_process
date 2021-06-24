import os
import cv2
import numpy as np
import copy

folder_name = '/home/sean/Desktop/final/train/JPEGImages'
for name in os.listdir(folder_name):
    img_path = os.path.join(folder_name, name)
    print(img_path)
    frame = cv2.imread(img_path)
    cv2.imshow('1', frame)
    cv2.waitKey(0)
    frame_copy = copy.deepcopy(frame)
    fgbg = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=200, detectShadows=False)
    fgmask = fgbg.apply(frame_copy)
    background = fgbg.getBackgroundImage()
    diff = cv2.absdiff(frame_copy, background)
    imageEnhance = cv2.filter2D(diff, -1, np.array([[0, -1, 0], [0, 5, 0], [0, -1, 0]]))
    cv2.imwrite(os.path.join('/home/sean/Desktop/final/black/' + name), imageEnhance)
