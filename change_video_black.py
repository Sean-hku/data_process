
import cv2
import os
import copy
import numpy as np
video_name = '/media/hkuit164/WD20EJRX/test_video/output.mp4'
cap = cv2.VideoCapture(video_name)
cnt = 0
out_det_video = cv2.VideoWriter(("test.mp4"), cv2.VideoWriter_fourcc(*'XVID'), 20, (1080,720))
fgbg = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=200, detectShadows=False)
while True:
    ret, frame = cap.read()
    if ret:
        cnt+=1
        fgmask = fgbg.apply(frame)
        background = fgbg.getBackgroundImage()
        diff = cv2.absdiff(frame, background)
        imageEnhance = cv2.filter2D(diff, -1, np.array([[0, -1, 0], [0, 5, 0], [0, -1, 0]]))
        # cv2.imshow("gray", gray)
        # cv2.waitKey(0)
        print(cnt)
        imageEnhance=cv2.resize(imageEnhance,(1080,720))
        # cv2.imshow('black',imageEnhance)
        # cv2.waitKey(1)
        out_det_video.write(imageEnhance)
    else:
        out_det_video.release()
        break



