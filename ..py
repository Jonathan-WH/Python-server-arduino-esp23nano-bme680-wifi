import socket
import sys
import json

if len(sys.argv) == 1 or len(sys.argv) > 3:
    print("Usage: python server.py <ip> <port>")
    sys.exit(1)

UDP_IP = sys.argv[1]
UDP_PORT = int(sys.argv[2])

print("UDP target IP:", UDP_IP)
print("UDP target port:", UDP_PORT)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

counter = 0

while True:
    data, addr = sock.recvfrom(1024)
    data_dict = json.loads(data.decode('utf-8'))
    print("received message:", data_dict)
    if counter % 36 == 0:
        # send to firestore
        print("send to firestore")
    counter += 1