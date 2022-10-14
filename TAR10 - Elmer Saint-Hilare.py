"""
Escriba un programa que, mediante el uso de funciones realice lo siguiente:

Dado un número entero, realice la suma de sus dígitos.
Con el resultado de la suma, realizar lo siguiente:
Generar los números del 1 al s (suma), y a su vez hacer las siguientes condiciones:
Si el número es divisor de 3, mostrar el número y la palabra "Fizz".
Si el número es divisor de 5, mostrar el número y la palabra "Buzz".
Si el número es divisor de 3 y 5 (ambos), mostrar el número y la palabra "FizzBuzz".
Si el número no es divisor de ninguno (3 y 5), únicamente mostrar el número.
Elmer Saint-Hilare 21-1354
"""

#============================ Funciones ============================#
""" Documentación Funciones:
Las funciones es dónde tengo la lógica del programa, aquí me identifica con las condiciones cuál es divisor con 3 y con 5, o con ambos para luego imprimirme lo que se pide.
Aquí es dónde hago la multiplicación de cada uno de los digitos, dependiendo de las fucniones.
Cada función es para cada uno de los dígitos, para así poder controlar y especificarle a la máquina cuándo va calcular 3, o cuando va a calcular 8 digitos.
Las funciones me reciben un parámetro, que en este caso es la entrada de del número entero.
Ellos entran como str, por eso los paso a int para luego sumarlos y con la suma de ellos poder continuar con las iteraciones.
Con el bucle for también es para que me haga el proceso, empezando desde el 1 hasta la 1 + de la suma de dicha operación.
Fin documentación funciones."""

#--------------# Función 1 #--------------#    
def Suma_Digitos1(x):
    digito1 = x[0]
    
    operacion = int(digito1)
    print("\n",digito1, "=", operacion)
    
    for n in range(1, operacion+1):
        print(n)
        if n %3 == 0:
            if n %5 == 0: print("FizzBuzz")
            else: print("Fizz")
        elif n %5 == 0: print("Buzz")
#--------------# Función 2 #--------------#     
def Suma_Digitos2(x):
    digito1 = x[0]
    digito2 = x[1]

    operacion = int(digito1) + int(digito2)
    print("\n",digito1, "+", digito2, "=", operacion)
    
    for n in range(1, operacion+1):
        print(n)
        if n %3 == 0:
            if n %5 == 0: print("FizzBuzz")
            else: print("Fizz")
        elif n %5 == 0: print("Buzz")
#--------------# Función 3 #--------------# 
def Suma_Digitos3(x):
    digito1 = x[0]
    digito2 = x[1]
    digito3 = x[2]

    operacion = int(digito1) + int(digito2) + int(digito3)
    print("\n",digito1, "+", digito2, "+", digito3,"=", operacion)

    for n in range(1, operacion+1):
        print(n)
        if n %3 == 0:
            if n %5 == 0: print("FizzBuzz")
            else: print("Fizz")
        elif n %5 == 0: print("Buzz")
#--------------# Función 4 #--------------#        
def Suma_Digitos4(x):
    digito1 = x[0]
    digito2 = x[1]
    digito3 = x[2]
    digito4 = x[3]

    operacion = int(digito1) + int(digito2) + int(digito3) + int(digito4)
    print("\n",digito1, "+", digito2, "+", digito3,"+", digito4,"=", operacion)
    
    for n in range(1, operacion+1):
        print(n)
        if n %3 == 0:
            if n %5 == 0: print("FizzBuzz")
            else: print("Fizz")
        elif n %5 == 0: print("Buzz")
#--------------# Función 5 #--------------#     
def Suma_Digitos5(x):
    digito1 = x[0]
    digito2 = x[1]
    digito3 = x[2]
    digito4 = x[3]
    digito5 = x[4]

    operacion = int(digito1) + int(digito2) + int(digito3) + int(digito4) + int(digito5)
    print("\n",digito1, "+", digito2, "+", digito3,"+", digito4,"+", digito5, "=", operacion)
        
    print("""
*--------------*
|   FizzBuzz   |
*--------------*
""")
    for n in range(1, operacion+1):
        print(n)
        if n %3 == 0:
            if n %5 == 0: print("FizzBuzz")
            else: print("Fizz")
        elif n %5 == 0: print("Buzz")
#--------------# Función 6 #--------------#             
def Suma_Digitos6(x):
    digito1 = x[0]
    digito2 = x[1]
    digito3 = x[2]
    digito4 = x[3]
    digito5 = x[4]
    digito6 = x[5]

    operacion = int(digito1) + int(digito2) + int(digito3) + int(digito4) + int(digito5) + int(digito6)
    print("\n",digito1, "+", digito2, "+", digito3,"+", digito4,"+", digito5, digito6, "=", operacion)
        
    print("""
*--------------*
|   FizzBuzz   |
*--------------*
""")
    for n in range(1, operacion+1):
        print(n)
        if n %3 == 0:
            if n %5 == 0: print("FizzBuzz")
            else: print("Fizz")
        elif n %5 == 0: print("Buzz")
