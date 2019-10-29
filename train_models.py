import keras as kr
from keras.models import Sequential
from keras.layers import Dense
import numpy as np
#import MNIST from keras.dataset
from keras.datasets import mnist
from keras import losses
from keras import optimizers
import tensorflow as tf;
#This will plot out images for testing
import matplotlib.pyplot as plt
#since MNIST images have 28*28 resolution
#define image rows and columns to be 28
image = 28
#this trains and tests the AI with the MNIST DATA
(x_train, y_train), (x_test, y_test) = mnist.load_data()
#template taken from keras site - code creates a Sequential model
model = Sequential()
#Here we are basically saying give me 64 neurons and setting relu to activation function
model.add(kr.layers.Dense(64, input_dim=1, activation="linear"))
#10 is number of classification since MNIST is 0 - 9 digits we use 10
model.add(kr.layers.Dense(10, activation=tf.nn.softmax))#optimizer - loss metric which is degree of error 0.01 is percentage of error
model.compile(loss=losses.categorical_crossentropy,
optimizer=optimizers.SGD(lr=0.01, momentum=0.9, nesterov=True))
print(x_train[0])
