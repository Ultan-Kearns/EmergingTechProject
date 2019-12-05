from keras.models import Sequential
from keras.layers import Dense
import numpy as np
from keras.datasets import mnist
from keras import losses
from keras import optimizers
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
import keras as kr
import matplotlib.pyplot as plt
import h5py
import os
from keras.models import load_model

def train():
    #since MNIST images have 28*28 resolution
    #define image rows and columns to be 28
    image_rows = image_cols = 28
    #x_train and y_ train represent training data
    # x_test and y_ test represent category labels
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    #Define sequential model https://keras.io/models/model/ - resource taught me about modelss
    model = kr.Sequential([
        #flatten the layers to fit input size
        kr.layers.Flatten(input_shape=(image_cols, image_rows)),
        #here was basically see give me x neurons
        # I used 4 RELU layers and 1 softmax layer
        #Used https://keras.io/activations/ to research activations
        kr.layers.Dense(64, activation='relu'),
        kr.layers.Dense(64, activation='relu'),
        kr.layers.Dense(64, activation='relu'),
        kr.layers.Dense(64, activation='relu'),
        #softmax normalizes the dataset - 10 neurons due to only 10 possible digits
        kr.layers.Dense(10, activation='softmax'),
    ])
    # normalize inputs from 0-255 to 0-1
    x_train = x_train / 255
    x_test = x_test / 255
    #this will show what the model looks like
    model.summary()
    #here we compile the model
    #Optimzers - compared optimizers at https://keras.io/optimizers/
    #categorical crossentropy - standard loss function
    model.compile(optimizer='adadelta',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    #here we will train the model using training set and testing for x epochs
    #using 256 batchs for each model
    model.fit(x_train,y_train,epochs=10, batch_size=128)
    # Final evaluation of the model test loss and accuracy -  https://medium.com/coinmonks/handwritten-digit-prediction-using-convolutional-neural-networks-in-tensorflow-with-keras-and-live-5ebddf46dc8
    final_score = model.evaluate(x_test, y_test, verbose=0)
    print("final score - test loss & accuracy: ")
    print(final_score)
    print(" Loss ",final_score[0])
    print(" ACC: ", final_score[1])
    #prompt user for path
    path = input("Please enter directory where you want to save the model: ")
    try:
        #if path blank use cur dir
        if(path == ""):
            path = os.getcwd()
            print("PATH = " + path)
        #check path exists if not make path
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
    path = input("Please enter directory where model is stored: ")
    try:
        #if path blank use cur dir - this is for specifying file direction
        if(path == ""):
            path = os.getcwd()
            print("PATH = " + path)
            #check path exists if not call menu again and alert user
            if(os.path.exists(path) == False):
                print("path doesn't exist")
                path = ""
                menu();
        print("Loaded model")
        #Found info at https://keras.io/getting-started/faq/#how-can-i-save-a-keras-model
        model = load_model(path + "/" + "trained.h5")
        #load in the model
        (x_train, y_train), (x_test, y_test) = mnist.load_data()
        #predict random image and then show also generate randint between 1 and 10000 - size of test data
        prediction = model.predict(x_test)
        random = np.random.randint(1,10000)
        plt.imshow(x_test[random])
        plt.show()
    except:
        print("File doesn't exist")
        menu()
def menu():
    print("""Python App to classify image using the MNIST Dataset and Keras - Ultan Kearns G00343745""")
    print("1. To train Model")
    print("2. To make a prediction")
    print("3. To exit")
    x = input("Please enter the option you would like to choose: ")
    if(x == "1"):
        train()
        #Reference - https://www.pytorials.com/mnist-handwritten-digits-classification-using-keras/
        model_json = model.to_json()
        with open("model_json", "w") as json_file:
            json_file.write(model.json)
    elif(x == "2"):
        #make prediction function
        prediction()
        menu()
    elif(x == "3"):
        return
    else:
        print("Not a valid option")
        menu();
menu()
