import os
from flask import Flask
from flask import request
import requests


app= Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def hello(self):
    return "Hello World!"

# def response(self):
#     if request.method == 'POST':
#         data = request.form

#     return data['text']

# def send_post(self):
#     mybot_id= 0
#     msg = "Hello"
#     r = requests.post('https://api.groupme.com/v3/bots/post',data ={
#         'bot_id':'mybot_id', 'text':'msg'})


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0',port=port)
