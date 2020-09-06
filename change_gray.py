import cv2
import os
import copy

def gray3D(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)


folder_name = '/home/sean/Documents/yolov3_train/data/test/rgb'
for name in os.listdir(folder_name):
    img_path = os.path.join(folder_name,name)
    # print(img_path)
    frame = cv2.imread(img_path)
    frame_copy = copy.deepcopy(frame)
    gray = gray3D(frame_copy)
    gray = cv2.resize(gray,(608,608))
    # cv2.imshow("gray", gray)
    # cv2.waitKey(0)

    cv2.imwrite(os.path.join('/home/sean/Documents/yolov3_train/data/test/gray_608/' + name), gray)