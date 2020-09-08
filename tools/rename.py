'''
rename txt or pics within a folder
'''
import os

video_floder = '/home/sean/Documents/0605/without/'
date_name = str('0605_no_')
filename_list = os.listdir(video_floder)
print(filename_list)
count = 1
for i, file in enumerate(filename_list):
    used_name = video_floder + file
    new_name = video_floder +date_name +str(count)+'.mp4'
    os.rename(used_name, new_name)
    count+=1