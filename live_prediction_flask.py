from flask import Flask, Response
from VideoTransformer import VideoTransformer
import cv2
import live_prediction

app = Flask(__name__)

video = cv2.VideoCapture(1)

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/predict")
def predict():
    global video
    return Response(live_prediction.predict(video),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)
