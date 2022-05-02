import socket
import cv2
import pickle
import struct
import imutils

# Client socket
# create an INET, STREAMing socket : 
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_ip = '<localhost>'# Standard loopback interface address (localhost)
port = 10050 # Port to listen on (non-privileged ports are > 1023)

# now connect to the web server on the specified port number
client_socket.connect((host_ip,port)) 

#'b' or 'B'produces an instance of the bytes type instead of the str type
#used in handling binary data from network connections
data = b""
# Q: unsigned long long integer(8 bytes)
payload_size = struct.calcsize("Q")

while True:
    client_socket,addr = client_socket.accept()
    print('Connection from:',addr)
    if client_socket:
        vid = cv2.VideoCapture(0)
        while(vid.isOpened()):
            img,frame = vid.read()
            a = pickle.dumps(frame)
            #meta_data = 
            message = struct.pack("Q",len(a))+a
            client_socket.sendall(message)
            # recieve the data from the server and diaplay it:
            
            #-------------#
            cv2.imshow('Sending...',frame)
            key = cv2.waitKey(10) 
            if key ==13:
                client_socket.close()
            #-------------#