# Echo server program
import socket
import time
import threading

HOST = 'localhost'                 # Symbolic name meaning all available interfaces
PORT = 50007             # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))  # Hacemos el link estre el socket y el host
s.listen(1)  # Escuchamos 1 connexion
conn, addr = s.accept()  # aceptamos la conexion
text = ""

# recibimos el mesaje


def recibirMensaje(conn):
    while True:
        #print("el cliente dice: ")
        data = conn.recv(1024)
        print data
        if data == "bye":
            print("se cierra la conexion")
            conn.sendall(data)
            break


def enviarMensaje(conn, text):
    while True:
        #print("el server envia: ")
        text = raw_input()
        if text:
            conn.sendall(text)
        if text == "bye":
            print("se cierra la conexion")
            break

  





hiloR = threading.Thread(target=recibirMensaje, args=(conn,))
hiloR.start()

hiloE = threading.Thread(target=enviarMensaje, args=(conn, text))
hiloE.daemon = True
hiloE.start()

hiloR.join()


s.close()

