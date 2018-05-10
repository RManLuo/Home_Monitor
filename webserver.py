# -*- coding: utf-8 -*-
import cv2
from flask import Flask, render_template, Response
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('./index.html')#z主页
def gen(frame):
    ret,frame=cv2.imencode('.jpg',frame)
    return frame.tobytes()
def broadcast():
    while True:
        try:
            image=cv2.imread('./cache/online.jpg')
            jpeg = cv2.imencode('.jpg', image)[1]
            frame=jpeg.tobytes()
            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame+ b'\r\n\r\n')
        except:
            pass
@app.route('/watch')
def watch():
    return Response(broadcast(),mimetype='multipart/x-mixed-replace; boundary=frame')
if __name__ == '__main__':
    app.run()