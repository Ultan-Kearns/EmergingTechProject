from flask import Flask, escape, request,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("Home.html");
