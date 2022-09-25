#Escriba un programa que pregunte al usuario los números de su ticket de lotería, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor. 
#Elmer Saint-Hilare 21-1354

#Nombre del programa.
print("""
*-----------------------------------------------*
|Ordenar de menor a mayor los números de lotería|
*-----------------------------------------------*
\n""")#Decorando el nombre de la aplicación.

ListaNumLot = []
x = 1

#Variables a utilizar.
ListaNumLot = [] #Lista donde almaceno los números.
x = 1 #Variable con la que puedo ir aumentando de 1 en 1 y poder mostrarle el mandato correcto al usuario.

#Aquí es para saber la cantidad de números de ticket que el usuario tiene.
TipoDeTicket = int(input("""Ingrese la cantidad de números que tiene su ticket de lotería.
Recuerde contarlos por espacios, ejemplo: 04 12 73 ahí tiene 3 números.
> """))

if TipoDeTicket == 1:
    for numero in range(1):
        if x == 1: #Aquí para la primera iteración tendrá un valor de 1 la x, por lo que le pondrá el 1er mandato.
            ListaNumLot.append(int(input("Ingresar el primer número de lotería de su ticket. \n> ")))
        break
    
elif TipoDeTicket == 2:
    for numero in range(2):
        if x == 1: #Aquí para la primera iteración tendrá un valor de 1 la x, por lo que le pondrá el 1er mandato.
            ListaNumLot.append(int(input("Ingresar el primer número de lotería de su ticket. \n> ")))
        elif x == 2: #Aquí para la segunda iteración tendrá un valor de 2 la x, por lo que le pondrá el 2do mandato.
            ListaNumLot.append(int(input("Ingresar el segundo número de lotería de su ticket. \n> ")))
            break
        x=x+1

elif TipoDeTicket == 3:
    for numero in range(3):
        if x == 1: #Aquí para la primera iteración tendrá un valor de 1 la x, por lo que le pondrá el 1er mandato.
            ListaNumLot.append(int(input("Ingresar el primer número de lotería de su ticket. \n> ")))
        elif x == 2: #Aquí para la segunda iteración tendrá un valor de 2 la x, por lo que le pondrá el 2do mandato.
            ListaNumLot.append(int(input("Ingresar el segundo número de lotería de su ticket. \n> ")))
        elif x == 3: #Aquí para la tercera iteración tendrá un valor de 3 la x, por lo que le pondrá el 2do mandato.
            ListaNumLot.append(int(input("Ingresar el tercer número de lotería de su ticket. \n> ")))
            break
        x=x+1

elif TipoDeTicket == 4:
    for numero in range(4):
        if x == 1: #Aquí para la primera iteración tendrá un valor de 1 la x, por lo que le pondrá el 1er mandato.
            ListaNumLot.append(int(input("Ingresar el primer número de lotería de su ticket. \n> ")))
        elif x == 2: #Aquí para la segunda iteración tendrá un valor de 2 la x, por lo que le pondrá el 2do mandato.
            ListaNumLot.append(int(input("Ingresar el segundo número de lotería de su ticket. \n> ")))
        elif x == 3: #Aquí para la tercera iteración tendrá un valor de 3 la x, por lo que le pondrá el 2do mandato.
            ListaNumLot.append(int(input("Ingresar el tercer número de lotería de su ticket. \n> ")))
        elif x == 4: #Aquí para la cuarta iteración tendrá un valor de 4 la x, por lo que le pondrá el 2do mandato.
            ListaNumLot.append(int(input("Ingresar el cuarto número de lotería de su ticket. \n> ")))
            break
        x=x+1
        
