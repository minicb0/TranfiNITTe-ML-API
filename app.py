from flask import Flask, request
from amazoncaptcha import AmazonCaptcha
import os


app = Flask(__name__)

@app.route('/')
def home():
    return "Fuck Off"

@app.route('/getCapt', methods = ['POST'])
def log():
    link = request.form['link']

    captcha = AmazonCaptcha.fromlink(link)
    solution = captcha.solve()
    return solution


if __name__ == "__main__":
    app.run()