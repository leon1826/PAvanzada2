from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter as tk
import mysql.connector
from mysql.connector import Error


from tkinter import messagebox


def insertar(param,root):
    messagebox.showinfo("Confirmacion","Has seleccionado: "+param)
    print(param)


def mostrar(registros,root):
    lienzo = Canvas(root, width=650, height=400, background="#A9BCF5")
    lienzo.pack()
    lienzo.place(x=300, y=40)
    # top = Toplevel()
    # top.geometry("700x300")
    # top.resizable(width=None, height=None)
    text = Text(lienzo)
    text.config(font="Times",bg="lightblue",relief="groove",background="#A9BCF5")
    scroll = Scrollbar(lienzo, command=text.yview)
    # scroll1 = Scrollbar(lienzo, command=text.xview)
    text.pack(side=LEFT)
    scroll.pack(side=RIGHT, fill=Y)
    # scroll1.pack(side=BOTTOM, fill=Y)
    text.insert(END,
                 "{:10s} {:20s} {:10s} {:10s} {:10s} {:10s}".format("Cedula"," nombre", "origen", "destino", "fecha", "hora"))
    for fila in registros:
        text.insert(END,"\n")
        text.insert(END, "{:10s} {:20s} {:10s} {:10s} {:10s} {:10s} ".format(fila[0], fila[1], fila[2], fila[3], fila[4],fila[5]))

def consultar(param,busqueda, root):
    print(busqueda)
    if busqueda==""and param=="":
        messagebox.showinfo("INFO", "no ha digitado criterio de busqueda")
    else:
        print(param +" "+ busqueda)
        mydb = mysql.connector.connect(host="localhost", user="root", password="96122609380",
                                       database='Clientes_vuelos')
        micursor = mydb.cursor()
        cod = str(param)
        if busqueda=="Destino":
            comando = "SELECT * FROM Clientes WHERE destino=%s"
            micursor.execute(comando, (cod,))
            registros = micursor.fetchall()
            print(registros)
            mostrar(registros,root)
        elif busqueda=="Origen":
            comando = "SELECT * FROM Clientes WHERE destino=%s"
            micursor.execute(comando, (cod,))
            registros = micursor.fetchall()
            mostrar(registros, root)
        elif busqueda == "Aerolinea":
            comando = "SELECT * FROM Clientes WHERE aerolinea=%s"
            micursor.execute(comando, (cod,))
            registros = micursor.fetchall()
            mostrar(registros, root)
        elif busqueda == "Fecha":
            comando = "SELECT * FROM Clientes WHERE fecha=%s"
            micursor.execute(comando, (cod,))
            registros = micursor.fetchall()
            mostrar(registros, root)


def iniciar():
    root = Tk()
    root.geometry("1000x550")
    root.title("Consulta")

    root.config(bg="Blue")
    root.config(bd=20)

    lienzo = Canvas(root, width=650, height=420, background="#A9BCF5")
    lienzo.pack()
    lienzo.place(x=300, y=40)

    var = StringVar()
    lbl_var = Label(root, textvariable=var,relief="groove",bg="gray", font=("Times",20))
    var.set("CONSULTA DE BASE DE DATOS")
    lbl_var.pack()
    lbl_var.place(x=230, y=0)

    var = StringVar()
    lbl_buscar = Label(root, textvariable=var, relief="groove", bg="red",font=("Times",12))
    var.set("VARIABLE POR LA CUAL BUSCAR")
    lbl_buscar.pack()
    lbl_buscar.place(x=30, y=50)

    combo = ttk.Combobox()
    combo["values"]=["Origen","Destino", "Aerolinea","Fecha"]
    combo.place(x=50,y=80)


    entry_dato = Entry()
    entry_dato.pack()
    entry_dato.place(x=60, y=240)

    btn_selecccionar = Button(root, text=" Seleccionar ", command=lambda: insertar(str(combo.get()), root))
    btn_selecccionar.pack()
    btn_selecccionar.place(x=70, y=180)

    btn_consultar = Button(root, text=" Consultar ", command=lambda: consultar(str(entry_dato.get()),combo.get(), root))
    btn_consultar.pack()
    btn_consultar.place(x=90, y=300)

    root.mainloop()
iniciar()