#--------------# Función 7 #--------------#             
def Suma_Digitos7(x):
    digito1 = x[0]
    digito2 = x[1]
    digito3 = x[2]
    digito4 = x[3]
    digito5 = x[4]
    digito6 = x[5]
    digito7 = x[6]

    operacion = int(digito1) + int(digito2) + int(digito3) + int(digito4) + int(digito5) + int(digito6) + int(digito7)
    print("\n",digito1, "+", digito2, "+", digito3,"+", digito4,"+", digito5, digito6, "+", digito7, "=", operacion)
        
    print("""
*--------------*
|   FizzBuzz   |
*--------------*
""")
    for n in range(1, operacion+1):
        print(n)
        if n %3 == 0:
            if n %5 == 0: print("FizzBuzz")
            else: print("Fizz")
        elif n %5 == 0: print("Buzz")
#--------------# Función 8 #--------------#             
def Suma_Digitos8(x):
    digito1 = x[0]
    digito2 = x[1]
    digito3 = x[2]
    digito4 = x[3]
    digito5 = x[4]
    digito6 = x[5]
    digito7 = x[6]
    digito8 = x[7]

    operacion = int(digito1) + int(digito2) + int(digito3) + int(digito4) + int(digito5) + int(digito6) + int(digito7) + int(digito8)
    print("\n",digito1, "+", digito2, "+", digito3,"+", digito4,"+", digito5, digito6, "+", digito7, "+", digito8, "=", operacion)
        
    print("""
*--------------*
|   FizzBuzz   |
*--------------*
""")
    for n in range(1, operacion+1):
        print(n)
        if n %3 == 0:
            if n %5 == 0: print("FizzBuzz")
            else: print("Fizz")
        elif n %5 == 0: print("Buzz")
#--------------# Función 9 #--------------#             
def Suma_Digitos9(x):
    digito1 = x[0]
    digito2 = x[1]
    digito3 = x[2]
    digito4 = x[3]
    digito5 = x[4]
    digito6 = x[5]
    digito7 = x[6]
    digito8 = x[7]
    digito9 = x[8]

    operacion = int(digito1) + int(digito2) + int(digito3) + int(digito4) + int(digito5) + int(digito6) + int(digito7) + int(digito8) + int(digito9)
    print("\n",digito1, "+", digito2, "+", digito3,"+", digito4,"+", digito5, digito6, "+", digito7, "+", digito8,"+", digito9,"=", operacion)
        
    print("""
*--------------*
|   FizzBuzz   |
*--------------*
""")
    for n in range(1, operacion+1):
        print(n)
        if n %3 == 0:
            if n %5 == 0: print("FizzBuzz")
            else: print("Fizz")
        elif n %5 == 0: print("Buzz")
#--------------# Función 10 #--------------#             
def Suma_Digitos10(x):
    digito1 = x[0]
    digito2 = x[1]
    digito3 = x[2]
    digito4 = x[3]
    digito5 = x[4]
    digito6 = x[5]
    digito7 = x[6]
    digito8 = x[7]
    digito9 = x[8]
    digito10 = x[9]

    operacion = int(digito1) + int(digito2) + int(digito3) + int(digito4) + int(digito5) + int(digito6) + int(digito7) + int(digito8) + int(digito9) + int(digito10)
    print("\n",digito1, "+", digito2, "+", digito3,"+", digito4,"+", digito5, digito6, "+", digito7, "+", digito8,"+", digito9,"+", digito10, "=", operacion)
        
    print("""
*--------------*
|   FizzBuzz   |
*--------------*
""")
    for n in range(1, operacion+1):
        print(n)
        if n %3 == 0:
            if n %5 == 0: print("FizzBuzz")
            else: print("Fizz")
        elif n %5 == 0: print("Buzz")
#============================ Fin Funciones ============================#

#============================ Llamando Funciones ============================#
"""Documentación Llamanda de funciones:
Aquí es para llamar las funciones dependiendo la cantidad de dígitos que el usuario entre.
Hasta el momento sólo controlamos 10 digitos, ya que no quise estender el código mucho más.
Aquí tengo condicionales que son las que se encargan de verificar la longitud de los dígitos, para así poder llamar a la función correcta para dicha cantidad de dígitos.
Aquí también le tengo el mensaje de "Lo siento, no puedes introducir más de 10 digitos." para controlar cuando ponga más de 10 digitos.
Fin Documentación llamada de funciones."""

while True:
    x = str(input("Número entero: \n> "))
    if len(x) == 1: Suma_Digitos1(x)
    elif len(x) == 2: Suma_Digitos2(x)
    elif len(x) == 3: Suma_Digitos3(x)
    elif len(x) == 4: Suma_Digitos4(x)
    elif len(x) == 5: Suma_Digitos5(x)
    elif len(x) == 6: Suma_Digitos6(x)
    elif len(x) == 7: Suma_Digitos7(x)
    elif len(x) == 8: Suma_Digitos8(x)
    elif len(x) == 9: Suma_Digitos9(x)
    elif len(x) == 10: Suma_Digitos10(x)
    else: print("Lo siento, no puedes introducir más de 10 digitos.")
    break
#============================ Fin Llamando Funciones ============================#

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