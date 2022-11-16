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
from emoji import emojize as em # Esto no es parte del ejercicio, es decoración.

def programa10 ():
    #============================ Funciones ============================#
    """ Documentación Funciones:
    Las funciones es dónde tengo la lógica del programa, aquí me identifica con las condiciones cuál es divisor con 3 y con 5, o con ambos para luego imprimirme lo que se pide.
    Aquí es dónde hago la multiplicación de cada uno de los digitos, dependiendo de las fucniones.
    Cada función es para cada uno de los dígitos, para así poder controlar y especificarle a la máquina cuándo va calcular 3, o cuando va a calcular 8 digitos.
    Las funciones me reciben un parámetro, que en este caso es la entrada del número entero.
    Ellos entran como str, por eso los paso a int para luego sumarlos y con la suma de ellos poder continuar con las iteraciones.
    Con el bucle for también es para que me haga el proceso, empezando desde el 1 hasta la 1 + de la suma de dicha operación.
    Fin documentación funciones."""
    
    #--------------# Función 1 #--------------#    
    def Suma_Digitos1(numeroEntero):
        digito1 = numeroEntero[0]
        
        operacion = int(digito1)
        print("\n",digito1, "=", operacion)

        for numero1 in range(1, operacion+1):
            print(numero1)
            if numero1 %3 == 0:
                if numero1 %5 == 0: print("FizzBuzz")
                else: print("Fizz")
            elif numero1 %5 == 0: print("Buzz")
    #--------------# Función 2 #--------------#     
    def Suma_Digitos2(numeroEntero):
        digito1 = numeroEntero[0]
        digito2 = numeroEntero[1]

        operacion2 = int(digito1) + int(digito2)
        print("\n",digito1, "+", digito2, "=", operacion2)

        for numero2 in range(1, operacion2+1):
            print(numero2)
            if numero2 %3 == 0:
                if numero2 %5 == 0: print("FizzBuzz")
                else: print("Fizz")
            elif numero2 %5 == 0: print("Buzz")
    #--------------# Función 3 #--------------# 
    def Suma_Digitos3(numeroEntero):
        digito1 = numeroEntero[0]
        digito2 = numeroEntero[1]
        digito3 = numeroEntero[2]

        operacion3 = int(digito1) + int(digito2) + int(digito3)
        print("\n",digito1, "+", digito2, "+", digito3,"=", operacion3)

        for numero3 in range(1, operacion3+1):
            print(numero3)
            if numero3 %3 == 0:
                if numero3 %5 == 0: print("FizzBuzz")
                else: print("Fizz")
            elif numero3 %5 == 0: print("Buzz")
    #--------------# Función 4 #--------------#        
    def Suma_Digitos4(numeroEntero):
        digito1 = numeroEntero[0]
        digito2 = numeroEntero[1]
        digito3 = numeroEntero[2]
        digito4 = numeroEntero[3]

        operacion4 = int(digito1) + int(digito2) + int(digito3) + int(digito4)
        print("\n",digito1, "+", digito2, "+", digito3,"+", digito4,"=", operacion4)

        for numero4 in range(1, operacion4+1):
            print(numero4)
            if numero4 %3 == 0:
                if numero4 %5 == 0: print("FizzBuzz")
                else: print("Fizz")
            elif numero4 %5 == 0: print("Buzz")
    #--------------# Función 5 #--------------#     
    def Suma_Digitos5(numeroEntero):
        digito1 = numeroEntero[0]
        digito2 = numeroEntero[1]
        digito3 = numeroEntero[2]
        digito4 = numeroEntero[3]
        digito5 = numeroEntero[4]

        operacion5 = int(digito1) + int(digito2) + int(digito3) + int(digito4) + int(digito5)
        print("\n",digito1, "+", digito2, "+", digito3,"+", digito4,"+", digito5, "=", operacion5)

        print("""
*--------------*
|   FizzBuzz   |
*--------------*
""")
        for numero5 in range(1, operacion5+1):
            print(numero5)
            if numero5 %3 == 0:
                if numero5 %5 == 0: print("FizzBuzz")
                else: print("Fizz")
            elif numero5 %5 == 0: print("Buzz")
    #--------------# Función 6 #--------------#             
    def Suma_Digitos6(numeroEntero):
        digito1 = numeroEntero[0]
        digito2 = numeroEntero[1]
        digito3 = numeroEntero[2]
        digito4 = numeroEntero[3]
        digito5 = numeroEntero[4]
        digito6 = numeroEntero[5]

        operacion6 = int(digito1) + int(digito2) + int(digito3) + int(digito4) + int(digito5) + int(digito6)
        print("\n",digito1, "+", digito2, "+", digito3,"+", digito4,"+", digito5, digito6, "=", operacion6)

        print("""
*--------------*
|   FizzBuzz   |
*--------------*
""")
        for numero6 in range(1, operacion6+1):
            print(numero6)
            if numero6 %3 == 0:
                if numero6 %5 == 0: print("FizzBuzz")
                else: print("Fizz")
            elif numero6 %5 == 0: print("Buzz")
    #--------------# Función 7 #--------------#             
    def Suma_Digitos7(numeroEntero):
        digito1 = numeroEntero[0]
        digito2 = numeroEntero[1]
        digito3 = numeroEntero[2]
        digito4 = numeroEntero[3]
        digito5 = numeroEntero[4]
        digito6 = numeroEntero[5]
        digito7 = numeroEntero[6]

        operacion7 = int(digito1) + int(digito2) + int(digito3) + int(digito4) + int(digito5) + int(digito6) + int(digito7)
        print("\n",digito1, "+", digito2, "+", digito3,"+", digito4,"+", digito5, digito6, "+", digito7, "=", operacion7)

        print("""
*--------------*
|   FizzBuzz   |
*--------------*
""")
        for numero7 in range(1, operacion7+1):
            print(numero7)
            if numero7 %3 == 0:
                if numero7 %5 == 0: print("FizzBuzz")
                else: print("Fizz")
            elif numero7 %5 == 0: print("Buzz")
    #--------------# Función 8 #--------------#             
    def Suma_Digitos8(numeroEntero):
        digito1 = numeroEntero[0]
        digito2 = numeroEntero[1]
        digito3 = numeroEntero[2]
        digito4 = numeroEntero[3]
        digito5 = numeroEntero[4]
        digito6 = numeroEntero[5]
        digito7 = numeroEntero[6]
        digito8 = numeroEntero[7]

        operacion8 = int(digito1) + int(digito2) + int(digito3) + int(digito4) + int(digito5) + int(digito6) + int(digito7) + int(digito8)
        print("\n",digito1, "+", digito2, "+", digito3,"+", digito4,"+", digito5, digito6, "+", digito7, "+", digito8, "=", operacion8)

        print("""
*--------------*
|   FizzBuzz   |
*--------------*
""")
        for numero8 in range(1, operacion8+1):
            print(numero8)
            if numero8 %3 == 0:
                if numero8 %5 == 0: print("FizzBuzz")
                else: print("Fizz")
            elif numero8 %5 == 0: print("Buzz")
    #--------------# Función 9 #--------------#             
    def Suma_Digitos9(numeroEntero):
        digito1 = numeroEntero[0]
        digito2 = numeroEntero[1]
        digito3 = numeroEntero[2]
        digito4 = numeroEntero[3]
        digito5 = numeroEntero[4]
        digito6 = numeroEntero[5]
        digito7 = numeroEntero[6]
        digito8 = numeroEntero[7]
        digito9 = numeroEntero[8]

        operacion9 = int(digito1) + int(digito2) + int(digito3) + int(digito4) + int(digito5) + int(digito6) + int(digito7) + int(digito8) + int(digito9)
        print("\n",digito1, "+", digito2, "+", digito3,"+", digito4,"+", digito5, digito6, "+", digito7, "+", digito8,"+", digito9,"=", operacion9)

        print("""
*--------------*
|   FizzBuzz   |
*--------------*
""")
        for numero9 in range(1, operacion9+1):
            print(numero9)
            if numero9 %3 == 0:
                if numero9 %5 == 0: print("FizzBuzz")
                else: print("Fizz")
            elif numero9 %5 == 0: print("Buzz")
    #--------------# Función 10 #--------------#             
    def Suma_Digitos10(numeroEntero):
        digito1 = numeroEntero[0]
        digito2 = numeroEntero[1]
        digito3 = numeroEntero[2]
        digito4 = numeroEntero[3]
        digito5 = numeroEntero[4]
        digito6 = numeroEntero[5]
        digito7 = numeroEntero[6]
        digito8 = numeroEntero[7]
        digito9 = numeroEntero[8]
        digito10 = numeroEntero[9]

        operacion10 = int(digito1) + int(digito2) + int(digito3) + int(digito4) + int(digito5) + int(digito6) + int(digito7) + int(digito8) + int(digito9) + int(digito10)
        print("\n",digito1, "+", digito2, "+", digito3,"+", digito4,"+", digito5, digito6, "+", digito7, "+", digito8,"+", digito9,"+", digito10, "=", operacion10)

        print("""
*--------------*
|   FizzBuzz   |
*--------------*
""")
        for numero10 in range(1, operacion10+1):
            print(numero10)
            if numero10 %3 == 0:
                if numero10 %5 == 0: print("FizzBuzz")
                else: print("Fizz")
            elif numero10 %5 == 0: print("Buzz")
    #============================ Fin Funciones ============================#

    #============================ Llamando Funciones / Data basura ============================#
    """Documentación Llamanda de funciones:
    Aquí es para llamar las funciones dependiendo la cantidad de dígitos que el usuario entre.
    Hasta el momento sólo controlamos 10 digitos, ya que no quise estender el código mucho más.
    Aquí tengo condicionales que son las que se encargan de verificar la longitud de los dígitos, para así poder llamar a la función correcta para dicha cantidad de dígitos.
    Aquí también le tengo el mensaje de "Lo siento, no puedes introducir más de 10 digitos." para controlar cuando ponga más de 10 digitos.
    Fin Documentación llamada de funciones.
    
    En  la data basura controlo todo lo que no se necesita en el programa, como lo son caracteres especiales y letras, por lo que en el control me recive verdadero si es numero y falso si no lo es.
    Si lanza falso pues se quedara diciendole que es basura y que lo vuelva intentar, hasta que ponga un numero, o varios que es lo que se espera.
    """

    control2 = "a" # Lo utilizo para preguntarle algo, sin que se lo vuelva a repetir cuando salga del while de mayor o igual a 11.
    while True:
        if control2 != "x":
            numeroEntero = input("Número entero: \n> ")
            control1 = numeroEntero.isdigit()
        while True: # DATA BASURA
            if control1 == False:
                print("\nLo siento, no se acepta data basura.\nVuelve a intentarlo.")
                numeroEntero = input("\nNúmero entero: \n> ")
                control1 = numeroEntero.isdigit()
            else:
                break
        if len(numeroEntero) == 1: Suma_Digitos1(numeroEntero)
        elif len(numeroEntero) == 2: Suma_Digitos2(numeroEntero)
        elif len(numeroEntero) == 3: Suma_Digitos3(numeroEntero)
        elif len(numeroEntero) == 4: Suma_Digitos4(numeroEntero)
        elif len(numeroEntero) == 5: Suma_Digitos5(numeroEntero)
        elif len(numeroEntero) == 6: Suma_Digitos6(numeroEntero)
        elif len(numeroEntero) == 7: Suma_Digitos7(numeroEntero)
        elif len(numeroEntero) == 8: Suma_Digitos8(numeroEntero)
        elif len(numeroEntero) == 9: Suma_Digitos9(numeroEntero)
        elif len(numeroEntero) == 10: Suma_Digitos10(numeroEntero)
        elif len(numeroEntero) >= 11: 
            while len(numeroEntero) >= 11:
                print("Lo siento, no puedes introducir más de 10 digitos.\nIntente de nuevo.\n")
                numeroEntero = input("Número entero: \n> ")
                control2 = "x" # Lo utilizo para preguntarle algo, sin que se lo vuelva a repetir cuando salga del while de mayor o igual a 11.
                
            continue
        break
        
    
    #============================ Fin Llamando Funciones ============================#

    #========================== Agradecimiento por usar el programa =========================#  

    """
    Aquí imprimo por pantalla el agradecimiento y por quién fue creado, en este caso por mi.
    """

    print(em("""
*-----------------------------------------*
|  ¡Programa 10 Finalizado exitosamente! :smiling_face_with_smiling_eyes:|
*-----------------------------------------*
"""))
    # ========================== Fin Agradecimiento por usar el programa ========================= #