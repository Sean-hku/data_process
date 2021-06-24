import cv2
import os
import numpy as np

mark = ""
video_folder = "/home/hkuit164/Desktop/0619_data/0619_origin/test_video/"
img_folder = "/home/hkuit164/Desktop/0619_data/0619_origin/test_black/"
os.makedirs(img_folder,exist_ok=True)
step = 20


def get_black(video_name):
    cnt = 0
    video_path = os.path.join(video_folder, video_name)
    video_name = video_name.split("/")[-1][:-4]
    cap = cv2.VideoCapture(video_path)
    print(video_name)
    fgbg = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=200, detectShadows=False)

    while True:
        ret, frame = cap.read()
        if ret:
            cnt += 1
            # frame = cv2.resize(frame, (608, 608))
            fgmask = fgbg.apply(frame)
            background = fgbg.getBackgroundImage()
            diff = cv2.absdiff(frame, background)
            imageEnhance = cv2.filter2D(diff, -1, np.array([[0, -1, 0], [0, 5, 0], [0, -1, 0]]))
            # cv2.imshow("black", imageEnhance)
            if cnt % step == 0:
                cv2.imwrite(os.path.join(img_folder, video_name + "_{}.jpg".format(cnt)), imageEnhance)
            # cv2.waitKey(1)
        else:
            cv2.destroyAllWindows()
            break

if __name__ == '__main__':
    for video in os.listdir(video_folder):
        get_black(video)
