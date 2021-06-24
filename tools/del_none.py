import os


pre_name = '/media/hkuit164/TOSHIBA/nanodet/data/COCO/annotations/train'
name = os.listdir('/media/hkuit164/TOSHIBA/nanodet/data/COCO/annotations/train')
cnt = 0
for i in name:
    f_txt = open(os.path.join(pre_name, i), 'r')
    a= f_txt.read()
    if not a:
        os.remove(os.path.join(pre_name, i))
        cnt+=1
print(cnt)