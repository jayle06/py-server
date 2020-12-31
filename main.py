from flask import Flask, request
from youtube import yt_videos
from instagram import insta_down
from facebook import fb_down_vd

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello client!"

@app.route('/youtube', methods=['GET'])
def youtube_api():
    link = request.args.get("url")
    return yt_videos(link)

@app.route('/instagram', methods=['GET'])
def insta_api():
    link = request.args.get("url")
    return insta_down(link)

@app.route('/facebook', methods=['GET'])
def fb_api():
    link = request.args.get("url")
    return fb_down_vd(link)

if __name__ == '__main__' :
    app.run(host='192.168.1.9', port=5000, debug=True)        #host = your ip address
