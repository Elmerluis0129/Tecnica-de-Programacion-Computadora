"""
Escribir un programa que pida 2 números y muestre paso a paso el cálculo de la raíz cuadrada de la suma del cuadrado de ambos.
Elmer Luis Saint-Hilare Rojo / 21-1354. 
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

import math #Aquí importo math para poder hacer uso de la raiz cuadrada.

print("|------------------------------------|")
numero1 = int(input(" Ingrese el primer número: "))#Aquí le pido al usuario el primer número.
print("|------------------------------------|")
numero2 = int(input(" Ingrese el segundo número: "))#Aquí le pido al usuario el segundo número.
numero1cuadrado = pow(numero1,2)#Aquí elevo el primer número que me da el usuario al cuadrado.
numero2cuadrado = pow(numero2,2)#Aquí elevo el segundo número que me da el usuario al cuadrado.
operación = (numero1cuadrado + numero2cuadrado)#Aquí es para que me sume los dos números ya elevados al cuadrado.
resultado = math.sqrt(operación) #Aquí saco raiz de la operacion realizada (La suma de los cuadrados).

#Salidas/proceso que el usuario verá.
print("|----------------------------------------------|")
print("\n El resultado de: ", str(numero1) + "^2 =", numero1cuadrado) #Aquí le muestra el mismo elevado al cuadrado.
print("|----------------------------------------------|")
print("\n El resultado de: ", str(numero2) + "^2 =", numero2cuadrado)#Aquí le muestra el mismo elevado al cuadrado.
print("|----------------------------------------------|")
print("\n La suma de los números es: ", numero1**2, "+", numero2**2, "=", operación) #Aquí le muestra la suma de los números cuadrados.
print("|----------------------------------------------|")
print("\n La raiz de esa suma es: ", round(resultado, 2))#Aquí le muestra ya el resultado de el problema resuelto y utilizamos math.sqrt para sacar la raiz.
print("|----------------------------------------------|")

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