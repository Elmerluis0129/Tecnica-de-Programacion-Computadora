"""
Escriba un programa que pregunte al usuario los números de su ticket de lotería, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor. 
Elmer Saint-Hilare 21-1354
"""
def programa5 ():
    #Nombre del programa.
    print("""
*-----------------------------------------------*
|Ordenar de menor a mayor los números de lotería|
*-----------------------------------------------*
""")#Decorando el nombre de la aplicación.

    ListaNumLot = []
    x = 1
    
    numeroTicket = int(input("Ingrese la cantidad de números de su ticket\n> "))
    
    for i in range(1,numeroTicket+1):
        print("Ingrese el número",x,":")
        numerosDeTickets = int(input("> "))
        x = x + 1
        ListaNumLot.append(numerosDeTickets) 
    
    print("\nLista sin ordenar: ", ListaNumLot)#Lista normal sin ordenar.
    ListaNumLot.sort()#Función para ordenar la lista.
    print("Lista ordenada: ", ListaNumLot, ) #Lista ordenada.
    
    #========================== Agradecimiento por usar el programa =========================#  
    
    """
    Aquí imprimo por pantalla el agradecimiento y por quién fue creado, en este caso por mi.
    """
    
    print("""
*----------------------------------------------------------------------------*
|  ¡Programa 5 Finalizado exitosamente! / By: Elmer Saint-Hilare 21-1354     |
*----------------------------------------------------------------------------*
""")
#========================== Fin Agradecimiento por usar el programa =========================#