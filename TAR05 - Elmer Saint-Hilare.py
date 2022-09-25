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