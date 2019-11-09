from keras.models import Sequential
from keras.layers import Dense
import numpy as np
from keras.datasets import mnist
from keras import losses
from keras import optimizers
import keras as kr
import matplotlib.pyplot as plt
import h5py
import os
def train():
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
        kr.layers.Dense(1024, activation='softmax'),
    ])
    #this will show what the model looks like
    model.summary();
    #here we compile the model
    #Optimzers - compared optimizers at https://keras.io/optimizers/
    model.compile(optimizer='Adadelta',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    #here we will train the model using training set and testing for x epochs
    #using 256 batchs for each model
    model.fit(x_train,y_train,epochs=6, batch_size=256)
    #prompt user for path
    path = input("Please enter directory where you want to save the model: ")
    try:
        #check path exists if not make path
        print(os.path.exists(path) == False)
        if(os.path.exists(path) == False):
            os.mkdir(path)
        os.chdir(path)
        #save model
        model.save("trained.h5")
        print("Model saved to " + path)
    except:
        print(path + " not found please make directory using mkdir")
        menu();

def prediction():
    print("Predict......")

def menu():
    print("""Python App to classify image using the MNIST Dataset and Keras - Ultan Kearns G00343745""")
    print("1. To train Model")
    print("2. To make a prediction")
    x = input("Please enter the option you would like to choose: ")
    if(x == "1"):
        train()
    elif(x == "2"):
        #make prediction function
        print("not implemented yet")
    else:
        print("Not a valid option")
        menu();
menu()
