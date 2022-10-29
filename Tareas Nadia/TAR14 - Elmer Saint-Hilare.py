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

# ============== Nombre Programa ============== #
print("""
*---------------------------------------*  
|      Texto - Consonantes, Vocales     |
*---------------------------------------*
""")
# ============ Fin Nombre Programa ============ #

# ============ Variables generales ============ #
texto = input("Ingrese texto:\n> ").lower()
diccionario = {}
# ========== Fin Variables generales ========== #

# ============ Funciones ============ #
# ------------ Función 1 -------------#
"""
Aquí lo que hago es especificar algunos contadores, los cuales los uso para facilitar la busqueda entre elementos e ir teniendo una cuenta de las consonantes y vocales.
con el for recorro cada palabra del texto.
con los condicionales es para saber si empieza con vocal, o consonantes e irlas agregando según con lo que empiecen al diccionario.
"""
def VocalConsonante(m):
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
# ---------- Fin Función 1 -----------#

# ------------ Función 2 -------------#
"""
Aquí grego la cantidad de vocales y consonantes que encontró.
"""
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
# ---------- Fin Función 2 -----------#
# ========== Fin Funciones ========== #

# ============ Llamando funciones ============ #
"""
Aquí llamo mis funciones.
"""
VocalConsonante(texto.split(' '))
ConteoVocalesConsonantes(e,o)
# ========== Fin Llamando funciones ========== #

# ========== Impresión por pantalla ========== #
"""
Aquí imprimo en pantalla todos los resultados ya calculados.
"""
print("\n",diccionario)
texto = texto.title()
print("\nEl texto capitalizado es: ", texto)
# ======== Fin Impresión por pantalla ======== #

#========================== Agradecimiento por usar el programa =========================#  

"""
Aquí imprimo por pantalla el agradecimiento y por quién fue creado, en este caso por mi.
"""

print("""
*----------------------------------------------------------------------------*
| ¡Muchas gracias por utilizar mi programa! / By: Elmer Saint-Hilare 21-1354 |
*----------------------------------------------------------------------------*
""")
#========================== Fin Agradecimiento por usar el programa =========================#