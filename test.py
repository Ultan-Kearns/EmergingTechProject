from keras.models import Sequential
from keras.layers import Dense
from keras.datasets import mnist

#since MNIST images have 28*28 resolution
#define image rows and columns to be 28
image_rows = image_columns = 28
#template taken from keras site
model = Sequential()
model.add(Dense(units=64, activation='relu', input_dim=100))
model.add(Dense(units=10, activation='softmax'))
model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])
