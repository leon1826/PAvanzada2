import tkinter as tk
from tkinter import *
import mysql.connector
from mysql.connector import Error

def cerrar():
    marco.destroy()
def crearbase():
    mydb = mysql.connector.connect(host="localhost", user="root", password="96122609380")
    micursor = mydb.cursor()
    micursor.execute("SHOW DATABASES")
    for nom in micursor:
        print(nom)
        if "baseestudiantes" in nom:
            text.insert(INSERT, "La base de datos ya esta creada")
    micursor.close()
    mydb.close()
    print("base de datos ya creada")

def creartabla():
    pass
marco=tk.Tk()
marco.title("Base de Datos")
marco.geometry('700x500')
marco.configure(background='#A1A8D8')
botonCbase = tk.Button(marco,text="Crear base de datos", command = crearbase)
botonCbase.place(x=10,y=20)
botonCbase.config(font=("Consolas", 12), pady=5)
boton = tk.Button(marco,text="Crear Tablas", command = creartabla)
boton.place(x=10,y=80)
boton.config(font=("Consolas", 12), pady=5)
botonrstudent = tk.Button(marco,text="Registrar Estudiante", command = None)
botonrstudent.place(x=10,y=140)
botonrstudent.config(font=("Consolas", 12), pady=5)
botonlc = tk.Button(marco,text="Listar curso", command = None)
botonlc.place(x=10,y=200)
botonlc.config(font=("Consolas", 12), pady=5)
botonfs = tk.Button(marco,text="Buscar Estudiante", command = None)
botonfs.place(x=10,y=260)
botonfs.config(font=("Consolas", 12), pady=5)
botonrd = tk.Button(marco,text="Actualizar datos", command = None)
botonrd.place(x=10,y=320)
botonrd.config(font=("Consolas", 12), pady=5)
botonds = tk.Button(marco,text="Eliminar Estudiante", command = None)
botonds.place(x=10,y=380)
botonds.config(font=("Consolas", 12), pady=5)
b_cerrar = tk.Button(marco, text='Cerrar', command=cerrar)
b_cerrar.place(x=10,y=440)
b_cerrar.config(font=("Consolas", 12), pady=5)
text = Text(marco, height=26, width=30)
#scroll = Scrollbar(marco, command=text.yview)
#text.configure(yscrollcommand=scroll.set)
text.tag_configure('bold_italics',font=('Verdana', 12, 'bold', 'italic'))

text.place(x=400,y=25)
#scroll.pack(side=RIGHT, fill=Y)


marco.mainloop()



