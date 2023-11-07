import sys
import base64
import re
import io
import cv2
import os

import numpy as np
from flask import Flask, request, url_for, redirect, render_template, jsonify
from tensorflow.keras.models import load_model
from PIL import Image


application = app = Flask(__name__)


### SETTINGS ###

BASE_MODEL_PATH = '/Users/huntermitchell/Documents/Documents/PYTHON_FILES/Face_Prediction' # os.path.dirname(os.path.abspath(__file__))

IMG_SIZE = 256

show_classifying_image = False # for debugging
test_a_pic = False # test manual pic at startup
PRED_PIC_PATH = '/Users/huntermitchell/Documents/Documents/PYTHON_FILES/Face_Prediction/testing_pics/hunterPic.jpeg'



### LOAD MODELS ###

model_gender = load_model(f"{BASE_MODEL_PATH}/gender_prediction_model")
model_age = load_model(f"{BASE_MODEL_PATH}/age_prediction_model")



if test_a_pic:
    test_img = cv2.imread(PRED_PIC_PATH)
    test_img = cv2.resize(test_img,(IMG_SIZE,IMG_SIZE))
    test_img = test_img.reshape(1,IMG_SIZE,IMG_SIZE,3)

    age_prediction = model_age.predict(test_img)
    print('age prediction: ', age_prediction[0,0])

    gender_prediction = model_gender.predict(test_img)
    print('gender prediction: ', gender_prediction[0,0])



@app.route('/')
def home_get():
    return render_template('websiteMain.html')


@app.route('/project')
def project_get():
    return render_template('websiteProject.html')


@app.route('/project', methods=['POST'])
def project_post():

    image_b64 = request.values['imageBase64']
    image_b64 = image_b64[22:] # get ride of first 22 characters
    image_bytes = base64.b64decode(image_b64) # is in bytes now 

    image_PIL = Image.open(io.BytesIO(image_bytes))
    #image_PIL.show() 

    dimensions = (IMG_SIZE,IMG_SIZE)
    pred_img = image_PIL.resize(dimensions)

    pred_img = np.array(pred_img)
    pred_img = pred_img[:,:,:3]

    if show_classifying_image:
        test_img = Image.fromarray(pred_img) # Does not support [0,1] images in RGB
        test_img.show() # This is the exact image that the model is classifying ! 

    pred_img = pred_img.reshape(1,IMG_SIZE,IMG_SIZE,3)
    
    #print(pred_img[0])
    #print(pred_img.shape)

    if 'gender' == request.values['predType']:
        prediction = model_gender.predict(pred_img)
        male_prob =  round(prediction[0,0] * 100 , 2)
        female_prob = round( ( 1 - prediction[0,0]) * 100 , 2)
        combinedString = 'Male Probability: ' + str(male_prob) + '%, Female Probability: ' + str(female_prob) + '%'

    if 'age' == request.values['predType']:
        prediction = model_age.predict(pred_img)
        combinedString =  str( (int) (prediction[0,0]) ) + ' years old!'

    print(combinedString)
    return combinedString


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)