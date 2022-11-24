from tkinter import *

#Para abrir la ventana directamente, guardar este archivo con la extensión .pyw

raiz = Tk() #Creamos la ventana
raiz.title("My first window") #Ponemos título
raiz.geometry("300x200") #Especificamos el tamaño de la ventana
raiz.resizable(0,0) #Sirve para que no se puede modificar el tamaño de la ventana, en el caso de estar False (0)
raiz.iconbitmap("Programación.ico") #Aquí le ponemos imagén a nuestra ventana
raiz.config(bg = "Blue") #Aquí le damos el color azúl a nuestra ventana

raiz.mainloop() #Sirve para que no se cierre la ventana sola

