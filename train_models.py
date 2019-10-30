from keras.models import Sequential
from keras.layers import Dense
import numpy as np
#import MNIST from keras.dataset
from keras.datasets import mnist
from keras import losses
from keras import optimizers
import keras as kr
import tensorflow as tf
#This will plot out images for testing
import matplotlib.pyplot as plt
#since MNIST images have 28*28 resolution
#define image rows and columns to be 28
image_rows = image_cols = 28
#this trains and tests the AI with the MNIST DATA
(x_train, y_train), (x_test, y_test) = mnist.load_data()
#Define sequential model
model = kr.Sequential([
    #flatten the layers to fit input size
    kr.layers.Flatten(input_shape=(image_cols, image_rows)),
    #here was basically see give me x neurons
    #Used https://keras.io/activations/ to research activations
    kr.layers.Dense(10, activation='relu'),
    kr.layers.Dense(10, activation='relu'),
    kr.layers.Dense(10, activation='relu'),
    #research activation functions weird thing happens when switch to relu
    kr.layers.Dense(1024, activation='softmax'),
])
 #here we compile the model
model.compile(optimizer='Adadelta',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
#here we will train the model using training set and testing
model.fit(x_train,y_train,epochs=4)
#score based on test models
score = model.evaluate(x_test, y_test, verbose=0)
