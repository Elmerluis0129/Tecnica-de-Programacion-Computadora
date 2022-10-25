"""
Escribir un programa que mediante el uso de variables y operadores aritméticos, almacene la suma, resta, multiplicación y división de 2 números. Luego, mostrar los resultados.
Elmer Saint-Hilare 21-1354
"""

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
num2 = 300 # Numero 2.

#Operaciones.
Sumar = num1+num2
Restar = num1-num2
Multiplicar = num1*num2
Dividir = num1/num2

#Resultado operaciones.
print("\nEl resultado en todas las operaciones es: \n\nSuma: ", num1,"+",num2,"=", Sumar, "\nResta: ", num1,"-",num2,"=", Restar, "\nMultiplicación: ", num1,"*",num2,"=", Multiplicar, "\nDivisión: ", num1,"/",num2,"=", round(Dividir, 2))


#========================== Agradecimiento por usar el programa =========================#  

"""
Aquí imprimo por pantalla el agradecimiento y por quién fue creado, en este caso por mi.
"""

print("""
*----------------------------------------------------------------------------*
|  ¡Programa 1 Finalizado exitosamente! / By: Elmer Saint-Hilare 21-1354     |
*----------------------------------------------------------------------------*
""")
#========================== Fin Agradecimiento por usar el programa =========================#