elif TipoDeTicket == 5:
    for numero in range(5):
        if x == 1: #Aquí para la primera iteración tendrá un valor de 1 la x, por lo que le pondrá el 1er mandato.
            ListaNumLot.append(int(input("Ingresar el primer número de lotería de su ticket. \n> ")))
        elif x == 2: #Aquí para la segunda iteración tendrá un valor de 2 la x, por lo que le pondrá el 2do mandato.
            ListaNumLot.append(int(input("Ingresar el segundo número de lotería de su ticket. \n> ")))
        elif x == 3: #Aquí para la tercera iteración tendrá un valor de 3 la x, por lo que le pondrá el 2do mandato.
            ListaNumLot.append(int(input("Ingresar el tercer número de lotería de su ticket. \n> ")))
        elif x == 4: #Aquí para la cuarta iteración tendrá un valor de 4 la x, por lo que le pondrá el 2do mandato.
            ListaNumLot.append(int(input("Ingresar el cuarto número de lotería de su ticket. \n> ")))
        elif x == 5: #Aquí para la quinta iteración tendrá un valor de 5 la x, por lo que le pondrá el 2do mandato.
            ListaNumLot.append(int(input("Ingresar el quinto número de lotería de su ticket. \n> ")))
        break #Esto sirve para cuanddo vaya por la 5ta iteración y se cumpla la condición el bucle for se rompa, terminando por completo con las iteraciones.
        x = x+1 #Este es la magia del bucle, aquí la variable x irá aumentando su valor de 1 en 1, por lo que es lo que ayuda a que cada condición se vaya cumpliendo según aumente el valor de x.
    
else:
    for numero in range(TipoDeTicket):
        ListaNumLot.append(int(input("Ingresar el número de su ticket. \n> "))) #TODO Poner a que muestre la lista ordenada de menor a mayor.

#Estas condiciones es para mostrarle los mandatos necesarios según marqué la cantidad de números de ticket que tiene.
if TipoDeTicket == 1:#Aquí sólo tiene un sólo número de ticket.
    for numero in range(1):#Aquí para que me iteré 1 vez.
        if x == 1: #Aquí para la primera iteración tendrá un valor de 1 la x, por lo que le pondrá el 1er mandato.
            ListaNumLot.append(int(input("Ingresar el primer número de lotería de su ticket. \n> ")))#Mandato 1.
        break#Esto sirve para cuanddo vaya por la 1ra iteración y se cumpla la condición el bucle for se rompa, terminando por completo con las iteraciones.
    
elif TipoDeTicket == 2:#Aquí sólo tiene dos números de ticket.
    for numero in range(2):#Aquí para que me iteré 2 veces.
        if x == 1: #Aquí para la primera iteración tendrá un valor de 1 la x, por lo que le pondrá el 1er mandato.
            ListaNumLot.append(int(input("Ingresar el primer número de lotería de su ticket. \n> ")))#Mandato 1.
        elif x == 2: #Aquí para la segunda iteración tendrá un valor de 2 la x, por lo que le pondrá el 2do mandato.
            ListaNumLot.append(int(input("Ingresar el segundo número de lotería de su ticket. \n> ")))#Mandato 2.
            break#Esto sirve para cuanddo vaya por la 2da iteración y se cumpla la condición el bucle for se rompa, terminando por completo con las iteraciones.
        x=x+1

elif TipoDeTicket == 3:#Aquí sólo tiene tres números de ticket.
    for numero in range(3):#Aquí para que me iteré 3 veces.
        if x == 1: #Aquí para la primera iteración tendrá un valor de 1 la x, por lo que le pondrá el 1er mandato.
            ListaNumLot.append(int(input("Ingresar el primer número de lotería de su ticket. \n> ")))#Mandato 1.
        elif x == 2: #Aquí para la segunda iteración tendrá un valor de 2 la x, por lo que le pondrá el 2do mandato.
            ListaNumLot.append(int(input("Ingresar el segundo número de lotería de su ticket. \n> ")))#Mandato 2.
        elif x == 3: #Aquí para la tercera iteración tendrá un valor de 3 la x, por lo que le pondrá el 2do mandato.
            ListaNumLot.append(int(input("Ingresar el tercer número de lotería de su ticket. \n> ")))#Mandato 3.
            break#Esto sirve para cuanddo vaya por la 3ra iteración y se cumpla la condición el bucle for se rompa, terminando por completo con las iteraciones.
        x=x+1

