import cv2
import os
import numpy as np
frame = cv2.imread('/media/hkuit164/TOSHIBA/paper_img/diff_enhance/6100.jpg')
frame1 = cv2.imread('/media/hkuit164/TOSHIBA/paper_img/diff_enhance/-61.jpg')
frame2 = cv2.imread('/media/hkuit164/TOSHIBA/paper_img/diff_enhance/61.jpg')
frame1=cv2.resize(frame1,(640,640))
frame2=cv2.resize(frame2,(640,640))
# frame = cv2.copyMakeBorder(frame, 106, 106, 0, 0, cv2.BORDER_CONSTANT, value=(128,128,128))
frame=cv2.resize(frame,(640,640))
fr = np.concatenate((frame,frame1,frame2),axis=1)
cv2.imwrite('/media/hkuit164/TOSHIBA/paper_img/diff_enhance/3in_1.jpg',fr)
# cv2.imshow('i',fr)
# cv2.waitKey(0)