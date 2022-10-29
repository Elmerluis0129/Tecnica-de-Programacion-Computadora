"""
Escriba un programa que dado un texto con n palabras realice lo siguiente:

Determine cuántas palabras comienzan con consonantes.
Determine cuántas palabras comienzan con vocales.
Retorne el texto capitalizado.

Elmer Saint-Hilare 21-1354
"""
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
    time.sleep(0.07)
    print(barraProgreso(i, limite, 50), end = "\r")
    
print("\n")
    
# ============== Fin Barra de porcentaje ============== #

print("""
*---------------------------------------*  
|      Texto - Consonantes, Vocales     |
*---------------------------------------*
""")

print("Por favor no introducir vocales con acento. (á,é,í,ó,ú)")
texto = input("Ingrese texto:\n> ").lower()


diccionario = {}
listavocales = ['a','e','i','o','u','á','é','í','ó','ú']
    

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
        elif m[a].startswith('á')|m[a].startswith('é')|m[a].startswith('í')|m[a].startswith('ó')|m[a].startswith('ú'):
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


funcion1(texto.split(' '))
ConteoVocalesConsonantes(e,o)
print("\n",diccionario)
texto = texto.title()
print("\nEl texto capitalizado es: ", texto)