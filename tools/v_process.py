import cv2
import os
import config
import numpy as np
class Process:
    def __init__(self,train_or_test):
        self.video_folder = train_or_test
        self.date_name = config.date_name
        self.step = config.step
        self.frame_size = config.frame_size

    def rename(self):
        filename_list = os.listdir(self.video_folder)
        # print(filename_list)
        count = 1
        for i, file in enumerate(filename_list):
            if os.path.isfile(self.video_folder + file):
                used_name = self.video_folder + file
                if 'without' in self.video_folder:
                    new_name = self.video_folder + self.date_name + 'no_'+str(count) + '.mp4'
                else:
                    new_name = self.video_folder + self.date_name + 'yes_' + str(count) + '.mp4'
                os.rename(used_name, new_name)
                count += 1
    # def cut_rgb_img(self):
    #     os.makedirs(self.video_folder+'rgb/JPEGImages/',exist_ok=True)
    #     img_folder = self.video_folder+'rgb/JPEGImages/'
    #     for video in os.listdir(self.video_folder):
    #         video_path = os.path.join(self.video_folder, video)
    #         cnt = 0
    #         video_name = video.split('.')[0]
    #         cap = cv2.VideoCapture(video_path)
    #         while True:
    #             ret, frame = cap.read()
    #             if ret:
    #                 cnt += 1
    #                 frame = cv2.resize(frame, self.frame_size)
    #                 if cnt % self.step == 0:
    #                     cv2.imwrite(os.path.join(img_folder, video_name + "_{}.jpg".format(cnt)), frame)
    #             else:
    #                 cv2.destroyAllWindows()
    #                 break
    def cut_rgb_img(self):
        if 'train' in self.video_folder:
            img_folder = config.video_folder + 'rgb/train/JPEGImages/'
            os.makedirs(img_folder, exist_ok=True)
        else:
            img_folder = config.video_folder + 'rgb/test/JPEGImages/'
            os.makedirs(img_folder, exist_ok=True)
        for video in os.listdir(self.video_folder):
            # os.makedirs(self.video_folder + video.split('.')[0], exist_ok=True)
            # img_folder = self.video_folder + video.split('.')[0]
            video_path = os.path.join(self.video_folder, video)
            cnt = 0
            video_name = video.split('.')[0]
            cap = cv2.VideoCapture(video_path)
            while True:
                ret, frame = cap.read()
                if ret:
                    cnt += 1
                    frame = cv2.resize(frame, self.frame_size)
                    if cnt % self.step == 0:
                        cv2.imwrite(os.path.join(img_folder, video_name + "_{}.jpg".format(cnt)), frame)
                else:
                    cv2.destroyAllWindows()
                    break

    def cut_gray_img(self):
        if 'train' in self.video_folder:
            img_folder = config.video_folder+'gray/train/JPEGImages/'
            os.makedirs(img_folder,exist_ok=True)
        else:
            img_folder = config.video_folder + 'gray/test/JPEGImages/'
            os.makedirs(img_folder, exist_ok=True)
        # img_folder = config.video_folder+'gray/JPEGImages/'
        for video in os.listdir(self.video_folder):
            video_path = os.path.join(self.video_folder, video)
            cnt = 0
            cap = cv2.VideoCapture(video_path)
            video_name = video_path.split("/")[-1][:-4]
            while True:
                ret, frame = cap.read()
                if ret:
                    cnt += 1
                    frame = cv2.resize(frame, self.frame_size)
                    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
                    if cnt % self.step == 0:
                        cv2.imwrite(os.path.join(img_folder,  video_name + "_{}.jpg".format(cnt)), gray)
                else:
                    cv2.destroyAllWindows()
                    break

    def cut_black_img(self):
        # os.makedirs(self.video_folder + 'black/JPEGImages/', exist_ok=True)
        # img_folder = self.video_folder + 'black/JPEGImages/'
        if 'train' in self.video_folder:
            img_folder = config.video_folder+'black/train/JPEGImages/'
            os.makedirs(img_folder,exist_ok=True)
        else:
            img_folder = config.video_folder + 'black/test/JPEGImages/'
            os.makedirs(img_folder, exist_ok=True)
        for video in os.listdir(self.video_folder):
            video_path = os.path.join(self.video_folder, video)
            cnt = 0
            video_name = video_path.split("/")[-1][:-4]
            cap = cv2.VideoCapture(video_path)
            fgbg = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=200, detectShadows=False)
            while True:
                ret, frame = cap.read()
                if ret:
                    cnt += 1
                    frame = cv2.resize(frame, self.frame_size)
                    fgmask = fgbg.apply(frame)
                    background = fgbg.getBackgroundImage()
                    diff = cv2.absdiff(frame, background)
                    imageEnhance = cv2.filter2D(diff, -1, np.array([[0, -1, 0], [0, 5, 0], [0, -1, 0]]))
                    if cnt % self.step == 0:
                        cv2.imwrite(os.path.join(img_folder,  video_name + "_{}.jpg".format(cnt)), imageEnhance)
                else:
                    cv2.destroyAllWindows()
                    break


    def del_diff_pics(self):
        pass
