"""
Escriba un programa que dado un texto con n palabras realice lo siguiente:

Determine cuántas palabras comienzan con consonantes.
Determine cuántas palabras comienzan con vocales.
Retorne el texto capitalizado.

Elmer Saint-Hilare 21-1354
"""

print("""
*---------------------------------------*  
|      Texto - Consonantes, Vocales     |
*---------------------------------------*
""")

print("Por favor no introducir vocales con acento. (á,é,í,ó,ú)")
texto = input("Ingrese texto:\n> ")
texto1 = texto.lower()

diccionario = {}


def funcion1(m):
    a = 0
    global e
    global o
    e = 0
    o = 0
    for x in m:
        if m[a].startswith('a')|m[a].startswith('e')|m[a].startswith('i')|m[a].startswith('o')|m[a].startswith('u'):
            diccionario.update(
                {
                    m[a]:"Vocal"
                }
                )
            
            e += 1
        else:
            diccionario.update(
                {
                    m[a]:"Consonante"
                }
            )        
            o += 1
        a += 1
        


def ConteoVocalesConsonantes (TotalVocal, TotalConsonante):
    diccionario.update(
                {
                    "Vocales":TotalVocal
                }
                )
    diccionario.update(
                {
                    "Consonantes":TotalConsonante
                }
                )




funcion1(texto1.split(' '))
ConteoVocalesConsonantes(e,o)
print(diccionario)
#TODO PONER A QUE CAPITALIZE TODAS LAS LETRAS DEL TEXTO.