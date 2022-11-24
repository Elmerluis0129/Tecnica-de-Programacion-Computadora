from tkinter import * #Importamos todo lo concerniente a la librería de tkinter
import time #Importamos todo lo concerniente a la librería de time


"""
Aquí creamos la interfaz gráfica.
Le ponemos título.
Le ponemos tamaño.
"""
root=Tk()
root.title("My first window")
root.geometry("500x300")

"""
Aquí creamos el primer boton.
Lo almacenamos en root.
Le damos el comando a ejecutar.
Con bg, le damos el color al boton.
"""
Boton1 = Button(root, text="Minimizar", command=root.iconify, bg="yellow")
Boton1.pack(side=LEFT)

"""
Aquí simplemente creamos una función para hacer una etiqueta y usarlo como comando en el boton 2.
"""
def imprimir():
    label1 = Label(root, text="Imprimiendo...")
    label1.pack()

"""
Aquí creamos el segundo boton.
Lo almacenamos en root.
Le damos el comando a ejecutar.
Con bg, le damos el color al boton.
"""
Boton2 = Button(root, text="Imprimir", command=imprimir, bg="red") 
Boton2.pack(side=RIGHT)

"""
Aquí es  para que la interfaz gráfica no se cierre, hasta, que el usuario lo inidique presionando la "x"
"""
root.mainloop()