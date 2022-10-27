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
def programa12():

    #Nombre del programa.
    print("""
*-----------------------------------------------*
|        Buscar viajero según su destino        |
*-----------------------------------------------*
""")#Decorando el nombre de la aplicación.

# ============== Lista con los viajeros =============== #
    """
    Aquí almaceno la lista de tuplas con la informacion de los usuarios.
    """
    ListaTuplasViajeros = [
        ('Juan'    , 30, 'Madrid'), 
        ('Fernanda', 42, 'Portugal'), 
        ('Raúl'    , 28, 'Brazil'), 
        ('Julio'   , 32, 'Venezuela'), 
        ('Mateo'   , 26, 'Argentina'), 
        ('María'   , 32, 'Portugal'), 
        ('José'    , 29, 'Madrid'), 
        ('Marcos'  , 29, 'Venezuela'), 
        ('Juana'   , 41, 'Venezuela'), 
        ('Paulina' , 35, 'Madrid')
    ]
    # ============ Fin Lista con los viajeros ============= #

    # ===== Listas Generales ===== #
    """
    En estas listas procedo mas adelante a convertirlas segun lo necesite.
    Aquí guardo tanto los destinos como la informacion de cada pasajero.
    """
    Diccionario = []
    ListaDestinos = []
    # === Fin Listas Generales === #

    # ==== For - Creando Diccionario / Destinos ==== #
    """
    Aquí voy pasando la informacion de la lista de tuplas a un diccionario, indicando el nombre, edad y destino.
    Y aquí también agrego de la lista de tuplas solamente los destinos en la lista creada anteriormente.
    """
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
    # == Fin For - Creando Diccionario / Destinos == #

    # =================== Funciones ======================= #
    """
    Aquí con las funciones en la primera lo que hago es verificar si el destino ingresado por teclado es igual a uno de la lista ya mostrada.
    SI lo es entonces me reccorre las tuplas una vez mas y me verifica si la clave posicion 2 (Destino) es igual o no al destino seleccionado por el usuario
    Si lo es entonces me crea un diccionario con esa informacion, tanto asi que solo me crea un diccionario con los usuarios que coinciden con el destino buscado.

    Si el destino ingresado no esta en la lista, procede a mostrarle un mesanje avisandole que dicho destino no hay pasajero que vayan para el mismo.

    En la segunda función me encargo de la lista anterior de destinos que tenia, me ignora todas las repetidas ya que la paso de lista a set.
    Luego me imprime esos destinos.
    """
    def BuscarPasajeroDestino(n):
        m = 0
        if n in ListaDestinos:
            print("\nPasajeros que van para {}:\n".format(n))
            for clave in ListaTuplasViajeros:
                if clave[2] == n:
                    Diccionario2 = {
                            "Nombre": clave[0],
                            "Edad": clave[1],
                            "Destino": clave[2]
                         }   
                    m = m + 1     
                    print("|{}.|".format(m), Diccionario2)
            if m == 1:
                print("\nSe encontró: {} pasajero.".format(m)) 
            else:
                print("\nSe encontraron: {} pasajeros.".format(m))  
        else:
            print("\n¡Lo siento! No hay pasajeros con destino a '{}'.".format(n))


    def destino(x=0):
        Destinos = set(ListaDestinos)
        print("\nDestinos: {}".format(Destinos))
        print("\nIngrese el destino para saber quien va a viajar para el mismo.")


    # ================= Fin Funciones ===================== #

    # ============ Llamada Funciones ============ #
    """
    Aquí es donde llamo mis funciones con el orden correspondiente.
    """
    destino() 
    BuscarPasajeroDestino(input("\nDestino: \n> "))
    # ========== Fin Llamada Funciones ========== #

    #========================== Agradecimiento por usar el programa =========================#  

    """
    Aquí imprimo por pantalla el agradecimiento y por quién fue creado, en este caso por mi.
    """

    print("""
*----------------------------------------------------------------------------*
|  ¡Programa 12 Finalizado exitosamente! / By: Elmer Saint-Hilare 21-1354    |
*----------------------------------------------------------------------------*
""")
#========================== Fin Agradecimiento por usar el programa =========================#