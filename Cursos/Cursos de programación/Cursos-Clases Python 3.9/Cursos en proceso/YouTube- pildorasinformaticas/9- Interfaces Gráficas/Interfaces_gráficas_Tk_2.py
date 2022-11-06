from tkinter import *

#Para abrir la ventana directamente, guardar este archivo con la extensión .pyw

raiz = Tk()
raiz.title("My window with Frame")
#raiz.geometry("500x400")
#raiz.resizable(0,0)
raiz.iconbitmap("Programación.ico")
raiz.config(bg = "Cyan")
raiz.config(bd = "100") #Tamaño de borde
raiz.config(relief = "sunken") #Tipo de borde
raiz.config(cursor = "hand2") #Tipo de cursor

#Creamos el frame
miFrame = Frame() 
"""
.pack(#Aquí van todas las modificaciones del frame)

Documentation:
Empaquetamos el frame, y el frame se puede colocar en la parte de arriba, abajo, izquierda y derecha, 
para ponerlo arriba sería side="top",para ponerlo abajo sería side="bottom" en la derecha se pone side="right", y para izquierda 
side="left". Para ponerlo en dos lados al mismo tiempo, osea en las esquinas se le tiene que poner otro parametro que sería anchor, 
este recibe como parametros las iniciales de los puntos cardinales, n, s, w, e, también ne, se, sw y nw
Ejemplo: miFrame.pack(side = "left", anchor = "n")

Con fill recibe parametros como x, y, both, con x se ajusta horizontalmente, con y verticalmente, pero para esto, 
necesita usar otro que es expand = "True".
Ejemplo: miFrame.pack(fill = "y", expand = "True")
con both, se expande tanto para el vertical como para el horizontal, pero, tiene que tener también True el expand.
Ejemplo: miFrame.pack(fill = "both", expand = "True")
"""
miFrame.pack()
"""
Aqui le damos color y tamaño al frame con bg es el color, con width la anchura de la 
ventana y con height la altura de la misma.
ejemplo: miFrame.config(bg = "Red", width = "450", height = "350")
"""
miFrame.config(bg = "Red", width = "450", height = "350") 
"""
Aquí le agregamos borde a la ventana, en nuestro caso es con relief y recive como parametro flat, groove, raised, ridge, solid, o sunken
y con bd, le damos tamaño al borde del 1 al 1000 y con el cursor, lo cambia a otro tipo, en este caso con hand2, lo convierte en una mano
también está, pirate, que lo convierte en una calavera
"""
miFrame.config(bd = "50") #Tamaño de borde
miFrame.config(relief = "groove")#Tipo de borde
miFrame.config(cursor = "pirate")#Tipo de cursor


raiz.mainloop()