"""
Escriba un programa que mediante módulos tenga el siguiente menú de opciones, y realice lo que se indica para cada una de ellas:

Diccionario de caracteres. Solicitar una cadena de caracteres y devolver un diccionario con la cantidad de apariciones de cada caracter (sin repetir) en la cadena. Si la cadena tiene espacios, el diccionario debe tener la clave 'espacio'.
Formato de fechas. Solicitar una fecha por teclado (día, mes y año), y retornarla en el siguiente formato de ejemplo: Sábado 29 de octubre del 2022.

Elmer Saint-Hilare 21-1354

"""

# ================= Importaciones ================= #
"""
Aquí importo mis 12 programas, para tener acceso a los mismo con su respectivos nombres, del ms1 al ms12.
"""
from Módulos import TAR01_Elmer_Saint_Hilare as ms1
from Módulos import TAR02_Elmer_Saint_Hilare as ms2
from Módulos import TAR03_Elmer_Saint_Hilare as ms3
from Módulos import TAR04_Elmer_Saint_Hilare as ms4
from Módulos import TAR05_Elmer_Saint_Hilare as ms5
from Módulos import TAR06_Elmer_Saint_Hilare as ms6
from Módulos import TAR07_Elmer_Saint_Hilare as ms7
from Módulos import TAR08_Elmer_Saint_Hilare as ms8
from Módulos import TAR09_Elmer_Saint_Hilare as ms9
from Módulos import TAR10_Elmer_Saint_Hilare as ms10
from Módulos import TAR11_Elmer_Saint_Hilare as ms11
from Módulos import TAR12_Elmer_Saint_Hilare as ms12
# =============== Fin Importaciones =============== #


# ================= Menú de opciones ================= #
"""
Muestro por pantalla mi menú de opciones.
"""
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
# =============== Fin Menú de opciones =============== #
x = "1"
print("Si quieres salir solo tienes que escribir: Fin")
while True:
    if x == 3:
        break
    elif x == "1":
        eleccion = input("¿Qué programa desea ejecutar? \n> ")
    if eleccion == "1":
        ms1.programa1()
        x = "1"
        print("Recuerda que si quieres salir solo tienes que escribir: \"Fin\"")
        
    elif eleccion == "2":
        ms2.programa2()
        x = "1"
        print("Recuerda que si quieres salir solo tienes que escribir: \"Fin\"")
        
    elif eleccion == "3":
        ms3.programa3()
        x = "1"
        print("Recuerda que si quieres salir solo tienes que escribir: \"Fin\"")
        
    elif eleccion == "4":
        ms4.programa4()
        x = "1"
        print("Recuerda que si quieres salir solo tienes que escribir: \"Fin\"")
        
    elif eleccion == "5":
        ms5.programa5()
        x = "1"
        print("Recuerda que si quieres salir solo tienes que escribir: \"Fin\"")
        
    elif eleccion == "6":
        ms6.programa6()
        x = "1"
        print("Recuerda que si quieres salir solo tienes que escribir: \"Fin\"")
        
    elif eleccion == "7":
        ms7.programa7()
        x = "1"
        print("Recuerda que si quieres salir solo tienes que escribir: \"Fin\"")
        
    elif eleccion == "8":
        ms8.programa8()
        x = "1"
        print("Recuerda que si quieres salir solo tienes que escribir: \"Fin\"")
        
    elif eleccion == "9":
        ms9.programa9()
        x = "1"
        print("Recuerda que si quieres salir solo tienes que escribir: \"Fin\"")
        
    elif eleccion == "10":
        ms10.programa10()
        x = "1"
        print("Recuerda que si quieres salir solo tienes que escribir: \"Fin\"")
        
    elif eleccion == "11":
        ms11.programa11()
        x = "1"
        print("Recuerda que si quieres salir solo tienes que escribir: \"Fin\"")
        
    elif eleccion == "12":
        ms12.programa12()
        x = "1"
        print("Recuerda que si quieres salir solo tienes que escribir: \"Fin\"")
        
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