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

ListaTuplasViajeros = [
    ('Juan', 30, 'Madrid'), 
    ('Fernanda', 42, 'Portugal'), 
    ('Raúl', 28, 'Brazil'), 
    ('Julio', 32, 'Venezuela'), 
    ('Mateo', 26, 'Argentina'), 
    ('María', 32, 'Portugal'), 
    ('José', 29, 'Madrid'), 
    ('Marcos', 29, 'Venezuela'), 
    ('Juana', 41, 'Venezuela'), 
    ('Paulina', 35, 'Madrid')
]
Diccionario = []
ListaDestinos = []

for clave in ListaTuplasViajeros:
    Diccionario.append(
        {
            "Nombre": clave[0],
            "Edad": clave[1],
            "Destino": clave[2]
        }
    )
    ListaDestinos.append(
        clave[2]
    )
    

def BuscarPasajeroDestino(n):
    m = 1
    if n in ListaDestinos:
        print("\nPasajeros que van para {}:\n".format(n))
        for clave in ListaTuplasViajeros:
            if clave[2] == n:
                Diccionario2 = {
                        "Nombre": clave[0],
                        "Edad": clave[1],
                        "Destino": clave[2]
                     }    
                print("|{}.|".format(m), Diccionario2)
                m = m + 1      
    else:
        print("\n¡Lo siento! No hay pasajeros con destino a '{}'.".format(n))
    

def destino(x=0):
    Destinos = set(ListaDestinos)
    print("\nDestinos: {}".format(Destinos))
    print("\nIngrese el destino para saber quien va a viajar para el mismo.")
    BuscarPasajeroDestino(input("\nDestino: \n> "))
    

destino()

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