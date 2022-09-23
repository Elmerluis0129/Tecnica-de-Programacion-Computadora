#Nombre del programa.
print("\n*--------------------*")#Decorando el nombre.
print("| Calculadora Básica |")
print("*--------------------*\n")#Decorando el nombre.
#Prueba

#Operaciones para mostrarle en pantalla las que tiene para poder elegir.
print("""\nOperaciones:\n
1.- Sumar\n
2.- Restar\n
3.- Multiplicar\n
4.- Dividir\n""")

#Para saber si el usuario quiere que le muestre las 4 operaciones con los mismos 2 números, o si quiere que le muestre el resultado con la operación que desea
modo = int(input("""¿Cómo quieres las respuesta/s? Responder con el número por favor.
\n1.- Que el programa te haga las 4 operaciones con los mismos números."""   #Aqui muestra los resultados de las 4 operaciones básicas.
"""\n2.- Que el programa te haga solo la operacion que selecciones.\n> """)) #Solo muestra el resultado de una operación ya seleccionada por el usuario.

#Si el usuario selecciona la opcion 2, hace la operacion que elija.
if modo == 2:
    print("\n*-------------------------------*")#Decorando los "Subtitulos"
    print("| Modo: Selección de operación. |")
    print("*-------------------------------*\n")#Decorando los "Subtitulos"
    #Eleccion de la operacion a realizar
    operacion = int(input("¿Qué operación desea realizar? / Responde con el número, por favor.\n> "))

    #Aquí lo utilizo para saber qué número me da el usuario y así identificar qué quiere el usuario hacer, si sumar, restar, multiplicar o dividir.
    #Operacion Sumar.
    if operacion == 1:
        print("\n*---------------------------------*")#Decorando la operación.
        print("| Haz elegido la operación: Sumar |")
        print("*---------------------------------*\n")#Decorando la operación.

        #Entrada de los numeros / Variables.
        num1 = float(input("Por favor, ingrese el primer número: "))#Numero 1.
        num2 = float(input("Por favor, ingrese el segundo número: "))#Numero 2.
        #Variable de la suma.
        Sumar = num1 + num2

        print("El resultado de:", num1,"+",num2,"=", Sumar)
    else:
        #Decorando los "Subtitulos"
        #Operacion Restar.
        if operacion == 2:
            print("\n*----------------------------------*")#Decorando los la operación.
            print("| Haz elegido la operación: Restar |")
            print("*----------------------------------*\n")#Decorando la operación.

            #Entrada de los numeros / Variables.
            num1 = float(input("Por favor, ingrese el primer número: "))#Numero 1.
            num2 = float(input("Por favor, ingrese el segundo número: "))#Numero 2.
            #Variable de la resta.
            Restar = num1 - num2

            print("El resultado de:", num1,"-",num2,"=", Restar)
        else:
            #Decorando los "Subtitulos"
            #Operacion Multiplicar.
            if operacion == 3:
                print("\n*---------------------------------------*")#Decorando la operación.
                print("| Haz elegido la operación: Multiplicar |")
                print("*---------------------------------------*\n")#Decorando la operación.

                #Entrada de los numeros / Variables.
                num1 = float(input("Por favor, ingrese el primer número: "))#Numero 1.
                num2 = float(input("Por favor, ingrese el segundo número: "))#Numero 2.
                #Variable de la Multiplicacion.
                Multiplicar = num1 * num2

                print("El resultado de:", num1,"*",num2,"=", Multiplicar)
            else:
                #Decorando los "Subtitulos"
                #Operacion Dividir.
                if operacion == 4:
                    print("\n*-----------------------------------*")#Decorando la operación.
                    print("| Haz elegido la operación: Dividir |\n*-----------------------------------*")#Decorando la operación.
                    print("Recuerda que el segundo número no puede ser igual a cero(0)\n")

                    #Entrada de los números / Variables.
                    num1 = float(input("Por favor, ingrese el primer número: "))#Numero 1.
                    num2 = float(input("Por favor, ingrese el segundo número: "))#Numero 2.

                    #Verificar si el denominador (Segundo numero) pone un 0.
                    if num2 == 0:
                        print("\n¡ERROR! Recuerda que no puedes poner cero(0) en el divisor(en el dividiendo)")#Error mas comprensible por un usuario.
                    else:
                        #Variable de la división.
                        Dividir = num1 / num2
                        print("El resultado de:", num1,"/",num2,"=", Dividir)
                else:
                    if operacion >= 5:
                        print("\nLo siento, debes introducir un número de las opciones que se te marcan al principio.") #Aqui el usuario pone una un numero mayor que las opciones que se les propone
                    else:
                        if operacion <= 0:
                            print("\nLo siento, debes introducir un número de las opciones que se te marcan al principio.") #Aqui el usuario pone una un numero menor que las opciones que se les propone

else:
    if modo == 1: #Si elije la opcion 1, el programa hace las 4 operaciones al mismo tiempo.
        print("\n*-----------------------------*")#Decorando el Modo.
        print("| Modo: Todas las operaciones |")
        print("*-----------------------------*\n")#Decorando el Modo.

        #Entrada de los numeros / Variables
        num1 = float(input("Por favor, ingrese el primer número: "))#Numero 1.
        num2 = float(input("Por favor, ingrese el segundo número: "))#Numero 2.

        #Operaciones.
        Sumar = num1+num2
        Restar = num1-num2
        Multiplicar = num1*num2
        Dividir = num1/num2

        #Condicion para saber si marca el cero como segundo número y asi le muestre un error que pueda entender.
        if num2 == 0:
            print("¡ERROR! Recuerda que no puedes dividir con cero(0)") #Error mas comprensible por un usuario.
        else:
            #Variable de la division.
            print("\nEl resultado en todas las operaciones es: \nSuma: ", num1,"+",num2,"=", Sumar, "\nResta: ", num1,"-",num2,"=", Restar, "\nMultiplicación: ", num1,"*",num2,"=", Multiplicar, "\nDivisión: ", num1,"/",num2,"=", Dividir)
            
    else:
        if modo >= 3:
            print("\nLo siento, este número no es uno de las opciones mostradas en pantalla.")
        else:
            if modo <= 0:
                print("\nLo siento, este número no es uno de las opciones mostradas en pantalla.")

#Agradecimiento por usar el programa.
print("\n*----------------------------------------------------------------------------*")#Decorando el agradecimiento.
print("| ¡Muchas gracias por utilizar mi programa! / By: Elmer Saint-Hilare 21-1354 |")
print("*----------------------------------------------------------------------------*\n")#Decorando el agradecimiento.
#FIN