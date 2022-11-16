""" 
Escriba un programa que calcule el precio a pagar por el suministro de energía eléctrica. Se debe preguntar la cantidad de kwh 
consumidos y el tipo de instalación: R para residencias, I para industrias y C para comercios. Calcule el precio a pagar de acuerdo 
con la siguiente tabla. (Tabla en la plataforma UNPHU)
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

print("""\n
*------------------------------------------------------*
|Precio a pagar por el suministro de energía eléctrica.|
*------------------------------------------------------*
""")# Decorando el nombre.

print("""
*--------------------------------------*
|Tipos de instalacciones a seleccionar.|
*--------------------------------------*
\n""")# Decorando la pregunta.

print("""
*---------------*
|R = Residencial|
|---------------|
|C = Comercial  |
|---------------|
|I = Industrial |
*---------------*
\n""")# Decorando las opciones.

# Declaro las variables a utilizar, tipo de instalacion y kilo waths consumidos.
TipoInstalacion = str(input("Ingrese el tipo de instalación: ")) # Tipo de instalacion.
kwhConsumido = int(input("Ingrese la cantidad de Kilo Watts consumidos: "))# Kilo Whatts consumidos.

# Condiciones para saber que tipo de instalacion tienen los usuarios.
if TipoInstalacion == "R":# Aqui para saber si su instalacion es tipo R.
    if kwhConsumido == 1 or kwhConsumido <= 500:# Sentencia para saber si la cantidad de Kilo watts es menor a 500.
        print("\nEl precio a pagar es de: RD$550.00")# Precio a pagar dependiendo de si su consumo es menor a 500.
    elif kwhConsumido > 500:# Sentencia para saber si la cantidad de Kilo watts es mayor a 500.
        print("\nEl precio a pagar es de: RD$850.00")# Precio a pagar dependiendo de si su consumo es mayor a 500.
elif TipoInstalacion == "C":# Aqui para saber si su instalacion es tipo C.
    if kwhConsumido == 1 or kwhConsumido <= 1000:#Sentencia para saber si la cantidad de Kilo watts es menor a 1000.
        print("\nEl precio a pagar es de: RD$1300.00")#Precio a pagar dependiendo de si su consumo es menor a 1000.
    elif kwhConsumido > 1000:# Sentencia para saber si la cantidad de Kilo watts es mayor a 1000.
        print("\nEl precio a pagar es de: RD$2500.00")#Precio a pagar dependiendo de si su consumo es mayor a 1000.
elif TipoInstalacion == "I":# Aqui para saber si su instalacion es tipo I.
    if kwhConsumido == 1 or kwhConsumido <= 5000:# Sentencia para saber si la cantidad de Kilo watts es menor a 5000.
        print("\nEl precio a pagar es de: RD$3800.00")# Precio a pagar dependiendo de si su consumo es menor a 5000.
    elif kwhConsumido > 5000:# Sentencia para saber si la cantidad de Kilo watts es mayor a 5000.
        print("\nEl precio a pagar es de: RD$4200.00")# Precio a pagar dependiendo de si su consumo es mayor a 5000.
else:
    print("\nLo siento, lo que haz introducido no es la letra que corresponde a una de las opciones de tipo de instalacion. ") #En caso de que el usuario no marque correctamente la letra de su tipo de instalacion.
        
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