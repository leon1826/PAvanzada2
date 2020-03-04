import socket

# import errno

# import sys


HEADER_LENGTH = 10

IP = "127.0.0.1"

PORT = 1234

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((IP, PORT))

client_socket.setblocking(True)

op = 'y'

while op == "y":
    print("Digite los siguientes datos por favor")

    idCliente = input("Cedula: ")

    nombre = input("Nombre: ")

    paisOrigen = input("Pais de origen: ")

    paisDestino = input("Pais de destino: ")

    horaVuelo = input("Hora de vuelo: ")

    fecha = input("Fecha deseada DD/MM/AAAA: ")

    aerolinea = input("Nombre de la aerolinea: ")

    costo = input("Costo del vuelo: ")

    mensaje = (idCliente + "," + nombre + "," + paisOrigen + "," + paisDestino + "," + horaVuelo

               + "," + fecha + "," + aerolinea + "," + costo).encode('utf-8')

    client_socket.send(mensaje)

    op = input("Desea registrar otro vuelo? y/n: ")

# encabezado = f"{len(id_cliente):< {HEADER_LENGTH}}".encode('utf_8')

# print(id_cliente," ",encabezado)


'''

while True:

    #mensaje = input(f"{nombre_u}")

    #if mensaje:

    #    mensaje=mensaje.encode("utf-8")

    #    lon_mensaje=f"{len(mensaje):< {HEADER_LENGTH}}".encode("utf_8")

    #    client_socket.send(lon_mensaje+mensaje)

    try:

        while True:

            encabezado = client_socket.recv(HEADER_LENGTH)

            if not len(encabezado):

                print("conexion cerrada por el servidor")

                sys.exit()

            longitud = int(encabezado.decode("utf-8").strip())

            id_cliente = client_socket.recv(longitud).decode("utf-8")

            m_encabezado = client_socket.recv(HEADER_LENGTH)

            m_longitud=int(m_encabezado.decode("utf-8").strip())

    except IOError as e:

        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:

            print("error leyendo")

            sys.exit()

        continue

    except Exception as e:

        print("error general", str(e))

        sys.exit()

'''