import select
import socket
from tkinter import messagebox

import mysql.connector
from mysql.connector import Error

def crearBase():
    nombre = 'Clientes_vuelos'
    mydb = mysql.connector.connect(host="localhost", user="root", password="96122609380")
    micursor = mydb.cursor()
    comando = "SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = %s"
    micursor.execute(comando, (nombre,))
    # print(micursor.fetchone())
    resultado = micursor.fetchone()
    if resultado == None:
        comando = "create database " + nombre
        micursor.execute(comando)
        print("Base Creada", "Base creada exitosamente con el nombre: " + nombre)
    micursor.close()
    mydb.close()

def crearTablas():
    tabla = 'Clientes'
    mydb = mysql.connector.connect(host="localhost", user="root", password="96122609380", database='Clientes_vuelos')
    micursor = mydb.cursor()
    micursor.execute(
        "CREATE TABLE IF NOT EXISTS " + tabla + "(cedula VARCHAR(20) NOT NULL PRIMARY KEY, nombre VARCHAR(20) NOT NULL, "
                                                " origen VARCHAR(20) NOT NULL, destino VARCHAR(20) NOT NULL, "
                                                "fecha VARCHAR(20) NOT NULL, hora VARCHAR(20) NOT NULL, aerolinea VARCHAR(20) NOT NULL"
                                                ", costo VARCHAR(20) NOT NULL)")
    micursor.close()
    mydb.close()

def registrarCliente(datos_cliente):
    mydb = mysql.connector.connect(host="localhost", user="root", password="96122609380", database='Clientes_vuelos')
    micursor = mydb.cursor()
    print("paso")
    cedula = datos_cliente[0]
    comando = "SELECT * FROM Clientes WHERE cedula=%s"
    micursor.execute(comando, (cedula,))
    micursor.fetchone()
    if micursor.rowcount > 0:
        micursor.close()
        mydb.close()
    else:
        print("paso2")
        cedula = datos_cliente[0]
        nom = datos_cliente[1]
        print("paso3")
        origen = datos_cliente[2]
        destino = datos_cliente[3]
        fecha = datos_cliente[4]
        hora =datos_cliente[5]
        aerolinea =datos_cliente[6]
        costo = datos_cliente[7]
        comando2 = "INSERT INTO Clientes(cedula, nombre, origen, destino, fecha, hora,aerolinea, costo ) VALUES(%s, %s, %s, %s, %s , %s, %s, %s)"
        micursor.execute(comando2, (cedula, nom, origen, destino,fecha,hora,aerolinea, costo))
        mydb.commit()
        micursor.close()
        mydb.close()


IP = '127.0.0.1'
PORT = 1234


print("creando")
crearBase()
crearTablas()
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((IP,PORT))
server_socket.listen()
lista_sockets = [server_socket]
outputs = []
clients = {}

while True:
    read_sockets, writable, exception_sockets = select.select(lista_sockets, outputs, lista_sockets)
    for notified_socket in read_sockets:
        if notified_socket == server_socket:
            client_socket, client_address = server_socket.accept()
            lista_sockets.append(client_socket)
            # clients[client_socket] = user
        else:
            data = notified_socket.recv(1024)
            if data:
                # A readable client socket has data
                print(data.decode())
                datos_cliente = list()
                cadena = data.decode()
                datos_cliente = cadena.split(",")
                print(datos_cliente)
                registrarCliente(datos_cliente)
                # Add output channel for response
            else:
                # Interpret empty result as closed connection
                print('closing')
                # Stop listening for input on the connection
                if notified_socket in outputs:
                    outputs.remove(notified_socket)
                lista_sockets.remove(notified_socket)
                notified_socket.close()
    # data = conn.recv(1024)
    # if not data:
    #     break

