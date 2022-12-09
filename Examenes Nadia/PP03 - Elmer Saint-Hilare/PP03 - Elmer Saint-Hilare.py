"""
Examen Final - Sistema PowerGames
Valor: 100ptos.

Mediante el uso de Programación Orientada a Objetos, desarrollar un pequeño sistema que permita el mantenimiento de las ventas de videojuegos de PowerGames.

Indicaciones:

El sistema debe tener un menú de opciones que permita la interacción con el mismo.
El sistema debe realizar las 4 operaciones de un CRUD (Create, Read, Update, Delete) para las siguientes clases (modelos):
Clientes.
Videojuegos.
Ventas.
El sistema debe permitir la carga y la exportación de data a través de archivos .csv (para todos los modelos).
El sistema debe tener una opción que permita generar un archivo .csv con los videojuegos cuyas ventas sean mayores a RD$500.00.
Se deben controlar las excepciones (data basura) haciendo uso de try-except.

Elmer Saint-Hilare 21-1354
"""

import PP03_Clientes as Cls
import PP03_Ventas as Vns
import PP03_VideoJuegos as VJs

j = 5

def MenuPrincipal():
    print(
"""
   Menú CRUD
*--------------*
|1.| Listar
|2.| Crear
|3.| Leer
|4.| Actualizar
|5.| Eliminar
*--------------*

       Menú adicional
*---------------------------*
|1.-| Carga-Exportacion CSV
|2.-| Videojuegos Ventas CSV 
*---------------------------*
""")
MenuPrincipal()

def elegirOpcionEnMenu(x):
    while True:
        try:
            if x == 1:
                eleccionCRUD = int(input("¿Qué desea hacer?\n> "))
                if eleccionCRUD == 0:
                    print(f"Lo siento, el '{eleccionCRUD}' no se encuentra en el menú. \n")

                elif eleccionCRUD >= 1 and eleccionCRUD <= 5:
                    if eleccionCRUD == 1:
                        pass
                    elif eleccionCRUD == 2:
                        pass
                    elif eleccionCRUD == 3:
                        pass
                    elif eleccionCRUD == 4:
                        pass
                    else:
                        pass
                    break
                else:
                    print(f"Lo siento, el '{eleccionCRUD}' no se encuentra en el menú. \n")
                    continue
                
            elif x == 2:
                eleccionAdicional = int(input("¿Qué desea hacer?\n> "))
                if eleccionAdicional == 0:
                    print(f"Lo siento, el '{eleccionAdicional}' no se encuentra en el menú. \n")

                elif eleccionAdicional >= 1 and eleccionAdicional <= 2:
                    if eleccionAdicional == 1:
                        pass
                    else:
                        pass
                    break
                else:
                    print(f"Lo siento, el '{eleccionAdicional}' no se encuentra en el menú. \n")
                    continue
                
        except ValueError:
            print("Lo siento, no aceptamos data basura.\n")
            continue
        
def elegirMenu():
    while True:
        try:
            eleccionMenu = int(input("¿Qué menú desea utilizar? '1' para 'Menú CRUD' y '2' para 'Menú adicional'\n> "))
            if eleccionMenu == 0:
                print(f"Lo siento, el '{eleccionMenu}' no se encuentra dentro de las opciones (1 y 2). \n")

            elif eleccionMenu == 1:
                print("Haz seleccionado el menú CRUD...")
                elegirOpcionEnMenu(1)
                
            elif eleccionMenu == 2:
                print("Haz seleccionado el menú adicional...")
                elegirOpcionEnMenu(2)
                
            else:
                print(f"Lo siento, el '{eleccionMenu}' no se encuentra dentro de las opciones (1 y 2). \n")
                continue
            break
        except ValueError:
            print("Lo siento, no aceptamos data basura.\n")
            continue
        
elegirMenu()
#TODO escuchar la nota de voz de nadia, para saber cual es el proximo paso.