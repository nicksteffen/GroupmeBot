import os
from flask import Flask
from flask import request
import requests


app= Flask(__name__)

# @app.route('/', methods=["GET","POST"])

# def hello():
#     print ("hello")
#     return "Hello World!"

@app.route('/', methods=["GET","POST"])
def response():
    print ("response")
    if request.method == 'POST':
        data = request.form['text']
        print("post request made")
        print(len(data))
        print( data)
        return "post"
    else:
        return "not a post request"

def temp():
    print (data, len(data), "TEST")

@app.route('/post', methods=["GET","POST"])
def send_post():
    print("send_post")
    mybot_id = "b3eabaca8f17b655ed331166ba"
    msg = "Kristin be nice to me"
    r = requests.post("https://api.groupme.com/v3/bots/post",
                      data ={'text': msg, 'bot_id':mybot_id})
    return r.url


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0',port=port)
