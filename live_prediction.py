import cv2
from VideoTransformer import VideoTransformer


my_video_transformer = VideoTransformer()

def predict(video):
    while True:
        ret, frame = video.read()
        frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
        taged_frame = my_video_transformer.transform(frame)
        img = taged_frame.tobytes()
        
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')