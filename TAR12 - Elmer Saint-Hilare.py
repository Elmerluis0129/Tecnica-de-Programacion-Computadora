"""
Escriba un programa con funciones definidas por usted, que realice lo siguiente:

Almacene una lista de 10 tuplas que correspondan a los siguientes viajeros de un aeropuerto. Nota: La estructura de los datos de cada viajero es Nombre, Edad, Destino:
Juan, 30, Madrid.
Fernanda, 42, Portugal.
Raúl, 28, Brazil.
Julio, 32, Venezuela.
Mateo, 26, Argentina.
María, 32, Portugal.
José, 29, Madrid.
Marcos, 29, Venezuela.
Juana, 41, Venezuela.
Paulina, 35, Madrid.
Muestre los destinos almacenados (sin repetir).
Devuelva una lista de diccionarios de los pasajeros cuyo destino sea el solicitado por teclado.
Si se coloca un destino que no se encuentra en los almacenados, el programa debe mostrar un mensaje diciendo: "No hay pasajeros para este destino".

Elmer Saint-Hilare 21-1354.
"""
ListaDestinos = ["Madrid", "Portugal", "Brazil", "Venezuela", "Argentina", "Portugal", "Madrid", "Venezuela", "Venezuela", "Madrid"]
ListaGeneral = [('Juan', 30, 'Madrid'), ('Fernanda', 42, 'Portugal'), ('Raúl', 28, 'Brazil'), ('Julio', 32, 'Venezuela'), ('Mateo', 26, 'Argentina'), ('María', 32, 'Portugal'), ('José', 29, 'Madrid'), ('Marcos', 29, 'Venezuela.'), ('Juana', 41, 'Venezuela'), ('Paulina', 35, 'Madrid')]
ListaDiccionario = [{'Nombre': 'Juan',
                     'Edad':30,
                     'Destino':'Madrid'
                     },{'Nombre': 'Fernanda',
                     'Edad':42,
                     'Destino':'Portugal'
                     },{'Nombre': 'Raúl',
                     'Edad':28,
                     'Destino':'Brazil'
                     },{'Nombre': 'Julio',
                     'Edad':32,
                     'Destino':'Venezuela'
                     },{'Nombre': 'Mateo',
                     'Edad':26,
                     'Destino':'Argentina'
                     },{'Nombre': 'María',
                     'Edad':32,
                     'Destino':'Portugal'
                     },{'Nombre': 'José',
                     'Edad':29,
                     'Destino':'Madrid'
                     },{'Nombre': 'Marcos',
                     'Edad':29,
                     'Destino':'Venezuela'
                     },{'Nombre': 'Juana',
                     'Edad':41,
                     'Destino':'Venezuela'
                     },{'Nombre': 'Paulina',
                     'Edad':35,
                     'Destino':'Madrid'
                     }]



def destino(x=0):
    Destinos = set(ListaDestinos)
    print("Destinos: ", Destinos)
    
def buscarPersona(a):
    if a in ListaDestinos:
        if a == 'Madrid':
            print("*-----------------------------*")
            print("|Pasajeros que van a: ", a,"|")
            print("*-----------------------------*\n")
            print(ListaDiccionario[0])
            print(ListaDiccionario[6])
            print(ListaDiccionario[9])

        elif a == 'Portugal':
            print("*-------------------------------*")
            print("|Pasajeros que van a: ", a,"|")
            print("*-------------------------------*\n")
            print(ListaDiccionario[1])  
            print(ListaDiccionario[5])
        elif a == 'Brazil':
            print("*-----------------------------*")
            print("|Pasajeros que van a: ", a,"|")
            print("*-----------------------------*\n")
            print(ListaDiccionario[2]) 
        elif a == 'Venezuela':
            print("*--------------------------------*")
            print("|Pasajeros que van a: ", a,"|")
            print("*--------------------------------*\n")
            print(ListaDiccionario[3])
            print(ListaDiccionario[7])
            print(ListaDiccionario[8])
        elif a == 'Argentina':
            print("*--------------------------------*")
            print("|Pasajeros que van a: ", a,"|")
            print("*--------------------------------*\n")
            print(ListaDiccionario[4]) 
            
                  
    else:
        print("\nLo siento, no hay pasajeros con destino a:", a)
       
destino()
buscarPersona(input("\nPasajero destino a: \n> "))

#========================== Agradecimiento por usar el programa =========================#  

"""
Aquí imprimo por pantalla el agradecimiento y por quién fue creado, en este caso por mi.
"""

print("""
*----------------------------------------------------------------------------*
| ¡Muchas gracias por utilizar mi programa! / By: Elmer Saint-Hilare 21-1354 |
*----------------------------------------------------------------------------*
""")
#========================== Fin Agradecimiento por usar el programa =========================#r usar el programa =========================#
#TODO RECORDAR DE DOCUMENTAR ANTES DE ENTREGAR EL PROGRAMA.