elif TipoDeTicket == 4:#Aquí sólo tiene cuatro números de ticket.
    for numero in range(4):#Aquí para que me iteré 4 veces.
        if x == 1: #Aquí para la primera iteración tendrá un valor de 1 la x, por lo que le pondrá el 1er mandato.
            ListaNumLot.append(int(input("Ingresar el primer número de lotería de su ticket. \n> ")))#Mandato 1.
        elif x == 2: #Aquí para la segunda iteración tendrá un valor de 2 la x, por lo que le pondrá el 2do mandato.
            ListaNumLot.append(int(input("Ingresar el segundo número de lotería de su ticket. \n> ")))#Mandato 2.
        elif x == 3: #Aquí para la tercera iteración tendrá un valor de 3 la x, por lo que le pondrá el 2do mandato.
            ListaNumLot.append(int(input("Ingresar el tercer número de lotería de su ticket. \n> ")))#Mandato 3.
        elif x == 4: #Aquí para la cuarta iteración tendrá un valor de 4 la x, por lo que le pondrá el 2do mandato.
            ListaNumLot.append(int(input("Ingresar el cuarto número de lotería de su ticket. \n> ")))#Mandato 4.
            break#Esto sirve para cuanddo vaya por la 4ta iteración y se cumpla la condición el bucle for se rompa, terminando por completo con las iteraciones.
        x=x+1
        
elif TipoDeTicket == 5:#Aquí sólo tiene cinco números de ticket.
    for numero in range(5): #Aquí para que me iteré 5 veces.
        if x == 1: #Aquí para la primera iteración tendrá un valor de 1 la x, por lo que le pondrá el 1er mandato.
            ListaNumLot.append(int(input("Ingresar el primer número de lotería de su ticket. \n> ")))#Mandato 1.
        elif x == 2: #Aquí para la segunda iteración tendrá un valor de 2 la x, por lo que le pondrá el 2do mandato.
            ListaNumLot.append(int(input("Ingresar el segundo número de lotería de su ticket. \n> ")))#Mandato 2.
        elif x == 3: #Aquí para la tercera iteración tendrá un valor de 3 la x, por lo que le pondrá el 2do mandato.
            ListaNumLot.append(int(input("Ingresar el tercer número de lotería de su ticket. \n> ")))#Mandato 3.
        elif x == 4: #Aquí para la cuarta iteración tendrá un valor de 4 la x, por lo que le pondrá el 2do mandato.
            ListaNumLot.append(int(input("Ingresar el cuarto número de lotería de su ticket. \n> ")))#Mandato 4.
        elif x == 5: #Aquí para la quinta iteración tendrá un valor de 5 la x, por lo que le pondrá el 2do mandato.
            ListaNumLot.append(int(input("Ingresar el quinto número de lotería de su ticket. \n> ")))#Mandato 5.
            break #Esto sirve para cuanddo vaya por la 5ta iteración y se cumpla la condición el bucle for se rompa, terminando por completo con las iteraciones.
        x = x+1 #Este es la magia del bucle, aquí la variable x irá aumentando su valor de 1 en 1, por lo que es lo que ayuda a que cada condición se vaya cumpliendo según aumente el valor de x.
    
else:#Aquí sólo tiene 6 o más números de ticket.
    for numero in range(TipoDeTicket):#Aquí para que me iteré de 6 a la cantidad que el usuario especifique.
        ListaNumLot.append(int(input("Ingresar el número de su ticket. \n> ")))#Aquí le mostrará el mismo mensaje a diferencia de lo anterior las veces necesarias.
        
print("\nLa lista creada con los números de tu ticket de loteria es: ", ListaNumLot)#Lista normal sin ordenar.
ListaNumLot.sort()#Función para ordenar la lista.
print("\nEl orden de menor a mayor en la lista creada con tus números de tickets es: ", ListaNumLot, "\n") #Lista ordenada.

#Agradecimiento por usar el programa.
print("""\n
*----------------------------------------------------------------------------*
| ¡Muchas gracias por utilizar mi programa! / By: Elmer Saint-Hilare 21-1354 |
*----------------------------------------------------------------------------*
\n""")#Decorando el agradecimiento.
#FIN