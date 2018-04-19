import os
from flask import Flask, request, json
import requests
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import parser


app= Flask(__name__)

# @app.route('/', methods=["GET","POST"])

# def hello():
#     print ("hello")
#     return "Hello World!"

@app.route('/', methods=["GET","POST"])
def response():
    print ("response")
    if request.method == 'POST':
        print("post request made")
        data = request.get_json()
        message= parser.format_message(data['text'])
        if message != False:
            print(send_post(message))

        print(data['text'], data['sender_id'], data['name'])
        return "post"
    else:
        return "not a post request"

def temp():
    print (data, len(data), "TEST")

@app.route('/post', methods=["GET","POST"])
def send_post(message):
    post_url="https://api.groupme.com/v3/bots/post"
    print("send_post")
    mybot_id = "a618a63dd6defdbe37360bb0fa"
    msg = "Kristin be nice to me"
    data =  {'text':message, 'bot_id':mybot_id}
    #r = requests.post(post_url,json ={'text': message, 'bot_id':mybot_id})
    request = Request(post_url, urlencode(data).encode())
    json = urlopen(request).read.decode()
    print(json)
    return json


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0',port=port)
