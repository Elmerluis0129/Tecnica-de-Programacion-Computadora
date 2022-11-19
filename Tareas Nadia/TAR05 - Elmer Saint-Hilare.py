"""
Escriba un programa que pregunte al usuario los números de su ticket de lotería, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor. 
Elmer Saint-Hilare 21-1354
"""
from emoji import emojize as em # Esto no es parte del ejercicio, es decoración.

# ==== Importando time ==== #
"""
Aquí lo importo para usar la función sleep y poder controlar la velocidad de iteración del bucle for.
"""
import time
# ==== Fin Importando time ==== #

# ================ Barra de porcentaje ================ #
"""
Aquí declaro mi limite una función, que es la que se encarga de hacer los cálculos de la barra.
Con el for es para darle formato a la barra de carga, de tal manera que vaya haciendolo con un tiempo de 0,7 por iteración.
"""
limite = 50

def barraProgreso(segmento, total, longitud):
    porcentaje = segmento / total
    completado = int(porcentaje * longitud)
    restante = longitud - completado
    barra = f"[{'+' * completado}{'-' * restante}{porcentaje:.2%}]"
    return barra

input("\nPresione Enter para iniciar el programa... \n")
print("\nCargando... Por favor espere.")
for i in range(limite+1):
    time.sleep(0.03)
    print(barraProgreso(i, limite, 50), end = "\r")
    
print("\n")
    
# ============== Fin Barra de porcentaje ============== #

def programa5 ():
    #Nombre del programa.
    print("""
*-----------------------------------------------*
|Ordenar de menor a mayor los números de lotería|
*-----------------------------------------------*
""")#Decorando el nombre de la aplicación.

    ListaNumLot = []
    numeroAcumulador = 1
    
    while True: # DATA BASURA
        try: # Aquí le digo al programa que intente las líneas de códigos que están dentro de la misma.
            numeroTicket = int(input("Ingrese la cantidad de números de su ticket\n> "))
            break
        except ValueError: # Lo utilizo para que cuando me lance ese error, le muestre otro mas entendible y tenga la opcion de cambiarlo.
            print("\nLo siento, no se permite data basura.\nVuelva a intentarlo.\n")
            continue
    
    
    for i in range(1,numeroTicket+1):
        while True: # DATA BASURA
            try: # Aquí le digo al programa que intente las líneas de códigos que están dentro de la misma.
                print("Ingrese el número",numeroAcumulador,":")
                numerosDeTickets = int(input("> "))
                break
            except ValueError: # Lo utilizo para que cuando me lance ese error, le muestre otro mas entendible y tenga la opcion de cambiarlo.
                print("\nLo siento, no se permite data basura.\nVuelva a intentarlo.\n")
                continue
        
        numeroAcumulador += 1
        ListaNumLot.append(numerosDeTickets) 
    
    print("\nLista sin ordenar: ", ListaNumLot)#Lista normal sin ordenar.
    ListaNumLot.sort()#Función para ordenar la lista.
    print("Lista ordenada: ", ListaNumLot, ) #Lista ordenada.
    
    # ========================== Agradecimiento por usar el programa ========================= #  
    
    """
    Aquí imprimo por pantalla el agradecimiento y por quién fue creado, en este caso por mi.
    """
    
    print(em("""
*-----------------------------------------*
|  ¡Programa 5 Finalizado exitosamente! :smiling_face_with_smiling_eyes:|
*-----------------------------------------*
"""))
# ========================== Fin Agradecimiento por usar el programa ========================= #
programa5()