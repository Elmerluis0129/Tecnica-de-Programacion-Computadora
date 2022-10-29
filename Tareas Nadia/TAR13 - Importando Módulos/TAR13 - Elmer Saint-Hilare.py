"""
TAR13 - Módulos

Escriba un programa que mediante módulos tenga el siguiente menú de opciones, y realice lo que se indica para cada una de ellas:

Diccionario de caracteres. Solicitar una cadena de caracteres y devolver un diccionario con la cantidad de apariciones de cada caracter (sin repetir) en la cadena. Si la cadena tiene espacios, el diccionario debe tener la clave 'espacio'.
Formato de fechas. Solicitar una fecha por teclado (día, mes y año), y retornarla en el siguiente formato de ejemplo: Sábado 29 de octubre del 2022.

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

# ================ Menú de opciones ================ #
"""
Aquí es donde presento al usuario las opciones que tiene de los diferentes programas.

Y aqui espero la respuesta del mismo.
"""
print("""
*----------------------*
|   Menú de opciones   | 
*----------------------*

|1.-| Diccionario de caracteres.
|2.-| Formato de fecha.
""")

seleccion = input("> ")
# ============== Fin Menú de opciones ============== #

# ============== While - Control ============== #
"""
Aquí controlo lo que son las opciones, y que no me acepte nada mas que no sea las opciones establecidas en el menu que son las de mis programas.

en las condicionales dentro del while, son las que me controlan cuando si y cuando no importar el programa que desea el usuario.

Si introduce algo no esperado, se lo notifica hasta que introduzca lo esperado.
"""
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

# ============ Fin While - Control ============ #

    

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