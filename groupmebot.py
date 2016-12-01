import os
from flask import Flask
from flask import request
import requests


app= Flask(__name__)

@app.route('/', methods=["GET","POST"])

def hello():
    print ("hello")
    return "Hello World!"

@app.route('/', methods=["GET","POST"])
def response():
    print ("response")
    if request.method == 'POST':
        data = request.form

    return data['text']

def temp():
    print (data, len(data), "TEST")

def send_post():
    print("send_post")
    mybot_id = "b3eabaca8f17b655ed331166ba"
    msg = "Hello"
    r = requests.post('https://api.groupme.com/v3/bots/post',data ={
        'bot_id':'mybot_id', 'text':'msg'})


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0',port=port)
