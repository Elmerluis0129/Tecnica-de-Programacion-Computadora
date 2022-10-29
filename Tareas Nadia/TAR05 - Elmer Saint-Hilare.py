"""
Escriba un programa que pregunte al usuario los números de su ticket de lotería, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor. 
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

#Nombre del programa.
print("""
*-----------------------------------------------*
|Ordenar de menor a mayor los números de lotería|
*-----------------------------------------------*
""")#Decorando el nombre de la aplicación.

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
        ListaNumLot.append(int(input("Ingresar el número de su ticket. \n> "))) 

print("La lista creada con los números de tu ticket de loteria es: ", ListaNumLot)#Lista normal sin ordenar.
ListaNumLot.sort()#Función para ordenar la lista.
print("El orden de menor a mayor en la lista creada con tus números de tickets es: ", ListaNumLot, ) #Lista ordenada.

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