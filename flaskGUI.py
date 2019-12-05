from flask import Flask, escape, request,render_template
import train_models
from keras.models import load_model
from scipy.misc import imread, imresize
import keras as kr
import numpy as np
import base64
import tensorflow as tf
import cv2
#handels regular expressions
import re
app = Flask(__name__)
model = load_model('/trained.h5')
@app.route('/')
def home():
     return render_template("Home.html")
@app.route('/verify/', methods=['GET','POST'])
def verifyImage():
    #Verify images
    #Reference - https://www.pytorials.com/deploy-keras-model-to-production-using-flask/
    imgData = request.get_data()
    imgResize = (28,28)
    # encode image in base 64
    imgstr = re.search(b'base64,(.*)', imgData).group(1)
    with open('output.png','wb') as output:
        output.write(base64.decodebytes(imgstr))
    # Read image in
    x = cv2.imread('output.png', cv2.IMREAD_GRAYSCALE)
    # Resize image
    x = cv2.resize(x,(28,28))
    #reshape image
    x = x.reshape(1, 28, 28)
    out = model.predict(x)
    #ValueError: Error when checking input: expected flatten_1_input to have 3 dimensions, but got array with shape (28, 28)
    ###problem with model.predict
    #print(out)
    #print(np.argmax(out, axis=1))
    #response = np.argmax(out, axis=1)
    #should be response
    return str(x)
