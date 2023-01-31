import tkinter as tk
from tkinter import ttk

root = tk.Tk()

def Seleccionar(Opcion):
    print(Opcion)

#Segunda manera de crear botones en las interfaces gráficas...

ttk.Button(root, text="Python", command = lambda: Seleccionar("Python")).pack()
ttk.Button(root, text="Java", command = lambda: Seleccionar("Java")).pack()
ttk.Button(root, text="JavaScript", command = lambda: Seleccionar("JavaScript")).pack()

root.mainloop()
