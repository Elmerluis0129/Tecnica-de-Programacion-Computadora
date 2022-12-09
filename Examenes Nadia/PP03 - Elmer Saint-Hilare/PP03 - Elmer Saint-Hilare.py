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

ListaClientes = []

def MenuPrincipal():
    print(
"""
  Menú Principal
*----------------*
|1.| Clientes
|2.| Video Juegos
|3.| Ventas
*----------------*
""")
MenuPrincipal()

def Menus():
        print(
"""
   Menú CRUD
*--------------*
|1.| Listar /Hecho Clientes
|2.| Crear /Hecho Clientes
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

        def elegirOpcionEnMenu(x, y):
            while True:
                try:
                    if x == 1 and y == 1: # CONFIGURACION MENU 1 EN CLIENTES
                        eleccionCRUD = int(input("¿Qué desea hacer?\n> "))
                        if eleccionCRUD == 0:
                            print(f"Lo siento, el '{eleccionCRUD}' no se encuentra en el menú. \n")

                        elif eleccionCRUD >= 1 and eleccionCRUD <= 5:
                            if eleccionCRUD == 1:
                                contador1 = 0
                                contador2 = 0
                                contador3 = 0
                                contador4 = 1
                                prueba = 1
                                while True:
                                    contador1 += 3
                                    contador2 += 4
                                    
                                    if len(ListaClientes) == contador2:
                                        print(f"Se encontraron: {contador2-contador1} cliente/s.\n")
                                        for x in range((contador2-contador1)+1):
                                            if prueba:
                                                print("""       Cedula  |  Nombre   |  Apellido  |  Metodo de Pago""")
                                                prueba = 0
                                            else:
                                                print("*---*------------------------------------------------------------*")
                                                print(f"|{contador4}.-|",ListaClientes[contador3], ListaClientes[contador3+1], ListaClientes[contador3+2], ListaClientes[contador3+3])
                                                contador3 += 4
                                                contador4 += 1
                                        print("*---*------------------------------------------------------------*")
                                        break
                                        
                            elif eleccionCRUD == 2:
                                contador = 0
                                while True:
                                    try:
                                        CantidadClientes = int(input("Cantidad de clientes a ingresar: \n> "))
                                        break
                                    except ValueError:
                                        print("No aceptamos data basuta.")
                                        continue
                                while True:
                                    try:
                                        while CantidadClientes != contador:
                                            cedula = int(input("Ingrese su identificación personal (ID): \n>"))
                                            cedulaModificada = str(cedula)
                                            nombre = input("Ingrese su/s nombre/s:")
                                            apellido = input("Ingrese su/s apellido/s:")
                                            print("\n'1' para pagar con tarjeta de crédito o débito. '2' para pagar en efectivo.")
                                            metodoPago = input("Ingrese su método de pago:")
                                            if metodoPago == "1":
                                                clientes = Cls.Clientes(cedulaModificada, nombre, apellido, "Tarjeta de crédito o débito")
                                            elif metodoPago == "2":
                                                clientes = Cls.Clientes(cedulaModificada, nombre, apellido, "Efectivo")
                                            ListaClientes.append(clientes.cedula_clientes)
                                            ListaClientes.append(clientes.nombre_clientes)
                                            ListaClientes.append(clientes.apellido_clientes)
                                            ListaClientes.append(clientes.metodoPago_clientes)
                                            
                                            contador += 1
                                        break
                                    except ValueError:
                                        print("Lo siento, no aceptamos data basura.\n")
                                        continue
                                        
                                    
                            elif eleccionCRUD == 3:
                                pass
                            elif eleccionCRUD == 4:
                                pass
                            else:
                                pass
                            
                        else:
                            print(f"Lo siento, el '{eleccionCRUD}' no se encuentra en el menú. \n")
                            continue
                        
                    elif x == 1 and y == 2: # CONFIGURACION MENU 1 EN VIDEO JUEGOS
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
                        
                    elif x == 1 and y == 3: # CONFIGURACION MENU 1 EN VENTAS
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
                            
                        
                    elif x == 2 and y == 1: # CONFIGURACION MENU 2 EN CLIENTES
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
                        
                    elif x == 2 and y == 2: # CONFIGURACION MENU 2 EN VIDEO JUEGOS
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
                        
                    elif x == 2 and y == 3: # CONFIGURACION MENU 2 EN VENTAS
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
                    elegirMenu()
                except ValueError:
                    print("Lo siento, no aceptamos data basura.\n")
                    continue
                
        def elegirMenu():
            while True:
                try:
                    eleccionMenu = int(input("\n¿Qué menú desea utilizar? '1' para 'Menú CRUD' y '2' para 'Menú adicional' y '3' para mostrar el menú\n> "))
                    if eleccionMenu == 0:
                        print(f"Lo siento, el '{eleccionMenu}' no se encuentra dentro de las opciones (1 y 2). \n")

                    elif eleccionMenu == 1:
                        print("Haz seleccionado el menú CRUD...")
                        elegirOpcionEnMenu(1, eleccionPrincipal)

                    elif eleccionMenu == 2:
                        print("Haz seleccionado el menú adicional...")
                        elegirOpcionEnMenu(2, eleccionPrincipal)
                    
                    elif eleccionMenu == 3:
                        Menus()

                    else:
                        print(f"Lo siento, el '{eleccionMenu}' no se encuentra dentro de las opciones (1 y 2). \n")
                        continue
                    break
                except ValueError:
                    print("Lo siento, no aceptamos data basura.\n")
                    continue
                
        elegirMenu()

while True:
    try:
        eleccionPrincipal = int(input("¿Qué desea hacer?\n> "))
        if eleccionPrincipal == 0:
            print(f"Lo siento, el '{eleccionPrincipal}' no se encuentra en el menú. \n")
        elif eleccionPrincipal >= 1 and eleccionPrincipal <= 3:
            if eleccionPrincipal == 1:
                print("Haz seleccionado 'Clientes'...")
                Menus()
            elif eleccionPrincipal == 2:
                print("Haz seleccionado 'Video Juegos'...")
                Menus()
            else:
                print("Haz seleccionado 'Ventas'...")
                Menus()
            break
        else:
            print(f"Lo siento, el '{eleccionPrincipal}' no se encuentra en el menú. \n")
            continue

    except ValueError:
        print("Lo siento, no aceptamos data basura.\n")
        continue
    
