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
    cv2.startWindowThread()
    #shows only black square
    cv2.imshow('img',x)
    cv2.waitKey()
    # Resize image
    x = cv2.resize(x,imgResize)

    #x = x.reshape(784,28, 28)
    out = model.predict(x)
    ###problem with above three lines - Think it's issue with model
    print(out)
    print(np.argmax(out, axis=1))
    response = np.argmax(out, axis=1)
    return str(x)
