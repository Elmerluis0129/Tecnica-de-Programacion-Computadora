"""
Escribir un programa que mediante el uso de variables y operadores aritméticos, almacene la suma, resta, multiplicación y división de 2 números. Luego, mostrar los resultados.
Elmer Saint-Hilare 21-1354
"""

from emoji import emojize as em # Esto no es parte del ejercicio, es decoración.

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
    time.sleep(0.03)
    print(barraProgreso(i, limite, 50), end = "\r")
    
print("\n")
    
# ============== Fin Barra de porcentaje ============== #


def programa1 (): # Esta linea no es parte del ejercicio, es del examen.
#Nombre del programa.
    print("""
*--------------------*
| Calculadora Básica |
*--------------------*
""")#Decorando el nombre.

    print("""
Operaciones:

1.- Sumar
2.- Restar
3.- Multiplicar
4.- Dividir
""")

    print("""
*-----------------------------*
|    Todas las operaciones    |
*-----------------------------*
""")#Decorando.


    #Entrada de los numeros / Variables
    num1 = 96 # Numero 1.
    num2 = 347 # Numero 2.

    #Operaciones.
    Sumar = num1+num2
    Restar = num1-num2
    Multiplicar = num1*num2
    Dividir = num1/num2

#Resultado operaciones.
    print(f"""
El resultado en todas las operaciones con los números: {num1} y {num2}

La suma de """, f'{num1}',f'+ {num2} = {Sumar}',"""
La resta de """, f'{num1}',f'- {num2} = {Restar}',"""
La multiplicación de """, f'{num1}',f'* {num2} = {Multiplicar}',"""
La división de """, f'{num1}',f'/ {num2} = {Dividir}'
)

#========================== Agradecimiento por usar el programa =========================#  


#Aquí imprimo por pantalla el agradecimiento y por quién fue creado, en este caso por mi.


    print(em("""
*-----------------------------------------*
|  ¡Programa 1 Finalizado exitosamente! :smiling_face_with_smiling_eyes:|
*-----------------------------------------*
"""))
#========================== Fin Agradecimiento por usar el programa =========================#
programa1 ()