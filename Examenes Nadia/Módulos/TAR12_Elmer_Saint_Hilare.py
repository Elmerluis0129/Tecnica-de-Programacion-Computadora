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

Elmer Saint-Hilare 21-1354. # Nombre del creador
"""
from emoji import emojize as em # Esto no es parte del ejercicio, es decoración.

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
        ('Juan'    , 30, 'Madrid'   ), 
        ('Fernanda', 42, 'Portugal' ), 
        ('Raúl'    , 28, 'Brazil'   ), 
        ('Julio'   , 32, 'Venezuela'), 
        ('Mateo'   , 26, 'Argentina'), 
        ('María'   , 32, 'Portugal' ), 
        ('José'    , 29, 'Madrid'   ), 
        ('Marcos'  , 29, 'Venezuela'), 
        ('Juana'   , 41, 'Venezuela'), 
        ('Paulina' , 35, 'Madrid'   )
    ]
    # ============ Fin Lista con los viajeros ============= #

    # ===== Listas Generales ===== #
    """
    En esta lista procedo mas adelante a convertirlas segun lo necesite.
    Aquí guardo tanto los destinos como la informacion de cada pasajero.
    """
    ListaDestinos = []
    # === Fin Listas Generales === #

    # ==== For - Creando Diccionario / Destinos ==== #
    """
    Aquí voy pasando la informacion de la lista de tuplas a un diccionario, indicando el nombre, edad y destino.
    Y aquí también agrego de la lista de tuplas solamente los destinos en la lista creada anteriormente.
    """
    for clave in ListaTuplasViajeros:
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
    def BuscarPasajeroDestino(Destino):
        acumulador = 0
        while True:
            if Destino in ListaDestinos:
                print(f"\nPasajeros que van para {Destino}:\n")
                for clave in ListaTuplasViajeros:
                    if clave[2] == Destino:
                        Diccionario2 = {
                                "Nombre": clave[0],
                                "Edad": clave[1],
                                "Destino": clave[2]
                             }   
                        acumulador += 1     
                        print(f"|{acumulador}.|", Diccionario2)
                if acumulador == 1:
                    print(f"\nSe encontró: {acumulador} pasajero.") 
                else:
                    print(f"\nSe encontraron: {acumulador} pasajeros.")  
            else:
                while True: # DATA BASURA
                    if Destino in ListaDestinos: 
                        break
                    else:
                        print(f"\n¡Lo siento! No hay pasajeros con destino a '{Destino}'.")
                        Destino = input("\nDestino: \n> ")
                        
                        if Destino in ListaDestinos:
                            BuscarPasajeroDestino(Destino)
                        else:
                            continue
            break

                
                


    def destino():
        Destinos = set(ListaDestinos)
        print(f"\nDestinos: {Destinos}")
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

    print(em("""
*-----------------------------------------*
|  ¡Programa 12 Finalizado exitosamente! :smiling_face_with_smiling_eyes:|
*-----------------------------------------*
"""))
#========================== Fin Agradecimiento por usar el programa =========================#