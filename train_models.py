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
from keras.layers import Conv2D, MaxPooling2D
#since MNIST images have 28*28 resolution
#define image rows and columns to be 28
image = 28
#this trains and tests the AI with the MNIST DATA
(x_train, y_train), (x_test, y_test) = mnist.load_data()
#template taken from keras site - code creates a Sequential model
model = kr.Sequential([
    kr.layers.Flatten(input_shape=(28, 28)),
    kr.layers.Dense(128, activation='relu'),
    kr.layers.Dense(10, activation='softmax')
])
print(x_train.shape)


#10 is number of classification since MNIST is 0 - 9 digits we use 10
model.add(kr.layers.Dense(10, activation=tf.nn.softmax))
#here we compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
#here we will train the model using training set and testing
model.fit(x_train,y_train,epochs=10)
#score based on test models
score = model.evaluate(x_test, y_test, verbose=0)
