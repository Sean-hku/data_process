import cv2

img_path = '/media/hkuit164/TOSHIBA/nanodet/data/COCO/images/val2017/000000000139.jpg'
img = cv2.imread(img_path)
cv2.imshow('img',img)
cv2.waitKey(0)