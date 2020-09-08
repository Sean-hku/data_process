'''
sample from servel folders
'''
import os, random, shutil

def moveFile(fileDir,rate):
        pathDir = os.listdir(fileDir)
        filenumber=len(pathDir)
        picknumber=int(filenumber*rate)
        sample = random.sample(pathDir, picknumber)
        # print (sample)
        for name in sample:
                shutil.copy(fileDir+'/'+name, tarDir+'/'+name)
        return
if __name__ == '__main__':
    sample = {
              '0507':0.08,
              '0521':0.12,
              '0607':0.08,
              '0619':0.09,
              '0710':0.06
              }
    # tarDir = '/media/hkuit164/WD20EJRX/underwater_detection/rgb_img/test'
    tarDir = '/media/hkuit164/WD20EJRX/ceiling_detection/test'
    if not os.path.exists(tarDir):
        os.makedirs(tarDir)
    for folder_name,rate in sample.items():
        # fileDir = '/media/hkuit164/WD20EJRX/underwater_detection/rgb_img/'+folder_name
        fileDir = '/media/hkuit164/WD20EJRX/ceiling_detection/' + folder_name
        moveFile(fileDir,rate)