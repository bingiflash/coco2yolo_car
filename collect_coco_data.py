from pycocotools.coco import COCO
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import cv2
from skimage.draw import rectangle_perimeter
import random

dataTypes = ['train2017']
labels = ['car']
image_store_location = 'images\\'

print("filename,width,height,class,xmin,ymin,xmax,ymax")
for type in dataTypes:
    annFile = 'instances_{}.json'.format(type)
    coco = COCO(annFile)
    for label in labels:
        file_counter = 0
        catIds = coco.getCatIds(catNms=[label])
        imgIds = coco.getImgIds(catIds=catIds)
        random.shuffle(imgIds)
        for imgId in imgIds:
            img_data = coco.loadImgs(imgId)[0]
            try:
                image = io.imread(img_data['coco_url'])
            except:
                continue
            annIds = coco.getAnnIds(
                imgIds=img_data['id'], catIds=catIds, iscrowd=None)
            anns = coco.loadAnns(annIds)
            _ = io.imsave(image_store_location +label+'_'+'{:06}.jpg'.format(file_counter), image)
            with open(image_store_location+label+'_'+'{:06}.txt'.format(file_counter),'w') as f:
                for ann in anns:
                    xmin, ymin, width, height = ann['bbox']
                    cat_id = ann['category_id']
                    width_im = image.shape[1]
                    height_im = image.shape[0]
                    percentage_of_portion = ((width*height) *100) / (width_im*height_im)
                    # print('\t',percentage_of_portion)
                    if percentage_of_portion > 0.5 and percentage_of_portion < 90:
                        f.write('0 '+str((xmin+(width/2))/width_im)+' '+str((ymin+(height/2))/height_im)+' '+str(width/width_im)+' '+str(height/height_im)+'\n')        
                        # if file_counter <100 :
                        #     # print(xmin, ymin, xmin+width, ymin+height)
                        #     image = cv2.rectangle(image, (int(xmin), int(ymin)), (int(xmin+width), int(ymin+height)),(255,255,255), 1)
                # input()
            # cv2.imshow('image',image)
            # cv2.waitKey(0)
            file_counter = file_counter+1
            print(file_counter, len(imgIds))
            # if file_counter == 20:
            #     break
