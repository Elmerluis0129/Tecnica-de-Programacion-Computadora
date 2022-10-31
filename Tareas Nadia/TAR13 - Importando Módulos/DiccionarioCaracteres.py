"""
Diccionario de caracteres. Solicitar una cadena de caracteres y devolver un diccionario con la cantidad de apariciones de cada caracter (sin repetir) en la cadena. Si la cadena tiene espacios, el diccionario debe tener la clave 'espacio'.
Elmer Saint-Hilare 21-1354
"""
def diccionario():
    # ====== Variables generales ====== #
    """
    Aquí  tengo mi lista general, mi diccionario general y la variable donde almaceno la lista de caracteres.
    """
    ListaCaracteres1 = []
    Diccionario1 = {}
    cadenaCaracteres = input("Ingrese una cadena de caracteres: \n> ")
    # ==== Fin Variables generales ==== #
    
    # ============ Bucles FOR ============ #
    """
    Aquí en mis bucles for los utilizo para ir agregando y creando lo que necesite.
    También para recorrer una lista o diccionario la veces que necesite.
    """
    #----------- For 1 ------------- #
    """
    En el For 1 lo que hago es que agrego cada caracter de mi lista de caracteres a la lista 1.
    """
    
    for x in cadenaCaracteres:
        ListaCaracteres1.append(x)
            
    n = 0
    #--------- Fin For 1 ----------- #
    
    #----------- For 2 ------------- #
    """
    En el For 2 lo que hago es que cuento las veces que a (cada caracter) que se encuentra en la lista 1 aparece, me lo guarde en una variable.
    luego le pongo condicionales, que si tiene espacio pues que me agregue a mi diccionario 1 la palabra "espacio" junto a las veces que se repite el espacio en la lista de caracteres.
    
    si no lo que anda recorriendo en el momento no es un espacio, entonces que me agregue al diccionario el caracter junto a las veces que aparece el mismo.
    """
    
    for a in ListaCaracteres1:
        VecesRepite = ListaCaracteres1.count(a)
    
        if a == ' ':
            Diccionario1.update(
                {
                    'espacio':VecesRepite
                }
                
            )
          
        else:
            
            Diccionario1.update(
                {
                    a:VecesRepite
                }
            
            )
    #--------- Fin For 2 ----------- #
    
    # ========== Fin Bucles FOR ========== #
    
    # ===== Impresión por pantalla ===== #
    """
    Aquí ya imprimo mi diccionario ya formulado por mi bucle for adecuadamente.
    """
    print(Diccionario1)
    # === Fin Impresión por pantalla === #
    print("\n¡Programa 1 finalizado con éxito!")