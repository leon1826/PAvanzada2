import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
def buscarEstudiante(cod):
    mydb = mysql.connector.connect(host="localhost", user="root", password="96122609380", database="BaseEstudiantes")
    micursor = mydb.cursor()
    comando = "SELECT * FROM estudiantes WHERE codigo=%s"
    micursor.execute(comando, (cod,))
    resultado = micursor.fetchone()
    if resultado == None:
        print("No hay ningun estudiante con ese codigo")
        micursor.close()
        mydb.close()
        return False
    if resultado != None:
        print(resultado)
        return True

def buscarEstudianteNombre(nombre):
    mydb = mysql.connector.connect(host="localhost", user="root", password="96122609380", database="BaseEstudiantes")
    micursor = mydb.cursor()
    comando = "SELECT * FROM estudiantes WHERE nombre=%s"
    nom = input("Digite el nombre completo del estudiante: ")
    micursor.execute(comando, (nom,))
    resultado = micursor.fetchone()
    if resultado == None:
        print("No hay ningun estudiante con ese nombre")
    if resultado != None:
        print(resultado)
    micursor.close()
    mydb.close()

op = 0
while op != 8:
    print("1. Crear base de datos")
    print("2. Crear tabla")
    print("3. Insertar un estudiante")
    print("4. Ver tabla")
    print("5. Ver un solo estudiante")
    print("6. Actualizar datos estudiante")
    print("7. Eliminar un estudiante")
    print("8. Salir")
    print()

    op = int(input("Digite opcion: "))
    if op == 1:
        print("Insertar")
        mydb = mysql.connector.connect(host="localhost", user="root", password="96122609380")
        micursor = mydb.cursor()
        micursor.execute("SHOW DATABASES")
        for nom in micursor:
            print(nom)
            if nom=="baseestudiantes":
                print("La base de datos ya existe")
        micursor.close()
        mydb.close()
        print("base de datos ya creada")
    if op == 2:
        print("Crear tabla")
        mydb = mysql.connector.connect(host="localhost", user="root", password="96122609380", database="BaseEstudiantes")
        micursor = mydb.cursor()
        micursor.execute("CREATE TABLE estudiantes(codigo VARCHAR(20) NOT NULL PRIMARY KEY, nombre VARCHAR(20) NOT NULL, nota1 DOUBLE, nota2 DOUBLE, nota3 DOUBLE)")
        micursor.execute("SHOW TABLES")
        for nom in micursor:
            print(nom)
        micursor.close()
        mydb.close()
        print("Tabla creada")

    if op == 3:
        mydb = mysql.connector.connect(host="localhost", user="root", password="96122609380", database="BaseEstudiantes")
        micursor = mydb.cursor()
        cod = input("Digite el codigo del estudiante: ")
        comando = "SELECT * FROM estudiantes WHERE codigo=%s"
        micursor.execute(comando, (cod,))
        micursor.fetchone()
        if micursor.rowcount > 0:
            print("Ya existe el estudiante " + str(cod))
            micursor.close()
            mydb.close()
        else:
            nom = input("Digite el nombre del estudiante: ")
            nota1 = float(input("Digite la nota 1 del estudiante: "))
            nota2 = float(input("Digite la nota 2 del estudiante: "))
            nota3 = float(input("Digite la nota 3 del estudiante: "))
            comando2 = "INSERT INTO estudiantes(codigo, nombre, nota1, nota2, nota3) VALUES(%s, %s, %s, %s, %s)"
            micursor.execute(comando2, (cod, nom, nota1, nota2, nota3))
            mydb.commit()
            micursor.close()
            mydb.close()
            print("El estudiante ha sido ingresado exitosamente")

    if op == 4:
        mydb = mysql.connector.connect(host="localhost", user="root", password="96122609380", database="BaseEstudiantes")
        try:
            comando3="SELECT * FROM estudiantes"
            micursor = mydb.cursor()
            micursor.execute(comando3)
            registros = micursor.fetchall()
            promedio=0
            print("{:20s} {:30s} {:10s} {:10s} {:10s} {:10s}".format("Codigo","Nombre","Nota 1", "Nota 2", "Nota 3","Promedio"))
            for fila in registros:
                print("{:20s} {:30s} {:10f} {:10f} {:10f} {:10f}".format(fila[0],fila[1],fila[2], fila[3], fila[4], (fila[2]+fila[3]+fila[4])/3))
                promedio=promedio+((fila[2]+fila[3]+fila[4])/3)
            print("Promedio del curso")
            print(str(promedio/micursor._rowcount))

            micursor.close()
            mydb.close()
        except Error as e:
            print("error")
    if op == 5:
        mydb = mysql.connector.connect(host="localhost", user="root", password="96122609380",
                                       database="BaseEstudiantes")
        try:
            micursor = mydb.cursor()
            opcionb=0
            while opcionb != 3:
                print("De que manera desea buscar el estudiante ")
                print("1. Por codigo")
                print("2. Por Nombre")
                print("3. No buscar mas ")
                opcionb=int(input("su opcion"))
                if opcionb==1:
                    cod = input("Digite el codigo del estudiante: ")
                    buscarEstudiante(cod)
                if opcionb==2:
                    nom = input("Digite el nombre del estudiante: ")
                    buscarEstudianteNombre(nom)
        except Error as e:
            print("error")

    if op==6:
        print("Actualizar datos")
        mydb = mysql.connector.connect(host="localhost", user="root", password="96122609380",
                                       database="BaseEstudiantes")
        micursor = mydb.cursor()

        opcionb = 0
        while opcionb != 4:
            cod = input("Digite el codigo del estudiante: ")
            if buscarEstudiante(cod):
                print("Cual nota desea actualizar? ")
                print("1. Nota1")
                print("2. Nota2")
                print("3. Nota3")
                print("4. Salir")
                opcionb = int(input("Su opcion: "))
                if opcionb == 1:
                    auxNota = float(input("Digite la nota: "))
                    comando = "UPDATE estudiantes SET nota1=%s WHERE codigo=%s"
                    micursor.execute(comando, ( auxNota, cod))
                    mydb.commit()
                    print("Nota1 actualizada")
                if opcionb == 2:
                    auxNota = float(input("Digite la nota: "))
                    comando = "UPDATE estudiantes SET nota2=%s WHERE codigo=%s"
                    micursor.execute(comando, (auxNota, cod))
                    mydb.commit()
                    print("Nota2 actualizada")
                if opcionb == 3:
                    auxNota = float(input("Digite la nota: "))
                    comando = "UPDATE estudiantes SET nota3=%s WHERE codigo=%s"
                    micursor.execute(comando, (auxNota, cod))
                    mydb.commit()
                    print("Nota3 actualizada")
                opcionb=4
            micursor.close()
            mydb.close()

    if op==7:
        # print("Actualizar datos")
        mydb = mysql.connector.connect(host="localhost", user="root", password="96122609380",
                                       database="BaseEstudiantes")
        micursor = mydb.cursor()
        cod = input("Digite el codigo del estudiante a eliminar: ")
        if buscarEstudiante(cod):
            comando = "DELETE FROM estudiantes WHERE codigo=%s"
            micursor.execute(comando, (cod,))
            mydb.commit()
            print("Estudiante exitosamente eliminado")
            micursor.close()
            mydb.close()




