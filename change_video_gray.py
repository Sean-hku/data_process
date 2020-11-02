
import cv2
import os
import copy

def gray3D(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)


video_name = '/media/hkuit164/WD20EJRX/test_video/output.mp4'
cap = cv2.VideoCapture(video_name)
cnt = 0
out_det_video = cv2.VideoWriter(("gray.mp4"), cv2.VideoWriter_fourcc(*'XVID'), 20, (1080,720))
while True:
    ret, frame = cap.read()
    if ret:
        cnt+=1
        frame_copy = copy.deepcopy(frame)
        gray = gray3D(frame_copy)
        gray = cv2.resize(gray,(1080,720))
        # cv2.imshow("gray", gray)
        # cv2.waitKey(0)
        print(cnt)
        out_det_video.write(gray)
        # cv2.imwrite(os.path.join('/home/sean/Documents/yolov3_train/data/test/gray_608/' + name), gray)

    #test

