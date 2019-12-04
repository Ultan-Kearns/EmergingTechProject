# Emerging Technology Project - Using Keras and Tensorflow to create an image classifier in Python
## by Ultan Kearns - Student Number G00343745
### Table of Contents
- [Prerequisites](#Prerequisites)
- [How To Run](#How)
- [About Flask](#AboutFlask)
- [About Keras](#About Keras)
- [Summary](#Summary)
# Prerequisites to run this project <a name = "Prerequisites"></a>
You must have Python and Keras installed on your machine to run this project. To install Keras please use "pip3 install keras" in the terminal without quotes. You must also have flask which can be installed easily using the above command but replace "keras" with Flask. You must also have tensorflow installed on your machine which can be installed using "pip3 install tensorflow"
# How to run this application <a name = "How"></a>
To run the Flask GUI you need to run the command "env FLASK_APP=flaskGUI.py flask run" without quotes, this is assuming you are in the project directory and that you have Flask & Python installed on your machine.
# About Flask<a name = "AboutFlask"></a>
<img src = "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Flask_logo.svg/1920px-Flask_logo.svg.png" alt="Flask Icon"/>
Flask is a web framework written in python. Flask is used in this project to provide the user with an UI which they can use to draw the digits on a canvas.  The UI also offers then the options to clear the canvas and to send the image from the canvas to the model which will verify the digit.  Flask was voted the most popular framework in 2018 to cite Wikipedia <a href="https://en.wikipedia.org/wiki/Flask_%28web_framework%29">Flask wiki</a>
# About Keras
# Summary of project <a name = "Summary"></a>
This project is programmed in python and uses HTML for a frontend.  The aim of this project is to produce an image classifier in python using Keras and Tensorflow to identify digits drawn by the user which it performs using the MNIST dataset as a template and compares them with the user drawn digits to reach a conclusion.
