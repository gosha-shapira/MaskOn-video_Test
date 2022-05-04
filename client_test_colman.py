import socket
import struct
#------ Test connectivity to the server ------#
# Client socket
# create an INET, STREAMing socket : 
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_ip = '10.10.248.140' 
port = 10151 # Port to listen on (non-privileged ports are > 1023)

# now connect to the web server on the specified port number
client_socket.connect((host_ip,port))

# 'b' or 'B'produces an instance of the bytes type instead of the str type
# used in handling binary data from network connections
data = b""
# Q: unsigned long long integer(8 bytes)
payload_size = struct.calcsize("Q")

while True:
    print('sending \'Hello\' to the server')
    client_socket.sendmsg('Hello')
    print('sent to the server')