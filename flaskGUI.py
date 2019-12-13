from flask import Flask, escape, request,render_template
import train_models
from keras.models import load_model
from PIL import Image
import keras as kr
import numpy as np
import base64
import tensorflow as tf
import cv2
from model_load import init
from tensorflow.python.keras import Sequential
#handles regular expressions
import re
import os
app = Flask(__name__)
@app.route('/')
def home():
     return render_template("Home.html")
@app.route('/verify/', methods=['GET','POST'])
def verifyImage():
    #Verify images
    #Reference - https://www.pytorials.com/deploy-keras-model-to-production-using-flask/
    imgData = request.get_data()
    # encode image in base 64
    imgstr = re.search(r'base64,(.*)', str(imgData)).group(1)
    with open('output.png', 'wb') as output:
        output.write(base64.b64decode(imgstr))
    # Read image in
    x = cv2.imread(os.getcwd() + '/output.png',cv2.IMREAD_GRAYSCALE)
    # Add borders to image
    RED = [255,0,0]
    x = cv2.copyMakeBorder( x, 4,4, 4, 4, cv2.BORDER_CONSTANT,value=RED)
    # Resize image
    x = cv2.resize(x,(28,28))
    #reshape image
    x = x.reshape(1, 28, 28)
    graph,model = init()
    with graph.as_default():
        out = model.predict(x)
        print("X",x)
        print(np.argmax(out, axis=1))
        response = np.argmax(out, axis=1)
        #output response
        print("PREDICTED")
        return str(response[0])
