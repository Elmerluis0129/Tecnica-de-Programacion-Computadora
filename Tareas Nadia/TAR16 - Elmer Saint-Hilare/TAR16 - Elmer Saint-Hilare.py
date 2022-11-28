"""
Usando Programación Orientada a Objetos, escribir un programa que permita registrar n películas con los siguientes datos:

Nombre.
Categoría. (Deben estar predefinidas en una clase Categoría).
Director.
Año lanzamiento.
Cantidad de taquillas vendidas.
Luego, generar un archivo de texto plano (.txt) con las películas que se hayan registrado. La estructura de este archivo debe ser la siguiente (datos de ejemplo)

Indicaciones:

Se debe solicitar la cantidad de películas.
Las clases deben estar en archivos separados (Película y Categoría).
Deben existir categorías previamente definidas (las que usted desee).
Al momento de indicar la categoría de una película, se debe elegir de las que ya existan.
Incluir una opción que permita generar un archivo .csv con las películas que tengan un total de taquillas >= 2,000
Se deben controlar las excepciones (data basura) haciendo uso de try-except.

Elmer Saint-Hilare 21-1354
"""

import TAR16_Elmer_Saint_Hilare_Categoria as T16

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
    barra = f"[{'+' * completado}{'-' * restante}{porcentaje:.0%}]"
    return barra

input("\nPresione Enter para iniciar el programa... \n")
print("\nCargando... Por favor espere.")
for i in range(limite+1):
    time.sleep(0.02)
    print(barraProgreso(i, limite, 50), end = "\r")
    
print("\n")
    
# ============== Fin Barra de porcentaje ============== #

T16.Catego.categorias()



class Pelis():
    def __init__(self, cantidadPelis, archivoCSV):
        self.CantidadPelis = cantidadPelis
        self.archivoCSV = archivoCSV
        
        
while True:
    try:
        CantidadPelis = int(input("Ingrese la cantidad de peliculas que quiere registrar: \n> "))
        archivoCSV = int(input("Desea generar un archivo csv con las peliculas con taquillas mayor o igual a 2000? / 1 = Sí, 0 = No / Responder con el número.\n> "))
        break
    except ValueError:
        print("\nLo siento, no se acepta data basura.\n")
        continue
    
Peliculas = Pelis(CantidadPelis, archivoCSV)
    
x = 0
p = 0
n = 1
while x != Peliculas.CantidadPelis:
    archivo = open("Peliculas registradas.txt", "a")
    if n:
        archivo.write("Nombre|Categoria|Director|Año|Total taquillas\n")
        n = 0
    nombrePeli = input("Nombre pelicula\n> ")
    archivo.write(nombrePeli+"|")
    while True:
        categoria = input("Categoría pelicula\n> ")
        if categoria == "1": archivo.write("Horror|")
        elif categoria == "2": archivo.write("Drama|")
        elif categoria == "3": archivo.write("Comedia|")
        elif categoria == "4": archivo.write("Sangrienta|")
        elif categoria == "5": archivo.write("Acción|")
        elif categoria == "6": archivo.write("Aventura|")
        elif categoria == "7": archivo.write("Thrieler|")
        elif categoria == "8": archivo.write("Infantil|")
        elif categoria == "9": archivo.write("Animadas|")
        elif categoria == "10": archivo.write("Cartoon|")
        elif categoria == "11": archivo.write("Animales|")
        elif categoria == "12": archivo.write("Naturaleza|")
        elif categoria == "13": archivo.write("Otra|")
        else: 
            print("\nLo siento, no ha marcado una categoría del menú de categorías, vuelva a intentarlo.\n")
            continue
        break
    directorPeli = input("Director pelicula\n> ")
    archivo.write(directorPeli+"|")
    while True:
        try:
            año = int(input("Año de lanzamiento de la pelicula\n> "))
            taquillas = int(input("Cantidad de taquilla de la pelicula\n>"))
            archivo.write(str(año))
            archivo.write("|")
            archivo.write(f"{taquillas:,}")
            archivo.write("\n")
            break
        except ValueError:
            print("\nLo siento, no se acepta data basura.\n")
            continue
        
        
        
    if Peliculas.archivoCSV:
        archivo2 = open("Peliculas taquillas 2000.csv", "a")
        if taquillas >= 2000:
            if not n:
                archivo2.write("Nombre,Categoria,Director,Año,Total taquillas")
                archivo2.write("\n")
                n = None
            archivo2.write(nombrePeli)
            archivo2.write(",")
            while True:
                if categoria == "1": archivo2.write("Horror,")
                elif categoria == "2": archivo2.write("Drama,")
                elif categoria == "3": archivo2.write("Comedia,")
                elif categoria == "4": archivo2.write("Sangrienta,")
                elif categoria == "5": archivo2.write("Acción,")
                elif categoria == "6": archivo2.write("Aventura,")
                elif categoria == "7": archivo2.write("Thrieler,")
                elif categoria == "8": archivo2.write("Infantil,")
                elif categoria == "9": archivo2.write("Animadas,")
                elif categoria == "10": archivo2.write("Cartoon,")
                elif categoria == "11": archivo2.write("Animales,")
                elif categoria == "12": archivo2.write("Naturaleza",)
                elif categoria == "13": archivo2.write("Otra,")
                else: 
                    print("\nLo siento, no ha marcado una categoría del menú de categorías, vuelva a intentarlo.\n")
                    continue
                break
            archivo2.write(directorPeli+",")
            archivo2.write(str(año)+",")
            archivo2.write(f"{taquillas}")
            archivo2.close()

    x += 1
    archivo.close()



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