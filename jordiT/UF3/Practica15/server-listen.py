# Echo server program
import socket
import time

HOST = 'localhost'                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST,PORT))
while True:
    data, addr = s.recvfrom(1024)
    s.sendto(data, addr)
    print(addr ,data)
    if data == "bye":
        time.sleep(1)
        s.close()
