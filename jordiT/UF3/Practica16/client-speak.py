# Echo client program
import socket, threading


HOST = 'localhost'       # The remote host
PORT = 50007             # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


s.connect((HOST,PORT))
datos = ""

def recibirMensaje(s):
    while True:
        #print("el server dice: ")
        a = s.recv(1024)
        print a
        if a == "bye":
            print("se cierra la conexion")
            s.sendall(a)
            break
        

def enviarMensaje(s,datos):
    while True:
        datos = raw_input()
        if datos:
            s.sendall(datos)

        if datos == "bye":
            print("se cierra la conexion")
            break



hiloR = threading.Thread(target=recibirMensaje, args=(s,))
hiloR.start()

hiloE = threading.Thread(target=enviarMensaje, args=(s,datos))
hiloE.daemon = True
hiloE.start() 

hiloR.join()


s.close()
    






