# Emerging Technology Project - Using Keras and Tensorflow to create an image classifier in Python
## by Ultan Kearns - Student Number G00343745
## Note this project was produced as part of a fourth year module - Emerging Technologies

<img src = "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fyt3.ggpht.com%2F-lf7kKDOqMC0%2FAAAAAAAAAAI%2FAAAAAAAAAAA%2FkC9tDGn12mE%2Fs900-c-k-no-mo-rj-c0xffffff%2Fphoto.jpg&f=1&nofb=1" style="margin:auto; width:200px;display:block" height = "250px" alt = "gmit logo"   />

### Table of Contents
- [Prerequisites](#Prerequisites)
- [How To Run](#How)
- [About Flask](#AboutFlask)
- [About Keras](#AboutKeras)
- [Summary](#Summary)
# Prerequisites to run this project <a name = "Prerequisites"></a>
You must have Python and Keras installed on your machine to run this project. To install Keras please use "pip3 install keras" in the terminal without quotes. You must also have flask which can be installed easily using the above command but replace "keras" with Flask. You must also have tensorflow installed on your machine which can be installed using "pip3 install tensorflow"
# How to run this application <a name = "How"></a>
To run the Flask GUI you need to run the command "env FLASK_APP=flaskGUI.py flask run" without quotes, this is assuming you are in the project directory and that you have Flask & Python installed on your machine.  I have also included a CLI version, just run python "train_models.py" - yup it's that easy, you'll be presented with options to train the model, verify a digit, and to quit the application - revolutionary I know....
# About Flask<a name = "AboutFlask"></a>
<img src = "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Flask_logo.svg/1920px-Flask_logo.svg.png"  height = "250px"     alt="Flask Icon" width="100vw" style="margin:auto; width:200px;display:block"/> 
- image courtesy of wikipedia.
Flask is a web framework written in python. Flask is used in this project to provide the user with an UI which they can use to draw the digits on a canvas.  The UI also offers then the options to clear the canvas and to send the image from the canvas to the model which will verify the digit.  Flask was voted the most popular framework in 2018 to cite Wikipedia <a href="https://en.wikipedia.org/wiki/Flask_%28web_framework%29">Flask wiki</a>
# About Keras<a name="AboutKeras"></a>
<img src ="https://s3.amazonaws.com/keras.io/img/keras-logo-2018-large-1200.png" width ="250px" height = "250px"  alt="Keras logo" width="100vw" style="margin:auto; width:200px;display:block"/> 
- image courtesy of keras.io.
Keras is a high level neural network API which is programmed in Python.  Using Keras it is relatively simple to program a neural network in very few lines of code.  Keras has multiple features which make it desirable when using machine learning, these include but are not limited to: a very simple syntax to setting up models, a number of optimizers and activation functions, and a comprehensive site which contains all the information needed about Keras to get it up and running.  I used Keras to take in the MNIST digit dataset and train a model based upon the dataset.  I found Keras very easy to use and the documentation comprehensive.
# Summary of project <a name = "Summary"></a>
This project is programmed in python and uses HTML for a frontend.  The aim of this project is to produce an image classifier in python using Keras and Tensorflow to identify digits drawn by the user which it performs using the MNIST dataset as a template and compares them with the user drawn digits to reach a conclusion.
