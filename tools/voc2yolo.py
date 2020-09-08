import copy
import glob
import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
 
classes = ["person"]  #类别
 
def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)
 
def convert_annotation(voc_path,yolo_path,image_id):
    
    in_file = open(voc_path+'/%s.xml'%(image_id))
    
    out_file = open(yolo_path+'/%s.txt'%(image_id),'w') #生成txt格式文件

    tree=ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')  
    w = int(size.find('width').text)
    h = int(size.find('height').text)
 
    for obj in root.iter('object'):
        cls = obj.find('name').text
        if cls not in classes :
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')   
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w,h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')
        
if __name__ == '__main__':
    voc_path = '/home/hkuit164/Desktop/0619_data/0619_origin/test_gray_anno'
    yolo_path = '/home/hkuit164/Desktop/0619_data/0619_origin/tmp'
    name = glob.glob(os.path.join(voc_path,'*.xml'))
    name = map(lambda x:x.split('/')[-1].split('.')[0],name)

    for image_id in list(name):

        convert_annotation(voc_path,yolo_path,image_id)
