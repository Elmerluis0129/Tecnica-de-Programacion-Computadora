# Escriba una función que reciba 2 listas de productos (de forma dinámica), y retorne un conjunto (Set) de los productos comunes 
# en las mismas. En caso de que no hayan productos comunes, retornar: "No hay productos comunes en las listas".
# Elmer Saint-Hilare 21-1354

print("""
*---------------------------------------*  
|Productos en comunes entre listas(sets)|
*---------------------------------------*
""")

# ======== Variables generales (Listas) ========= #
"""
Variables Generales.
Aquí podemos apreciar las dos listas ya declaradas. Lista 1 y Lista 2.
"""
Lista1 = []
Lista2 = []
# ======== Fin Variables generales (Listas) ========= #

# ==================== Funciones ==================== #
"""
Aquí es dónde tengo las funciones que me van preguntando los productos, la cantidad de los mismos.
Aquí también agrego los productos a las listas correspondientes.

El while es para que me lo ejecute las veces n necesarias.
El for es para ir imprimiendo los productos de la listas.
En la ultima funcion es donde identifico si hay o no productos comunes entre listas.
"""

# ------------ Función 1 ------------ #
def ListaUno(x):
    j = 0
    m = 0
    print("\n================== Lista Uno ==================\n")
    while x != j:
        producto = input("""
*--------------------*
|Ingrese el producto:| 
*--------------------*
> """)
        Lista1.append(producto)
        j = j + 1
        
    print("\nCantidad de producto lista 1: ", len(Lista1))
    
    for e in Lista1:
        print("\nProducto: ", Lista1[m])
        m = m + 1
    
    print("\nLista 1: ", Lista1)
# ------------ Fin Función 1 ------------ #
          
# ------------ Función 2 ------------ #
def ListaDos(n):
    j = 0
    m = 0
    print("\n================== Lista Dos ==================\n")
    while n != j:
        producto = input("""
*--------------------*
|Ingrese el producto:| 
*--------------------*
> """)
        Lista2.append(producto)
        j = j + 1
        
    print("\nCantidad de producto lista 2: ", len(Lista2))
    
    for e in Lista2:
        print("\nProducto: ", Lista2[m])
        m = m + 1

    print("\nLista 2: ", Lista2)

# ------------ Fin Función 2 ------------ #

# ------------ Función 3 ------------ #    
def ProductoComunes(l):
    
    if len(l) >= 1:
        print("\n========= Producto comunes en ambas listas =========")
        print("\nProducto comunes: ", l)
    else:
        print("\nNo hay productos comunes en las listas.")
# ------------ Fin Función 3 ------------ #
    
# ==================== Fin Funciones ==================== #

# ==================== Llamada Funciones ==================== #
"""
Aquí llamo las funciones para que lleven acabo dichos códigos que tienen dentro.
"""

ListaUno(int(input("\nIngrese la cantidad de producto lista 1: \n> ")))
ListaDos(int(input("\nIngrese la cantidad de producto lista 2: \n> ")))
# =========== Conversión de lista a sets =========== #
"""
Aquí Convierto mis listas a set para luego encontrar los prodcutos comunes entre ellas con el comando de los conjuntos .intersections
"""
convirtiendo1 = set(Lista1)
convirtiendo2 = set(Lista2)
# =========== Fin Conversión de lista a sets =========== #
ProductoComunes(convirtiendo1.intersection(convirtiendo2))
# ==================== Fin Llamada Funciones ==================== #

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
#TODO Recuerda resolver que te diga los productos iguales y retornar que no hay si no los hay.