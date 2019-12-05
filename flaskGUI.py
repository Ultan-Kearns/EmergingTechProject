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
import os
app = Flask(__name__)
# Reference + refactor both
global model, graph
@app.route('/')
def home():
     return render_template("Home.html")
@app.route('/verify/', methods=['GET','POST'])

def init():
  json_file = open(os.getcwd() + '/model_json','r')
  loaded_model_json = json_file.read()
  json_file.close()
  loaded_model = model_from_json(loaded_model_json)
  #load weights into new model
  loaded_model.load_weights("trained.h5")
  print("Loaded Model from disk")
  #compile and evaluate loaded model
  loaded_model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
  graph = tf.get_default_graph()
  return loaded_model,graph
# initialize these variables
model, graph = init()
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
    with tf.Graph().as_default():
        tf_train_dataset = graph.get_tensor_by_name('x_train')
        tf_train_labels = graph.get_tensor_by_name('x_test')
        with tf.Session(graph=graph) as session:
            out = model.predict(x)
    ###problem with model.predict
    #print(out)
    #print(np.argmax(out, axis=1))
    #response = np.argmax(out, axis=1)
    #should be response
    return str(x)
