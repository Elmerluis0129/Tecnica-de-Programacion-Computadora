#Utilizando break y continue.
#break sirve para romper el ciclo o bucle.
#continue sirve para continuar el ciclo o bucle, ignorando por completo toda linea de codigo que tenga en la misma tabulacion debajo del mismo.

print("**********************************************")
print("* while con la sentencia break y continue \n *")
print("**********************************************")

contador = 0

while contador <= 149:
    contador+=1
    print("El valor actual de la variable es: ", contador)

    if contador == 10:
        print()
        print("¡ERROR! El programa se ha parado.\n")
        respuesta = input("¿Deseas reparar el programa? Si o No: ")

        if respuesta == "No":
            print("Cancelando proceso y terminando.")
            print("El programa ha terminado correctamente.")
            break
        elif respuesta == "Si":
            print("Programa reparado, continuando el proceso: \n")
            continue
        elif respuesta != "Si" or respuesta != "No":
            print("Lo siento, la respuesta está mal escrita, favor intentarlo de nuevo.\n")
            respuesta = input("¿Deseas reparar el programa? Si o No: ")
            while respuesta != "Si" or respuesta != "No":
                print("Lo siento, la respuesta está mal escrita, favor intentarlo de nuevo.\n")
                respuesta = input("¿Deseas reparar el programa? Si o No: ")
                
                if respuesta == "Si" or respuesta == "No":
                    break
                
            respuesta = input("¿Deseas volver a continuar el programa donde se detuvo? Si o No: ")
            if respuesta == "No":
                print("Cancelando proceso y terminando.")
                print("El programa ha terminado correctamente.")
                break
            elif respuesta == "Si":
                print("Continuando el programa: \n")
                continue
            
            continue

    if contador == 100:
        print()
        print("¡ERROR! El programa se ha parado.\n")
        respuesta = input("¿Deseas reparar el programa? Si o No: ")

        if respuesta == "No":
            print("Cancelando proceso y terminando.")
            print("El programa ha terminado correctamente.")
            break
        elif respuesta == "Si":
            print("Programa reparado, continuando el proceso: \n")
            continue
        elif respuesta != "Si" or respuesta != "No":
            print("Lo siento, la respuesta está mal escrita, favor intentarlo de nuevo.\n")
            respuesta = input("¿Deseas reparar el programa? Si o No: ")
            while respuesta != "Si" or respuesta != "No":
                print("Lo siento, la respuesta está mal escrita, favor intentarlo de nuevo.\n")
                respuesta = input("¿Deseas reparar el programa? Si o No: ")
                
                if respuesta == "Si" or respuesta == "No":
                    break
                
            respuesta = input("¿Deseas volver a continuar el programa donde se detuvo? Si o No: ")
            if respuesta == "No":
                print("Cancelando proceso y terminando.")
                print("El programa ha terminado correctamente.")
                break
            elif respuesta == "Si":
                print("Continuando el programa: \n")
                continue
            
            continue

                    
            
                
            
        

    


