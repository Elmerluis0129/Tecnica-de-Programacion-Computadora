"""
Escriba un programa que dado un texto con n palabras realice lo siguiente:

Determine cuántas palabras comienzan con consonantes.
Determine cuántas palabras comienzan con vocales.
Retorne el texto capitalizado.

Elmer Saint-Hilare 21-1354
"""

from tkinter import E


print("""
*---------------------------------------*  
|      Texto - Consonantes, Vocales     |
*---------------------------------------*
""")

texto = input("Ingrese texto:\n> ")

separado_por_espacios = texto.split(' ')
diccionario = {}

a = 0
e = 0
o = 0
for x in separado_por_espacios:
    if separado_por_espacios[a].startswith('a')|separado_por_espacios[a].startswith('e')|separado_por_espacios[a].startswith('i')|separado_por_espacios[a].startswith('o')|separado_por_espacios[a].startswith('u'):
        diccionario.update(
            {
                separado_por_espacios[a]:"Vocal"
            }
            )
        e += 1
    else:
        diccionario.update(
            {
                separado_por_espacios[a]:"Consonante"
            }
        )        
        o += 1
    a += 1
texto.abs

diccionario.update(
            {
                "Vocales":e
            }
            )
diccionario.update(
            {
                "Consonantes":o
            }
            )

print(diccionario)


#StrA = "".join(separado_por_espacios)
# TODO PONER A QUE IMPRIMA EL TEXTO CAPITALIZADO