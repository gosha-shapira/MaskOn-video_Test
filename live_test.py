import cv2
import VideoTransformer

my_video_transformer = VideoTransformer.VideoTransformer()

cap = cv2.VideoCapture(1)

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")

print('starting the live prediction')

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    taged_frame = my_video_transformer.transform(frame)
    cv2.imshow('Input', taged_frame)

    c = cv2.waitKey(1)
    if c == 27:
        break

cap.release()
cv2.destroyAllWindows()