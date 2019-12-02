from flask import Flask, escape, request,render_template
import train_models
from keras.models import load_model
from scipy.misc import imread, imresize
import keras as kr
import numpy as np
import base64
import tensorflow as tf
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
    #Refernce - https://www.pytorials.com/deploy-keras-model-to-production-using-flask/
    imgData = request.get_data()
    # encode image in base 64
    imgstr = str(re.search(r'base64,(.*)', str(imgData)))
    with open('/output.png', 'wb') as output:
        output.write(base64.b64decode(imgstr))
        print("OUTPUT")
    # Read image in
    x = imread('output.png', mode='L')
    # Resize image
    x = imresize(28,28)
    out = model.predict(x)
    print(out)
    print(np.argmax(out, axis=1))
    response = np.argmax(out, axis=1)
    return str(response[0])
    return render_template("Home.html")
