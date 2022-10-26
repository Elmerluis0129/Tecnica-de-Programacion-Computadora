"""
TAR13 - Módulos

Escriba un programa que mediante módulos tenga el siguiente menú de opciones, y realice lo que se indica para cada una de ellas:

Diccionario de caracteres. Solicitar una cadena de caracteres y devolver un diccionario con la cantidad de apariciones de cada caracter (sin repetir) en la cadena. Si la cadena tiene espacios, el diccionario debe tener la clave 'espacio'.
Formato de fechas. Solicitar una fecha por teclado (día, mes y año), y retornarla en el siguiente formato de ejemplo: Sábado 29 de octubre del 2022.

Elmer Saint-Hilare 21-1354
"""




print("""
*----------------------*
|   Menú de opciones   | 
*----------------------*

|1.-| Diccionario de caracteres.
|2.-| Formato de fecha.
""")

seleccion = input("> ")
while True:
    if seleccion == "2":
        import FormatoFecha
        break
    elif seleccion == "1":
        import DiccionarioCaracteres
        break
    else:
        while True:
            print("¡Lo siento! Lo que haz introducido no está en nuestro menú de opciones.\n")
            print("""
Seleccione una opción:

|1.-| Diccionario de caracteres.
|2.-| Formato de fecha.
""")
            seleccion = input("> ")
        
            if seleccion == "2" or seleccion == "1":
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