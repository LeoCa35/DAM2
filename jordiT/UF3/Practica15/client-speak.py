# Echo client program
import socket

HOST = 'localhost'    # The remote host
PORT = 50007              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#s.bind((HOST,PORT))
while True:
    print("Ponme Datos")
    datos = raw_input()
    sent = s.sendto(datos, (HOST,PORT))
    if datos == "bye":
        s.close() 
        break   

