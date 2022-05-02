import cv2
import datetime
import VideoTransformer

my_video_transformer = VideoTransformer.VideoTransformer()

#---------------- Dealing with the video ----------------#
#vid_cap = cv2.VideoCapture("/Users/gosha/PycharmProjects/MaskOn-Video/Video Test/Movie on 30-04-2022 at 12.27.mp4")
vid_cap = cv2.VideoCapture("/Users/gosha/PycharmProjects/MaskOn-Video/Video Test/Movie on 30-04-2022 at 13.12.mp4")

# store every frame from video file
success, image = vid_cap.read()
count = 0
frames = []
width = 1080
hight = 720

start_time = datetime.datetime.now()

while vid_cap.isOpened():
    success, image = vid_cap.read()
    if success:
        img = cv2.resize(image, (width, hight))
        tagged_img = my_video_transformer.transform(img)
        frames.append(tagged_img)
        count += 1
    else:
        break

vid_cap.release()

newframes = []

writer = cv2.VideoWriter("/Users/gosha/PycharmProjects/MaskOn-Video/Video Test/taged_outputvideo1.mp4", cv2.VideoWriter_fourcc(*"mp4v"), 30, (width, hight))

for i in range(0, len(frames)):
    newframes.append(frames[i])
    writer.write(frames[i])  # write frame into output vid

writer.release()
print('Finished')
print(f'The time it took to convert is: {datetime.datetime.now() - start_time}')