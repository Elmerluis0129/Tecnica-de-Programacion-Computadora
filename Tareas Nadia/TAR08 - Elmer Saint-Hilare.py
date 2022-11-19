"""
Escriba un programa que, mediante una función, retorne las tablas de multiplicar del n al m.
Ejemplo:
Ingrese el número por el que comenzarán a mostrarse las tablas: 1.
Ingrese el número por el que terminarán a mostrarse las tablas: 3.
Elmer Saint-Hilare 21-1354.
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

def programa8 ():
    # ========================== Nombre programa ========================= # 
    """
    Aquí es para imprimir el nombre del programa.
    """
    print("""
*--------------------*  
|Tabla de multiplicar|
*--------------------*
\n""")
# ========================== Fin Nombre programa ========================= #

# ========================== Inicio/Final ========================= #  

    """
    Aquí declaro mis variables inicio y fin, a las cuales le doy de valor una entrada que el usuario procederá a darme.
    Y un salto de línea para que no salga pegado.
    
    Aquí en el while tengo un control para saber si pone el iniciar las tablas igual al final o si el iniciar es mayor a final, para que solo haga las tablas cuando es posible
    Es posible cuando inicio es menor que el final o no es igual al final.
    """
    
    while True:
        try: # Aquí le digo al programa que intente las líneas de códigos que están dentro de la misma.
            Inicio = int(input("Escribe un número para comenzar la tabla: "))
            Final = int(input("Escribe un número para terminar la tabla: ")) 
            print("\n")
            break
        except ValueError: # Lo utilizo para que cuando me lance ese error, le muestre otro mas entendible y tenga la opcion de cambiarlo.
            print("\nLo siento, no se permite data basura.\nVuelva a intentarlo.\n")
            continue

    
    while True:
        if Inicio > Final:
            while True:
                print("\nLo siento, el inicio no puede ser mayor a final.")
                while True:
                    try: # Aquí le digo al programa que intente las líneas de códigos que están dentro de la misma.
                        Final = int(input("\nEscribe un número para terminar la tabla: ")) 
                        break
                    except ValueError: # Lo utilizo para que cuando me lance ese error, le muestre otro mas entendible y tenga la opcion de cambiarlo.
                        print("\nLo siento, no se permite data basura.\nVuelva a intentarlo.\n")
                        continue

                if Inicio <= Final:
                    break
            continue
                
        elif Inicio == Final:
            while True:
                print("\nLo siento, el inicio no puede ser igual a Final.")
                while True:
                    try: # Aquí le digo al programa que intente las líneas de códigos que están dentro de la misma.
                        Inicio = int(input("\nEscribe un número para comenzar la tabla: "))
                        break
                    except ValueError: # Lo utilizo para que cuando me lance ese error, le muestre otro mas entendible y tenga la opcion de cambiarlo.
                        print("\nLo siento, no se permite data basura.\nVuelva a intentarlo.\n")
                        continue
                if Inicio != Final:
                    break
            continue
        else:
            break
        
# ========================== Fin Inicio/Final ========================= # 

# ========================== Funciones ========================= #

    """
    En las funciones las utilizo para reutilizar la lógica n veces sin necesidad de repetir las líneas de códigos n veces.
    Aquí consta de 3 funciones: 
    -La primera (Inicio) se encarga de realizar la tabla del número que le indique el usuario como inicio.
    -La segunda (Desarrollo) se encarga de realizar las tablas que quedan de por medio de la tabla inicio y fin.
    -La tercera (Final) se encarga de realizar la tabla del número que le indique el usuario como fin.

    Aquí también le agrego lo que son los marcadores de inicio de la tabla y final de la tabla.
    """

    # ----- Función Inicio ----- #
    def multiplicar (Inicio):
        print("""
*--------------*
|Tabla del:""", Inicio, """ | 
*--------------*
""")
        for numero in range(0, 11):
            operacion = Inicio * numero
            print(Inicio, "*", numero ,"=", operacion)

        print("""
*------------------*
|Fin tabla del:""", Inicio, """ | 
*------------------*
""")
# ----- Fin Función Inicio ----- #

# ----- Función Desarrollo ----- #         
    def multiplicar3 (SumaIniAcu):
        print("""
*--------------*
|Tabla del:""", SumaIniAcu, """ | 
*--------------*
""")
        for numero3 in range(0, 11):
            operacion2 = numero3 * SumaIniAcu
            print((SumaIniAcu), "*", numero3 ,"=", operacion2)

        print("""
*------------------*
|Fin tabla del:""", SumaIniAcu, """ | 
*------------------*
""")
# ----- Fin Función Desarrollo ----- # 

# ------ Función Final ----- # 
    def multiplicar2 (Final):
        print("""
*--------------*
|Tabla del:""", Final, """ | 
*--------------*
""")
        for numero2 in range(0,11):
            operacion1 = Final * numero2
            print(Final, "*", numero2 ,"=", operacion1)

        print("""
*------------------*
|Fin tabla del:""", Final, """ | 
*------------------*
""")
# ----- Fin Función Final ----- # 

# ========================== Fin Funciones ========================= #

#========================== Lógica para imprimir las tablas n veces ========================= #

    """
    Aquí es dónde está la magía del código, está compuesto por un while que es el que se encarga de ir llamando las funciones en orden.
    Primero me llama la función Inicio, que se encarga de iniciar con la tabla que el usuario quiere.
    Después entra al while y lo ejecuta hasta que la función Desarrollo, que en este caso va imprimir la multiplicación de las tablas hasta que llegue el turno de llamar a la última función.
    """
  
    acumulador = 1
    multiplicar(Inicio)
    while True:
        multiplicar3(Inicio+acumulador)

        if (Final - 1) == Inicio + acumulador:
            multiplicar2(Final)
            break
        elif (Final) == Inicio + acumulador:
            break
        acumulador += 1
        continue
    
# ========================== Fin Lógica para imprimir las tablas n veces ========================= # 

# ========================== Agradecimiento por usar el programa ========================= #  

    """
    Aquí imprimo por pantalla el agradecimiento y por quién fue creado, en este caso por mi.
    """

    print(em("""
*-----------------------------------------*
|  ¡Programa 8 Finalizado exitosamente! :smiling_face_with_smiling_eyes:|
*-----------------------------------------*
"""))
# ========================== Fin Agradecimiento por usar el programa ========================= #
programa8()