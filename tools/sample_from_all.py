'''
sample from one folder
'''
import os, random, shutil

def moveFile(fileDir,testDir,rate):
        pathDir = os.listdir(fileDir)
        filenumber=len(pathDir)
        picknumber=int(filenumber*rate)
        sample = random.sample(pathDir, picknumber)
        print (filenumber)
        for name in sample:
                shutil.copy(fileDir+'/'+name, testDir+'/'+name)
        return
if __name__ == '__main__':
    all_img = '/media/hkuit164/WD20EJRX/underwater_detection/rgb_img/JPEGImages'
    sample_rate = 0.025
    testDir = '/media/hkuit164/WD20EJRX/underwater_detection/black_img/test'
    if not os.path.exists(testDir):
        os.makedirs(testDir)
    moveFile(all_img,testDir,sample_rate)