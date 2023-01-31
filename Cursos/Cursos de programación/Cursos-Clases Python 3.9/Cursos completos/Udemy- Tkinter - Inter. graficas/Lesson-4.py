from tkinter import *


root = Tk()
root.title("Entrada") # Sirve para asignarle título a la ventana.
root.geometry("290x225") # Sirve para darle un tamaño predefinido a la ventana.
root.resizable(0,0) # Sirve para que no se le pueda modificar el tamaño de ninguna forma a la ventana.

nombre = StringVar()
apellido = StringVar()
saludo = StringVar()

def Saludar():
	saludo.set("Hola " + nombre.get() + " " + apellido.get())

etiqueta1 = Label(root, text = "Escribe aquí tu nombre: ", bd = 5, bg = "orange", font=("Curier 8"))
etiqueta1.place(x = 10, y = 10)
entrada1 = Entry(root, textvariable = nombre, bd = 5)
entrada1.place(x = 150, y = 10)

etiqueta2 = Label(root, text = "Escribe aquí tu apellido: ", bd = 5, bg = "green", font=("Curier 8"))
etiqueta2.place(x = 10, y = 40)
entrada2 = Entry(root, textvariable = apellido, bd = 5)
entrada2.place(x = 150, y = 40)

boton = Button(root, text = "Saludar aquí", command = Saludar, bd = 5, bg = "purple", font=("Curier 8"))
boton.place(x = 105, y = 110)

entrada3 = Entry(root, textvariable = saludo, state = "disable", bd = 10, font = ("Curier 9"))
entrada3.place(x = 70, y = 160)

root.mainloop()
