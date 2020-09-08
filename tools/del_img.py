# -*- coding: utf-8 -*-
import os

less_one = '/media/hkuit164/WD20EJRX/ceiling_detection/test'
del_one = '/home/hkuit164/Desktop/0619_data/0619_origin/test_black'
ls1 = os.listdir(del_one)
ls2 = os.listdir(less_one)
diff = set(ls1).difference(set(ls2))
for name in diff:
    img_path = os.path.join('/home/hkuit164/Desktop/0619_data/0619_origin/test_black',name)
    os.remove(img_path)
# print(diff)
