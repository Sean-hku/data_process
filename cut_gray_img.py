import cv2
import os

mark = ""
video_folder = "/home/sean/Documents/train/"
img_folder = "/home/sean/Documents/img_608"
os.makedirs(img_folder,exist_ok=True)
step = 10


def gray3D(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)


def get_gray(v):
    cnt = 0
    video_path = os.path.join(video_folder, v)
    cap = cv2.VideoCapture(video_path)
    video_name = v.split("/")[-1][:-4]
    while True:
        ret, frame = cap.read()
        if ret:
            cnt += 1
            frame = cv2.resize(frame, (608, 608))
            gray = gray3D(frame)
            cv2.imshow("gray", gray)
            if cnt % step == 0:
                cv2.imwrite(os.path.join(img_folder, mark + video_name + "_{}.jpg".format(cnt)), gray)
            cv2.waitKey(1)
        else:
            break
    cv2.destroyAllWindows()


if __name__ == '__main__':
    for video in os.listdir(video_folder):
        v_name = os.path.join(video_folder, video)
        get_gray(video)