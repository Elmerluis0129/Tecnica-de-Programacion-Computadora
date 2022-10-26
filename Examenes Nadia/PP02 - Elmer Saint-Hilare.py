"""
Escriba un programa que mediante módulos tenga el siguiente menú de opciones, y realice lo que se indica para cada una de ellas:

Diccionario de caracteres. Solicitar una cadena de caracteres y devolver un diccionario con la cantidad de apariciones de cada caracter (sin repetir) en la cadena. Si la cadena tiene espacios, el diccionario debe tener la clave 'espacio'.
Formato de fechas. Solicitar una fecha por teclado (día, mes y año), y retornarla en el siguiente formato de ejemplo: Sábado 29 de octubre del 2022.

Elmer Saint-Hilare 21-1354

"""


x = "1"
print("""
*--------------------------------------*
|          Menú de opciones            |
*--------------------------------------*
|1.-| Operaciones Básicas.             |
|--------------------------------------|
|2.-| Entrada teclado.                 |
|--------------------------------------|
|3.-| Precio de energía eléctrica.     |
|--------------------------------------|
|4.-| Veces que se repite una palabra. |
|--------------------------------------|
|5.-| Números de lotería.              |
|--------------------------------------|
|6.-| Préstamos usando while.          |
|--------------------------------------|
|7.-| Lista de caracteres usando while.|
|--------------------------------------|
|8.-| Tablas de multiplicar.           |
|--------------------------------------|
|9.-| Primer caracter que no se repite.|
|--------------------------------------|
|10.-| Más funciones.                  |
|--------------------------------------|
|11.-| Sets a partir de listas.        |
|--------------------------------------|
|12.-| Los viajeros.                   |
*--------------------------------------*
""")

print("Si quieres salir solo tienes que escribir: Fin")
while True:
    if x == 3:
        break
    elif x == "1":
        eleccion = input("¿Qué programa desea ejecutar? \n> ")
    if eleccion == "1":
        import Módulos.TAR01_Elmer_Saint_Hilare
        
        x = "1"
        print("Recuerda que si quieres salir solo tienes que escribir: Fin")
    elif eleccion == "2":
        import Módulos.TAR02_Elmer_Saint_Hilare
        print("Recuerda que si quieres salir solo tienes que escribir: Fin")
        x = "1"
    elif eleccion == "3":
        import Módulos.TAR03_Elmer_Saint_Hilare
        x = "1"
        print("Recuerda que si quieres salir solo tienes que escribir: Fin")
    elif eleccion == "4":
        import Módulos.TAR04_Elmer_Saint_Hilare
        x = "1"
        print("Recuerda que si quieres salir solo tienes que escribir: Fin")
    elif eleccion == "5":
        import Módulos.TAR05_Elmer_Saint_Hilare
        x = "1"
        print("Recuerda que si quieres salir solo tienes que escribir: Fin")
    elif eleccion == "6":
        import Módulos.TAR06_Elmer_Saint_Hilare
        x = "1"
        print("Recuerda que si quieres salir solo tienes que escribir: Fin")
    elif eleccion == "7":
        import Módulos.TAR07_Elmer_Saint_Hilare
        x = "1"
        print("Recuerda que si quieres salir solo tienes que escribir: Fin")
    elif eleccion == "8":
        import Módulos.TAR08_Elmer_Saint_Hilare
        x = "1"
        print("Recuerda que si quieres salir solo tienes que escribir: Fin")
    elif eleccion == "9":
        import Módulos.TAR09_Elmer_Saint_Hilare
        x = "1"
        print("Recuerda que si quieres salir solo tienes que escribir: Fin")
    elif eleccion == "10":
        import Módulos.TAR10_Elmer_Saint_Hilare
        x = "1"
        print("Recuerda que si quieres salir solo tienes que escribir: Fin")
    elif eleccion == "11":
        import Módulos.TAR11_Elmer_Saint_Hilare
        x = "1"
        print("Recuerda que si quieres salir solo tienes que escribir: Fin")
    elif eleccion == "12":
        import Módulos.TAR12_Elmer_Saint_Hilare
        x = "1"
        print("Recuerda que si quieres salir solo tienes que escribir: Fin")
        
    elif eleccion == "Fin":
        print("\nCerrando el programa general...")
        break
    elif eleccion != "12":
        while True:
            
            print("Lo siento, lo que haz introducido no va acorde con los números del menú de opciones.")
            print("Intenta de nuevo.\n")
            eleccion = input("¿Qué programa desea ejecutar? \n> ")
            if eleccion == "1"  or eleccion == "2" or eleccion == "3" or eleccion == "4" or eleccion == "5" or eleccion == "6" or eleccion == "7" or eleccion == "8" or eleccion == "9" or eleccion == "10" or eleccion == "11" or eleccion == "12":
                x = "2"
                break
            elif eleccion == "Fin":
                print("\nCerrando el programa general...")
                x = 3
                break     
        continue
            
#Módulos.TAR01_Elmer_Saint_Hilare


# ========================== Agradecimiento por usar el programa ========================= #  

"""
Aquí imprimo por pantalla el agradecimiento y por quién fue creado, en este caso por mi.
"""

print("""
*----------------------------------------------------------------------------*
| ¡Muchas gracias por utilizar mi programa! / By: Elmer Saint-Hilare 21-1354 |
*----------------------------------------------------------------------------*
""")
# ========================== Fin Agradecimiento por usar el programa ========================= #