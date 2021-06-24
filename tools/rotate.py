#
# import cv2
# import numpy as np
#
# # 读取原图像
# img = cv2.imread('/home/hkuit164/Downloads/tmp/20210520_145331__0.jpg')
# # cv2.imshow("ori", img)
# # cv2.waitKey(0)
# #
# # # 获取输入图像的信息，生成旋转操作所需的参数（padding: 指定零填充的宽度； canter: 指定旋转的轴心坐标）
# # h, w = img.shape[:2]
# # padding = (w - h) // 2
# # center = (w // 2, w // 2)
# #
# # # 在原图像两边做对称的零填充，使得图片由矩形变为方形
# # img_padded = np.zeros(shape=(w, w, 3), dtype=np.uint8)
# # img_padded[padding:padding+h, :, :] = img
# #
# # cv2.imshow("pad", img_padded)
# # cv2.waitKey(0)
# # # cv2.imwrite("./img_padded.jpg", img_padded)
# #
# # # 逆时针-90°(即顺时针90°)旋转填充后的方形图片
# # M = cv2.getRotationMatrix2D(center, -180, 1)
# # rotated_padded = cv2.warpAffine(img_padded, M, (w, w))
# #
# # cv2.imshow("rotate", rotated_padded)
# # cv2.waitKey(0)
# # # cv2.imwrite("./rotated_padded.jpg", rotated_padded)
# #
# # # 从旋转后的图片中截取出我们需要的部分，作为最终的输出图像
# # output = rotated_padded[:, padding:padding+h, :]
# #
# # cv2.imshow("out", output)
# # cv2.waitKey(0)
# # cv2.imwrite("./output.jpg", output)
# #
# # cv2.destroyAllWindows()
#
# '''
# if h > w
# '''
#
# # import cv2
# # import numpy as np
# #
# # # 读取原图像
# # img = cv2.imread('/media/hkuit164/WD20EJRX/output.jpg')
# cv2.imshow("ori", img)
# cv2.waitKey(1)
#
# # 获取输入图像的信息，生成旋转操作所需的参数（padding: 指定零填充的宽度； canter: 指定旋转的轴心坐标）
# h, w = img.shape[:2]
# padding = (h - w) // 2
# center = (h // 2, h // 2)
#
# # 在原图像两边做对称的零填充，使得图片由矩形变为方形
# img_padded = np.zeros(shape=(h, h, 3), dtype=np.uint8)
# img_padded[:, padding:padding+w, :] = img
#
# cv2.imshow("pad", img_padded)
# cv2.waitKey(1)
# # cv2.imwrite("./img_padded.jpg", img_padded)
#
# # 逆时针-90°(即顺时针90°)旋转填充后的方形图片
# M = cv2.getRotationMatrix2D(center, 180, 1)
# rotated_padded = cv2.warpAffine(img_padded, M, (h, h))
#
# cv2.imshow("rotate", rotated_padded)
# cv2.waitKey()
# # cv2.imwrite("./rotated_padded.jpg", rotated_padded)
#
# # 从旋转后的图片中截取出我们需要的部分，作为最终的输出图像
# output = rotated_padded[padding:padding+w, :, :]
#
# cv2.imshow("out", output)
# cv2.waitKey(0)
# cv2.imwrite("./output.jpg", output)
#
# cv2.destroyAllWindows()


from PIL import Image
import os

dir_img = "/home/hkuit164/Downloads/tmp/"
# 待处理图片所在地址
dir_save = "/home/hkuit164/Downloads/img/"
# 旋转后保存的地址

list_img = os.listdir(dir_img)

for img_name in list_img:
    pri_image = Image.open(dir_img + img_name)
    tmppath = dir_save + img_name
    pri_image.rotate(180).save(tmppath)
