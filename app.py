import json
from flask import Flask, jsonify, request
from amazoncaptcha import AmazonCaptcha
from PIL import Image
import pytesseract
import urllib.request
import os


app = Flask(__name__)

@app.route('/')
def home():
    return "This is a captcha solver api made by Trojan Titans! We also included our ML algorithms in it and we are connecting it to backend through this API."

@app.route('/getCapt')
def getCapt():
    data = request.args['link']
    result = data[1:-1]

    f = open('cap.png','wb')
    f.write(urllib.request.urlopen(result).read())
    f.close()

    # urllib.request.urlretrieve(result, "cap.jpg")
    col = Image.open("cap.png")
    gray = col.convert('L')
    bw = gray.point(lambda x: 255 if x>=190 else 0, '1')
    bw.save('result.png')

    solution = pytesseract.image_to_string(Image.open('result.png'))
    solution = solution.strip()
    # captcha = AmazonCaptcha.fromlink(result)
    # solution = captcha.solve()
    solution = str(solution)
    return jsonify({"text": solution})

if __name__ == "__main__":
    app.run()