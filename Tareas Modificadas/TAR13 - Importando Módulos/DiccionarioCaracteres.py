"""
Diccionario de caracteres. Solicitar una cadena de caracteres y devolver un diccionario con la cantidad de apariciones de cada caracter (sin repetir) en la cadena. Si la cadena tiene espacios, el diccionario debe tener la clave 'espacio'.
Elmer Saint-Hilare 21-1354
"""




ListaCaracteres1 = []
ListaCaracteres2 = []
Diccionario1 = {}

cadenaCaracteres = input("Ingrese una cadena de caracteres: \n> ")




for x in cadenaCaracteres:
    ListaCaracteres1.append(x)
        
n = 0
    
for x in ListaCaracteres1:
    VecesRepite = ListaCaracteres1.count(x)

    if x == ' ':
        Diccionario1.update(
            {
                'espacio':VecesRepite
            }
            
        )
      
    else:
        
        Diccionario1.update(
            {
                x:VecesRepite
            }
        
        )

print(Diccionario1)