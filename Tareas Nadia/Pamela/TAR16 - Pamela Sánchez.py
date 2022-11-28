#Usando Programación Orientada a Objetos, escribir un programa que permita registrar n películas con los siguientes datos:

#Nombre.
#Categoría. (Deben estar predefinidas en una clase Categoría).
#Director.
#Año lanzamiento.
#Cantidad de taquillas vendidas.
#Luego, generar un archivo de texto plano (.txt) con las películas que se hayan registrado. La estructura de este archivo debe ser la siguiente (datos de ejemplo)

#Indicaciones:

#Se debe solicitar la cantidad de películas.
#Las clases deben estar en archivos separados (Película y Categoría).
#Deben existir categorías previamente definidas (las que usted desee).
#Al momento de indicar la categoría de una película, se debe elegir de las que ya existan.
#Incluir una opción que permita generar un archivo .csv con las películas que tengan un total de taquillas >= 2,000
#Se deben controlar las excepciones (data basura) haciendo uso de try-except.

#Pamela Sánchez 21-1727

class Peliculas():
     
    contador = True
    while contador:    
        try:
            Pelis = int(input("Peliculas que quiere registrar: "))
            opcionArchivo = int(input("Quiere un archivo csv? 1 para Sí y 2 para No: "))
            contador = False
        except ValueError:
            print("\nLo siento, no se acepta data basura.\n")
            continue
    contador1 = 0
    print("""
Categorías  
1- Horror            
2- Drama             
3- Comedia           
4- Otras categoria""")

    m = open("Archivo texto plano.txt", "a")
    m.write("nombre|categoría|director|año|taquillas vendidas")
    m.write("\n")
    m.close()
    
    while contador1 != Pelis:

        m = open("Archivo texto plano.txt", "a")
        nombre = input("Nombre de la pelicula que quiere registrar: ")
        m.write(nombre)
        m.write("|")
        while True:
            categoria = input("Categoría: ")
            if categoria == "1":
                m.write("Horror")
                m.write("|")
                
            elif categoria == "2":
                m.write("Drama")
                m.write("|")
                
            elif categoria == "3":
                m.write("Comedia")
                m.write("|")
                
            elif categoria == "4":
                m.write("Otras categoria")
                m.write("|")
                
            else: 
                print("\nLo siento, no se acepta data basura, mire bien el menu.\n")
                continue
            break
                
        director = input("Director: ")
        m.write(director)
        m.write("|")
        while True:
            try:
                año = int(input("Año lanzamiento: "))
                taquillas = int(input("Taquillas vendidas: "))
                m.write(str(año))
                m.write("|")
                m.write(taquillas)
                m.write("\n")
                break
            except ValueError:
                print("\nVuelva intentarlo.\n")
                continue
            
            
            
        if opcionArchivo == "1":
            m2 = open("Peliculas taquillas 2000.csv", "a")
            m2.write("nombre,categoría,director,año,taquillas vendidas")
            m2.write("\n")
            if taquillas >= 2000:
                m2.write(nombre)
                m2.write(",")
                while True:
                    
                    if categoria == "1":
                        m2.write("Horror")
                        m2.write(",")

                    elif categoria == "2":
                        m2.write("Drama")
                        m2.write(",")

                    elif categoria == "3":
                        m2.write("Comedia")
                        m2.write(",")

                    elif categoria == "4":
                        m2.write("Otras categoria")
                        m2.write(",")
                    else: 
                        print("\nLo siento, no se acepta data basura, mire bien el menu.\n")
                        continue
                    break
                m2.write(director)
                m2.write(",")
                m2.write(str(año))
                m2.write(",")
                m2.write(taquillas)
            
                
            m2.close()

        contador1 += 1
        
    m.close()