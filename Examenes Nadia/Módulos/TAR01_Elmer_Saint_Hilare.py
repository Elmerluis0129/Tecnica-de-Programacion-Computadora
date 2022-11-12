"""
Escribir un programa que mediante el uso de variables y operadores aritméticos, almacene la suma, resta, multiplicación y división de 2 números. Luego, mostrar los resultados.
Elmer Saint-Hilare 21-1354
"""

from emoji import emojize as em # Esto no es parte del ejercicio, es decoración.

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
    print("""
El resultado en todas las operaciones es:

La suma de """, '{}'.format(num1),'+ {} = {}'.format(num2, Sumar),"""
La resta de """, '{}'.format(num1),'- {} = {}'.format(num2, Restar),"""
La multiplicación de """, '{}'.format(num1),'* {} = {}'.format(num2, Multiplicar),"""
La división de """, '{}'.format(num1),'/ {} = {}'.format(num2, Dividir)
)

#========================== Agradecimiento por usar el programa =========================#  


#Aquí imprimo por pantalla el agradecimiento y por quién fue creado, en este caso por mi.


    print(em("""
*-----------------------------------------*
|  ¡Programa 1 Finalizado exitosamente! :smiling_face_with_smiling_eyes:|
*-----------------------------------------*
"""))
#========================== Fin Agradecimiento por usar el programa =========================#