"""
TAR13 - Módulos

Escriba un programa que mediante módulos tenga el siguiente menú de opciones, y realice lo que se indica para cada una de ellas:

Diccionario de caracteres. Solicitar una cadena de caracteres y devolver un diccionario con la cantidad de apariciones de cada caracter (sin repetir) en la cadena. Si la cadena tiene espacios, el diccionario debe tener la clave 'espacio'.
Formato de fechas. Solicitar una fecha por teclado (día, mes y año), y retornarla en el siguiente formato de ejemplo: Sábado 29 de octubre del 2022.

Elmer Saint-Hilare 21-1354
"""

import DiccionarioCaracteres, FormatoFecha


print("""
Seleccione una opción:

|1.-| Diccionario de caracteres.
|2.-| Formato de fecha.
""")
seleccion = int(input("> "))

