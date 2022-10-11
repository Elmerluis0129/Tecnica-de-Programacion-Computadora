#Escribir un programa que imprima la tabla de multiplicar de un numero ingresado por teclado.
#Elmer Saint-Hilare 21-1354

print("""
*--------------------*  
|Tabla de multiplicar|
*--------------------*
\n""")#Decoración.


numeroUsuario = int(input("Escribe un número: ")) #Número que le pide al usuario para que imprima la tabla del mismo.
print("\n\n")#Saltos de líneas.

#Variables que me van a permitir aumentar su valor más adelante y poder realizar lo que quiero.
x = 0 #Con esta me sirve para hacer posible la multiplicacion con los numeros del 0 al 10. Ejemplo: 7*x vendría siendo 7*0 y así el valor irá cambiando para multiplicar del 0 al 10.
j = 0 #Con esté me sirve para decorar, no tiene mucho valor en el programa, solo funciona para decorar con las líneas identificadas con "#Decoración".

while x <= 10: #Función while(mientras) sirve para generar tanto las lineas de decoración, como la multiplicación y también para aumentar el valor de mis variables x y j.
    operacion = numeroUsuario * x #Operación que se tiene que repetir según cambie el valor de x.
    if j == 0: #Aquí lo uso para que sólo me imprima el título una vez, sin importar cuántas vueltas de while.
        print("Tabla de multiplicar del ",numeroUsuario)#Título
    elif j == 9:#Esto es para decorar la multiplicación por 9 de x número y para obviamente mostrarme la operación del mismo.
        print("*--------------*")#Decoración.
        print("|",numeroUsuario,"*",x, "=", operacion, "|") #Esto es para imprimir la operación en sí de cuando multiplica el número que entra el usuario por el valor de x, en este caso sería 9.
    elif j == 10:#Esto es para decorar la multiplicación por 10 de x número y para obviamente mostrarme la operación del mismo.
        print("*---------------*")#Decoración.
        print("|",numeroUsuario,"*",x, "=", operacion, "|")#Esto es para imprimir la operación en sí de cuando multiplica el número que entra el usuario por el valor de x, en este caso sería 10.
    else:#Aquí ya lo uso para que me haga la operación y la decoración de la misma cuando la variable x tiene un valor del 0 al 8.
        print("*-------------*")#Decoración.
        print("|",numeroUsuario,"*",x, "=", operacion, "|")#Esto es para imprimir la operación en sí de cuando multiplica el número que entra el usuario por el valor de x, en este caso sería del 1 al 8.

    #Aquí es dónde aumento de 1 en 1 mis variables para ejecutar las líneas que especifiqué en las condiciones.
    x = x + 1
    j = j + 1
    
print("*---------------*\n") #Decoración.

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