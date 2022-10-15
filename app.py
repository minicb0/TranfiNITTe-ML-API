from flask import Flask, request, jsonify
from amazoncaptcha import AmazonCaptcha
import os


app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'harrish07')

@app.route('/getCapt', methods = ['POST'])
def log():
    link = request.form['link']

    captcha = AmazonCaptcha.fromlink(link)
    solution = captcha.solve()
    return jsonify({'text' : solution})


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')