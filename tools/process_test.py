'''
allocate train and validation images for test
'''
import glob, os

# current_dir = os.path.dirname(os.path.abspath(__file__))

current_dir= '/media/hkuit164/TOSHIBA/yolo/data/r_test/JPEGImages'
# print(current_dir)
# percentage_test = 10
percentage_test = 10
file_train = open(current_dir[:-10]+'rgb_train.txt', 'w')
file_test = open(current_dir[:-10]+'rgb_test.txt', 'w')

counter = 1
index_test = round(100 / percentage_test)
# print(list(glob.iglob(os.path.join(current_dir, "*.jpg"))))
for pathAndFilename in glob.iglob(os.path.join(current_dir, "*.jpg")):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    # if counter == index_test:
    #     counter = 1
    file_test.write('./data/r_test/JPEGImages' + "/" + title + ".jpg" + "\n")
    # else:
    #     file_train.write('./data/ceiling/JPEGImages' + "/" + title + ".jpg" + "\n")
    #     counter = counter + 1
