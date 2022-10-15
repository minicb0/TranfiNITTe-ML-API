from flask import Flask, jsonify, request
from amazoncaptcha import AmazonCaptcha
import os


app = Flask(__name__)

@app.route('/')
def home():
    return "Fuck Off"

@app.route('/getCapt')
def getCapt():
    data = request.args['link']
    result = data[1:-1]
    captcha = AmazonCaptcha.fromlink(result)
    solution = captcha.solve()
    return jsonify({'text': solution})


if __name__ == "__main__":
    app.run()