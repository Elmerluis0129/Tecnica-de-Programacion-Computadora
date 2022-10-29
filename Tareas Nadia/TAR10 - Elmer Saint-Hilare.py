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

"""
En la funcion fizzbuzz le tengo que me haga el juego de fizz buzz, donde tengo un for que me realiza los numeros del 1 hasta la 1+suma

Tengo condicionales para que imprima fizz cuando es divisor de 3, buzz cuando es de 5, y fizzbuzz cuando es de ambos.
"""
def FizzBuzz(j):
    
    print("""
*--------------*
|   FizzBuzz   |
*--------------*
""")
    for n in range(1, operacion+1):
        print(n)
        if n %3 == 0:
            if n %5 == 0:
                print(fb)
            else:
                print(f)
        elif n %5 == 0:
                print(b)
        
                
"""
En la funcion Suma_Digitos le tengo que me haga la suma de los digitos del numero entero.
primero los convierto a string con la entrada de teclado, luego los asigno a variables individuales.
y luego declaro una variable que me haga la operacion de las dos variables de mis digitos, pero los paso de str a int para hacer la operacion
tengo que cuando termine todo me llame a la funcion fizzbuzz
"""
    

def Suma_Digitos(x):
    global operacion, digito1, digito2
    digito1 = x[0]
    digito2 = x[1]
    operacion = int(digito1) + int(digito2)
    print("\n",digito1, "+", digito2, "=", operacion)
    
    FizzBuzz(0)

"""
Aqui declaro mis variables globales, que uso en las funciones
Aqui tambien hago el llamado de la funcion suma_digitos. 
"""
x = str(input("Número entero: \n> "))
f = "Fizz"
b = "Buzz"
fb = "FizzBuzz"
Suma_Digitos(x)


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