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
import matplotlib.pyplot as plt

class PreprocessData:
    def __init__(self):
        print("hello")
    def downloadData(self,imageNames):
        response = google_images_download.googleimagesdownload()   #class instantiation
        arguments = {"keywords":imageNames,"limit":100,"print_urls":True}   #creating list of arguments
        paths = response.download(arguments)   #passing the arguments to the function
        self.paths=paths
    def loadAllImages(self):
        img_dir='/home/hanifa/workspace/AIAP/AIAP-Week6/downloads/'
        self.apples=[img_dir+'Apples/'+i for i in os.listdir(img_dir+'Apples/')]
        self.oranges=[img_dir+'Oranges/'+i for i in os.listdir(img_dir+'Oranges/')]
        self.pears=[img_dir+'Pears/'+i for i in os.listdir(img_dir+'Pears/')]
        self.allImg=self.apples+self.oranges+self.pears
        
        
        
        

if __name__=="__main__":
    #one=PreprocessData()
    #one.downloadData("Apples,Pears,Oranges")
    img_dir='/home/hanifa/workspace/AIAP/AIAP-Week6/downloads/'
    train_apples=[img_dir+'Apples _smaller/'+i for i in os.listdir(img_dir+'Apples _smaller/')]

#img=plt.imread(train_apples[0])
#plt.imshow(img)
#plt.show()

