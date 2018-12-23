# -*- coding: utf-8 -*-
import os
from flask import Flask, render_template
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField
import numpy as np
import keras
#import matplotlib.pyplot as plt
import cv2
# import seaborn as sns
#from sklearn.model_selection import train_test_split
#from keras import layers,models,optimizers
#from keras.preprocessing.image import ImageDataGenerator
#from keras.callbacks import EarlyStopping
from keras.models import load_model
#import requests
#from PIL import Image
#import io

'''
import tensorflow as tf
from keras.backend.tensorflow_backend import set_session

config = tf.ConfigProto(
    gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.8)
)
config.gpu_options.allow_growth = True
session = tf.Session(config=config)
set_session(session)
'''
'''
import tensorflow as tf
global graph,model
graph = tf.get_default_graph()
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = 'I have a dream'
app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd()

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)  # set maximum file size, default is 16MB

global new_model
new_model = load_model('model_keras.h5')
new_model._make_predict_function()

'''
from keras.applications.resnet50 import ResNet50
global new_model
new_model = ResNet50(weights='imagenet')
'''


class UploadForm(FlaskForm):
    photo = FileField(validators=[FileAllowed(photos, u'Image only!'), FileRequired(u'File was empty!')])
    submit = SubmitField(u'Upload')

def classifiyImage(img):
    y_mapping={0:'Apples',1:'Pears',2:'Oranges'}
    img=img/255
    img=img.reshape(1,224,224,3)
    print(img.shape)
    print(new_model.summary())
    '''
    with graph.as_default():
        '''
    
    prob=new_model.predict(img)
    '''
    classes=new_model.predict_classes(img)
    print("Our algorithm says it is %s with a %d%% accuracy" %(y_mapping[classes[0]],int(prob[0][classes][0]*100)))
    '''
#    return y_mapping[classes[0]],int(prob[0][classes][0]*100)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    form = UploadForm()
    if form.validate_on_submit():
        filename = photos.save(form.photo.data)
        file_url = photos.url(filename)



        img=cv2.resize(cv2.imread(filename),(224,224),interpolation=cv2.INTER_CUBIC)
        RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        classifiyImage(RGB_img)

        
    else:
        file_url = None
    return render_template('index.html', form=form, file_url=file_url)





if __name__ == '__main__':
    app.run(debug = True)
