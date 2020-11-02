
'''
cut several videos into frames within a floder
'''

# import cv2
# import os
# pathin = '/media/hkuit164/WD20EJRX/fish'
# pathout = '/media/hkuit164/WD20EJRX/fish_pic/'
# # count=0
# for video in os.listdir(pathin):
#     video_path = os.path.join(pathin, video)
#     print(video_path)
#     step = 20
#     cnt = 0
#     cap = cv2.VideoCapture(video_path)
#     while True:
#         ret, frame = cap.read()
#         if ret:
#             if cnt % step == 0:
#                 cv2.imwrite(pathout +video.split('.')[0]+'__'+ str(cnt) + ".jpg", frame)
#             cnt += 1
#         else:
#             break

# cut several videos into frames in several floders
import cv2
import os
pathin = '/media/hkuit164/WD20EJRX/5Groups/'
# count=1
for video in os.listdir(pathin):
    video_path = os.path.join(pathin, video)
    for video1 in os.listdir(video_path):
        video1_path = os.path.join(video_path,video1)
        print(video1_path)
        step = 20
        cnt = 0
        cap = cv2.VideoCapture(video1_path)
        while True:
            ret, frame = cap.read()
            if ret:
                if cnt % step == 0 :
                    video_name = video1.split('.')[0]
                    folder_name = video_path.split('/')[-1]
                    cv2.imwrite('/media/hkuit164/WD20EJRX/5_pics/' +folder_name+'/'+ video_name+'_'+ str(cnt) + ".jpg", frame)
                    # cv2.imwrite("{}.jpg".format(cnt), frame)
                    # count += 1
                cnt += 1

            else:
                break