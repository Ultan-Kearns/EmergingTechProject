from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    greeting = request.args.get("greeting", "User")
    return f'Welcome, {escape(greeting)}!'
