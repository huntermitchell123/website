import os
import base64
from datetime import timedelta
from functools import update_wrapper
import io

import numpy as np
from flask import Flask, request, render_template, make_response, current_app
from flask_cors import CORS
import tflite_runtime.interpreter as tflite
from PIL import Image


app = Flask(__name__)
CORS(app, supports_credentials=True)


### SETTINGS ###

BASE_MODEL_PATH = os.path.dirname(os.path.abspath(__file__))

IMG_SIZE = 256

show_classifying_image = False # for debugging



### LOAD MODELS ###

interpreter_age = tflite.Interpreter(f"{BASE_MODEL_PATH}/models/age_prediction_model.tflite")
interpreter_gender = tflite.Interpreter(f"{BASE_MODEL_PATH}/models/gender_prediction_model.tflite")
interpreter_age.allocate_tensors()
interpreter_gender.allocate_tensors()

input_details_age = interpreter_age.get_input_details()
input_details_gender = interpreter_gender.get_input_details()
output_details_age = interpreter_age.get_output_details()
output_details_gender = interpreter_gender.get_output_details()


### CORS Decorator Function ###

def crossdomain(origin=None, methods=None, headers=None, max_age=21600,
                attach_to_all=True, automatic_options=True):
    """Decorator function that allows crossdomain requests.
      Courtesy of
      https://blog.skyred.fi/articles/better-crossdomain-snippet-for-flask.html
    """
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    # use str instead of basestring if using Python 3.x
    if headers is not None and not isinstance(headers, list):
        headers = ', '.join(x.upper() for x in headers)
    # use str instead of basestring if using Python 3.x
    if not isinstance(origin, list):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        """ Determines which methods are allowed
        """
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        """The decorator function
        """
        def wrapped_function(*args, **kwargs):
            """Caries out the actual cross domain code
            """
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers
            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            h['Access-Control-Allow-Credentials'] = 'true'
            h['Access-Control-Allow-Headers'] = \
                "Origin, X-Requested-With, Content-Type, Accept, Authorization"
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator



### DEFINE ROUTES ###

@app.route('/')
def home_get():
    return render_template('websiteMain.html')


@app.route('/project')
def project_get():
    return render_template('websiteProject.html')


@app.route('/project', methods=['POST', 'OPTIONS'])
@crossdomain(origin='*')
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
        interpreter_gender.set_tensor(input_details_gender[0]['index'], np.float32(pred_img))
        interpreter_gender.invoke()
        prediction_gender = interpreter_gender.get_tensor(output_details_gender[0]['index'])
        male_prob =  round(prediction_gender[0,0] * 100 , 2)
        female_prob = round( ( 1 - prediction_gender[0,0]) * 100 , 2)
        combinedString = 'Male Probability: ' + str(male_prob) + '%, Female Probability: ' + str(female_prob) + '%'

    if 'age' == request.values['predType']:
        interpreter_age.set_tensor(input_details_age[0]['index'], np.float32(pred_img))
        interpreter_age.invoke()
        prediction_age = interpreter_age.get_tensor(output_details_age[0]['index'])
        combinedString =  str( (int) (prediction_age[0,0]) ) + ' years old!'

    #print(combinedString)
    return combinedString


@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)