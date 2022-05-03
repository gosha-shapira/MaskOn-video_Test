import socket
import cv2
import pickle
import struct
import imutils
import VideoTransformer

my_video_transformer = VideoTransformer.VideoTransformer()

# Server socket
# create an INET, STREAMing socket
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_name  = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print('HOST IP:',host_ip)
port = 10050
socket_address = (host_ip,port)
print('Socket created')

# bind the socket to the host. 
#The values passed to bind() depend on the address family of the socket
server_socket.bind(socket_address)
print('Socket bind complete')

#listen() enables a server to accept() connections
#listen() has a backlog parameter. 
#It specifies the number of unaccepted connections that the system will allow before refusing new connections.
server_socket.listen(5)
print('Socket now listening')

#'b' or 'B'produces an instance of the bytes type instead of the str type
#used in handling binary data from network connections
data = b""
# Q: unsigned long long integer(8 bytes)
payload_size = struct.calcsize("Q")


while True:
    client_socket,addr = server_socket.accept()
    print('Connection from:',addr)
    if client_socket:
        while len(data) < payload_size:
            packet = client_socket.recv(4*1024)
            if not packet: break
            data+=packet
        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack("Q",packed_msg_size)[0]
        while len(data) < msg_size:
            data += client_socket.recv(4*1024)
        frame_data = data[:msg_size]
        data  = data[msg_size:]
        frame = pickle.loads(frame_data)
        taged_frame = my_video_transformer.transform(frame)
        a = pickle.dumps(taged_frame)
        message = struct.pack("Q",len(a))+a
        client_socket.sendall(message)
        # key = cv2.waitKey(5) 
        # if key ==13:
        #     client_socket.close()