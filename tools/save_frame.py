
'''
cut several videos into frames within a floder
'''

import cv2
import os
pathin = 'video'
# count=0
for video in os.listdir(pathin):
    video_path = os.path.join(pathin, video)
    # video_path = '46.mp4'
    step = 20
    cnt = 0
    cap = cv2.VideoCapture(video_path)
    while True:
        ret, frame = cap.read()
        if ret:
            if cnt % step == 0:
                cv2.imwrite('/home/hkuit164/Documents/fish/' +video.split('.')[0]+'__'+ str(cnt) + ".jpg", frame)
                # cv2.imwrite("{}.jpg".format(cnt), frame)
            # count += 1
            cnt += 1
        else:
            break
'''
# cut several videos into frames in several floders
import cv2
import os
pathin = '/home/sean/Documents/CeilingCam_0507/'
# count=1
for video in os.listdir(pathin):
    video_path = os.path.join(pathin, video)
    for video1 in os.listdir(video_path):
        video1_path = os.path.join(video_path,video1)
        print(video1_path)
        step = 5
        cnt = 0
        cap = cv2.VideoCapture(video1_path)
        while True:
            ret, frame = cap.read()
            if ret:
                if cnt % step == 0 and cnt % 10 != 0:
                    video_name = video1.split('.')[0]
                    folder_name = video_path.split('/')[-1]
                    cv2.imwrite('/home/sean/Documents/0507_new_frame/' + '0507_' +folder_name+'_'+ video_name+'_'
                                + str(cnt) + ".jpg", frame)
                    # cv2.imwrite("{}.jpg".format(cnt), frame)
                    # count += 1
                cnt += 1

            else:
                break'''
