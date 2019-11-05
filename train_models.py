from keras.models import Sequential
from keras.layers import Dense
import numpy as np
from keras.datasets import mnist
from keras import losses
from keras import optimizers
import keras as kr
import matplotlib.pyplot as plt
#since MNIST images have 28*28 resolution
#define image rows and columns to be 28
image_rows = image_cols = 28
#x_train and y_ train represent training data
# x_test and y_ test represent testing data
(x_train, y_train), (x_test, y_test) = mnist.load_data()
#Define sequential model https://keras.io/models/model/ - resource taught me about modelss
model = kr.Sequential([
    #flatten the layers to fit input size
    kr.layers.Flatten(input_shape=(image_cols, image_rows)),
    #here was basically see give me x neurons
    #Used https://keras.io/activations/ to research activations
    kr.layers.Dense(64, activation='relu'),
    kr.layers.Dense(64, activation='relu'),
    kr.layers.Dense(64, activation='relu'),    #research activation functions weird thing happens when switch to relu
    kr.layers.Dense(512, activation='softmax'),
])
#this will show what the model looks like
model.summary();
#here we compile the model
#Optimzers - compared optimizers at https://keras.io/optimizers/
model.compile(optimizer='Adadelta',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
#here we will train the model using training set and testing for x epochs
#using 512 batchs for each model
model.fit(x_train,y_train,epochs=10,batch_size=512)
