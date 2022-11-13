"""
Escriba una función que reciba 2 listas de productos (de forma dinámica), y retorne un conjunto (Set) de los productos comunes 
en las mismas. En caso de que no hayan productos comunes, retornar: "No hay productos comunes en las listas".

Elmer Saint-Hilare 21-1354
"""
from emoji import emojize as em # Esto no es parte del ejercicio, es decoración.

def programa11 ():
    print("""
*---------------------------------------*  
|Productos en comunes entre listas(sets)|
*---------------------------------------*
""")

    # ======== Variables generales (Listas) ========= #
    """
    Variables Generales.
    Aquí podemos apreciar las dos listas ya declaradas. Lista 1 y Lista 2.
    """
    Lista1 = []
    Lista2 = []
    # ======== Fin Variables generales (Listas) ========= #

    # ==================== Funciones ==================== #
    """
    Aquí es dónde tengo las funciones que me van preguntando los productos, la cantidad de los mismos.
    Aquí también agrego los productos a las listas correspondientes.

    El while es para que me lo ejecute las veces n necesarias.
    El for es para ir imprimiendo los productos de la listas.
    En la ultima funcion es donde identifico si hay o no productos comunes entre listas.

    En los acumuladores es para ir controlando el numero de producto, producto 1, 2, 3 etc y asi controlar todo con los numeros correspondientes.
    Los contadores son los que me van aumentando de 1 en 1 los acumuladores.
    """

    def ListaDeCompras(cantidadProducto):
        iteraccion = 1
        while True:
            # Acumuladores
            NumeroProducto = 1
            NumeroProducto2 = 1
            controlIteracion = 0
            PosicionLista = 0
            # ================ Lista 1 ================ #
            if iteraccion == 1:
                print("\n================== Lista Uno ==================\n")
                while cantidadProducto != controlIteracion:
                    print("""
*-----------------------*
|Ingrese el producto """+str(NumeroProducto2)+""":|
*-----------------------*""")
                    producto = input("> ")
                    controlProducto = producto.isdigit()
                    if controlProducto:
                        while True:
                            print("\nLo siento, no se permite data basura.\nVuelva a intentarlo.\n")
                            producto = input("> ")
                            controlProducto = producto.isdigit()
                            if not controlProducto:
                                Lista1.append(producto)
                                break
                    # Contadores
                    controlIteracion += 1
                    NumeroProducto2 += 1

                print("\nCantidad de producto lista 1: ", len(Lista1))
                for e in Lista1:
                    print("\nProducto",str(NumeroProducto)+":", Lista1[PosicionLista])
                    # Contadores
                    PosicionLista += 1
                    NumeroProducto += 1

                print("\nLista 1: ", Lista1)
                iteraccion = 2
                continue
            # ============== Fin Lista 1 ============== #
            
            # ================ Lista 2 ================ #
            elif iteraccion == 2: #Lista 2
                while True:
                    try: # Aquí le digo al programa que intente las líneas de códigos que están dentro de la misma.
                        cantidadProducto2 = int(input("\nIngrese la cantidad de producto lista 2: \n> "))
                        break
                    except ValueError: # Lo utilizo para que cuando me lance ese error, le muestre otro mas entendible y tenga la opcion de cambiarlo.
                        print("\nLo siento, no se permite data basura.\nVuelva a intentarlo.\n")
                        continue
                print("\n================== Lista Dos ==================\n")
                while cantidadProducto2 != controlIteracion:
                    print("""
*-----------------------*
|Ingrese el producto """+str(NumeroProducto2)+""":|
*-----------------------*""")
                    producto2 = input("> ")
                    controlProducto2 = producto2.isdigit()
                    if controlProducto2:
                        while True:
                            print("\nLo siento, no se permite data basura.\nVuelva a intentarlo.\n")
                            producto2 = input("> ")
                            controlProducto2 = producto2.isdigit()
                            if not controlProducto2:
                                Lista2.append(producto2)
                                break
                    # Contadores
                    controlIteracion += 1
                    NumeroProducto2 += 1

                print("\nCantidad de producto lista 2: ", len(Lista2))
                for e in Lista2:
                    print("\nProducto",str(NumeroProducto)+":", Lista2[PosicionLista])
                    # Contadores
                    PosicionLista += 1
                    NumeroProducto += 1

                print("\nLista 2: ", Lista2)

                iteraccion = 3
                continue
            # ============== Fin Lista 2 ============== #
            
            # ================ Set listas ================ #
            elif iteraccion == 3:
                convirtiendo1 = set(Lista1)
                convirtiendo2 = set(Lista2)
                l = convirtiendo1.intersection(convirtiendo2)
                if len(l) >= 1:
                    print("\n========= Producto comunes en ambas listas =========")
                    print("\nProducto comunes: ", l)
                
                else:
                    print("\nNo hay productos comunes en las listas.")
                iteraccion = "Fin"
                continue
            # ============== Fin Set Listas ============== #
            elif iteraccion == "Fin": break

    # ==================== Fin Funciones ==================== #

    # ==================== Llamada Función ==================== #
    """
    Aquí llamo la función para que lleven acabo dichos códigos que tienen dentro.
    """
    while True:
        try: # Aquí le digo al programa que intente las líneas de códigos que están dentro de la misma.
            CantidadProducto = int(input("\nIngrese la cantidad de producto lista 1: \n> "))
            break
        except ValueError: # Lo utilizo para que cuando me lance ese error, le muestre otro mas entendible y tenga la opcion de cambiarlo.
            print("\nLo siento, no se permite data basura.\nVuelva a intentarlo.\n")
            continue

    ListaDeCompras(CantidadProducto)
    # ================== Fin Llamada Función ================== #

    # ========================== Agradecimiento por usar el programa ========================= #  

    """
    Aquí imprimo por pantalla el agradecimiento y por quién fue creado, en este caso por mi.
    """

    print(em("""
*------------------------------------------*
|  ¡Programa 11 Finalizado exitosamente! :smiling_face_with_smiling_eyes:|
*------------------------------------------*
"""))
    # ========================== Fin Agradecimiento por usar el programa ========================= #
programa11()