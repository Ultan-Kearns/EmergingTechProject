from flask import Flask, escape, request,render_template
import train_models
app = Flask(__name__)

@app.route('/')
def home():
     return render_template("Home.html");
@app.route('/verify')
def request():
     return render_template("Home.html");
