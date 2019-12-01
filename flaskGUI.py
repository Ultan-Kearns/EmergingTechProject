from flask import Flask, escape, request,render_template
import train_models
from keras.models import load_model
import keras as kr
import numpy as np
app = Flask(__name__)
model = load_model('/trained.h5')

@app.route('/')
def home():
     return render_template("Home.html")
@app.route('/verify/', methods=['GET','POST'])
def verifyImage():
    #image is now going to server
    image = request.data 
    return render_template("Home.html")
