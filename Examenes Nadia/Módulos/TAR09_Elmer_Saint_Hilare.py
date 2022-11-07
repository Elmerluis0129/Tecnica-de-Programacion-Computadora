"""
Escriba un programa que, mediante una función, dada una cadena de caracteres (sin espacios), muestre el primer caracter que no se repite.
Ejemplo:
Ingrese una cadena de caracteres: aaabbbcdddefefef
El primer caracter que no se repite es: c
Elmer Saint-Hilare 21-1354
"""
from emoji import emojize as em # Esto no es parte del ejercicio, es decoración.

def programa9 ():
    #============ Nombre programa ===========#
    """
    Aquí es para imprimir el nombre del programa.
    """
    print("""
*------------------------*  
|Primero que no se repite|
*------------------------*
""")
#============ Fin Nombre programa ===========#

#========================== Función ==========================#
    """
    Aquí defino la función, la cual llamo luego para que me ejecute lo que tiene dentro.

    Dentro de la función tengo variables para ir midiendo la longitud de la cadena de caracteres.
    También tengo una condicional if para controlar los espacios, para que no ingrese espacios los usuarios.
    Luego tengo un while donde me ejecute ese código dentro mientras la longitud 2 sea diferente de la longitud 1 menos 1.
    Dentro del while tengo que cada vez que se iteree, me cambie el valor de la longitud 1 si es necesario, luego al primer caracter lo reemplazo con "", luego cambio longitud 2 si es necesario.
    Dentro del while también tengo otra condicional que es la que decide si imprimirme el primer carácter que no se repite, o si me dice que todos se repiten y termina el while.

    Lo que hace la magia aquí es que donde tengo el (pcnsr = pcnsr.replace(pcnsr[x], "") que basicamente me va eliminando todas los caracteres repetidos, entonces cuando queda la unica que no está repetida, ahí ya el condicional se encarga de decir que esa es la primera que no se repite.

    """

    #---------------------------- Función 1 ----------------------------#
    def primer_Caracter_no_se_repite(pcnsr):
        if " " in pcnsr:
            print("\nFavor no introducir espacios.\nVuelva a intentarlo.\n")
            primer_Caracter_no_se_repite(input("Ingrese la cadena de caracteres: \n>"))
        elif not " " in pcnsr:
            while True: 
                cadenaCaracteresLongitud = len(pcnsr) 
                primerCaracterRepetido = pcnsr[0]
                pcnsr = pcnsr.replace(pcnsr[0], "")
                cadenaCaracteresLongitud2 = len(pcnsr)
                if cadenaCaracteresLongitud2 == cadenaCaracteresLongitud-1: 
                    print ("\nEl primer carácter que no se repite es: ", primerCaracterRepetido, "\n")
                    break
        else:
            print("Lo siento, vuelve a intentarlo.")
    # ========================== Fin Función 1 ========================== #

    # ========================== Llamada Función ========================== # 
    """
    Aquí lo uso para llamar la función.
    También pongo que la entrada de la función sea una entrada de teclado, para que la lista de caracteres la introduzca el usuario.
    """       
    primer_Caracter_no_se_repite(input("Ingrese la cadena de caracteres: \n>"))
    # ========================== Fin Llamada Función ========================== #    

    # ========================== Agradecimiento por usar el programa ========================= #  

    """
    Aquí imprimo por pantalla el agradecimiento y por quién fue creado, en este caso por mi.
    """

    print(em("""
*-----------------------------------------*
|  ¡Programa 9 Finalizado exitosamente! :smiling_face_with_smiling_eyes:|
*-----------------------------------------*
"""))
    # ========================== Fin Agradecimiento por usar el programa ========================= #