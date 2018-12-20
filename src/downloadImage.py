#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 11:37:05 2018

@author: hanifa
"""
from google_images_download import google_images_download   #importing the library
import numpy as np
import pandas as pd
import os
import random
import gc
import cv2
#import matplotlib.pyplot as plt

class PreprocessData:
    def __init__(self):
        print("hello")
    def downloadData(self,imageNames):
        response = google_images_download.googleimagesdownload()   #class instantiation
        arguments = {"keywords":imageNames,"limit":100,"print_urls":True}   #creating list of arguments
        paths = response.download(arguments)   #passing the arguments to the function
        self.paths=paths
    def loadAllImages(self,img_dir):
        #img_dir='/home/hanifa/workspace/AIAP/AIAP-Week6/downloads/'
        self.apples=[img_dir+'Apples/'+i for i in os.listdir(img_dir+'Apples/')]
        self.oranges=[img_dir+'Oranges/'+i for i in os.listdir(img_dir+'Oranges/')]
        self.pears=[img_dir+'Pears/'+i for i in os.listdir(img_dir+'Pears/')]
        self.allImg=self.apples+self.oranges+self.pears
        
    def createDataset(self,data,i):
        for f in data:
            img=cv2.resize(cv2.imread(f),(224,224),interpolation=cv2.INTER_CUBIC)
            RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            self.X.append(RGB_img)
            self.y.append(i)
            
    def getTestImages(self):
        img_dir='/home/hanifa/workspace/AIAP/AIAP-Week6/downloads_test/'
        apples=[img_dir+'Apples/'+i for i in os.listdir(img_dir+'Apples/')]
        oranges=[img_dir+'Oranges/'+i for i in os.listdir(img_dir+'Oranges/')]
        pears=[img_dir+'Pears/'+i for i in os.listdir(img_dir+'Pears/')]
        allImg=apples+oranges+pears
        
        self.X=[]
        self.y=[]
        self.createDataset(apples,0)
        self.createDataset(pears,1)
        self.createDataset(oranges,2)   
        
if __name__=="__main__":
    one=PreprocessData()
    one.getTestImages()


#img=plt.imread(train_apples[0])
#plt.imshow(img)
#plt.show()

