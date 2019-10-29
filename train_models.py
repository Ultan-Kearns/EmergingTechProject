from keras.models import Sequential
from keras.layers import Dense
import numpy as np
#import MNIST from keras.dataset
from keras.datasets import mnist
from keras import losses
from keras import optimizers

#since MNIST images have 28*28 resolution
#define image rows and columns to be 28
image_rows = image_columns = 28
#this trains and tests the AI with the MNIST DATA
(x_train, y_train), (x_test, y_test) = mnist.load_data()
#template taken from keras site - code creates a Sequential model
model = Sequential()
model.add(Dense(units=64, activation='relu', input_dim=100))
model.add(Dense(units=10, activation='softmax'))
#optimizer
model.compile(loss=losses.categorical_crossentropy,
optimizer=optimizers.SGD(lr=0.01, momentum=0.9, nesterov=True))
#load data
print(mnist.load_data());
plt.imshows(x_train[0])
