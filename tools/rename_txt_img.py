'''
rename the txt and pics in the same time
'''
import os

img_floder = '/media/hkuit164/Ubuntu 16.0/Fish_documents/JPEGImages'
txt_folder = '/media/hkuit164/Ubuntu 16.0/Fish_documents/txt'
date_name = '0911_fish'
img_list = os.listdir(img_floder)
# txt_list = os.listdir(txt_folder)
count = 1
for name in img_list:
    print(count)
    count+=1
    name_tmp = name.split('.')[0]
    old_txt_file = os.path.join(txt_folder,name_tmp+'.txt')
    new_txt_file = os.path.join(txt_folder,date_name+name_tmp+'.txt')
    old_img_file = os.path.join(img_floder,name)
    new_img_file = os.path.join(img_floder,date_name+name)
    os.rename(old_img_file,new_img_file)
    os.rename(old_txt_file, new_txt_file)
    # if not os.path.exists(old_img_file):
    #     print(old_img_file)
# for i, file in enumerate(filename_list):
#     used_name = video_floder + file
#     new_name = video_floder +date_name +str(count)+'.mp4'
#     os.rename(used_name, new_name)
#     count+=1