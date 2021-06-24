'''
delete txt file if it strats with 1
'''
import os
import re
name = os.listdir('/media/hkuit164/WD20EJRX/basket/txt')
for i in range(len(name)):
    path = os.path.join('/media/hkuit164/WD20EJRX/basket/txt',name[i])
    print(path)
    f = open(path, 'r')
    alllines = f.readlines()
    f.close()
    f = open(path, 'w+')
    for eachline in alllines:
        a = re.sub('15 ', '0 ', eachline)
        f.writelines(a)
    f.close()