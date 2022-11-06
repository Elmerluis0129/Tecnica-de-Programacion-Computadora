print("*****************************")
print("*Vacaciones por Departamento*")
print("*****************************")
print()

nombre = input("Ingresa el nombre del empleado: ")
Dep = input("Ingresa el departamento de trabajo del empleado: ")

#DEPARTAMENTO DE ATENCIÓN AL CLIENTE

if Dep == "Dep.AtencionCliente":
    clave_uno = int(input("Ingresa la clave del empleado: "))

    if clave_uno != 1630:
        print("Clave de departamento no existe, vuelve a intentarlo.")
    if clave_uno == 1630:
        print()
        print("***********************************************************************************************************")
        print("*Para recibir vacaciones el empleado debe cumplir con el requisito de tener un año laborando con nosotros.*")
        print("***********************************************************************************************************")
        print()
        
        
        cant_año = float(input("Ingresa la cantidad de años que ha laborado el empleado " + nombre + ": "))
        if cant_año < 1:
            print("Lo siento, al empleado: " + nombre + ", le falta cumplir el año como minimo para poder recibir vacaciones")
        elif cant_año == 1 and cant_año < 2:
            print("El empleado tiene derecho a 6 días de vacaciones.")
        elif cant_año >= 2 and cant_año <= 6:
            print("El empleado tiene derecho a 14 días de vacaciones.")
        elif cant_año >= 7 and cant_año <= 12:
            print("El empleado tiene derecho a 20 días de vacaciones.")
        elif cant_año >= 12 and cant_año <= 20:
            print("El empleado tiene derecho a 30 días de vacaciones.")
        elif cant_año > 21 and cant_año <= 30:
            print("El empleado tiene derecho a ser pencionado.")
        else:
            print("Lo siento, el empleado no puede tener más de 30 años laborando con nosotros físicamente")

#DEPARTAMENTO DE LOGISTICA
    
if Dep == "Dep.Logistica":
    clave_dos = int(input("Ingresa la clave del empleado: "))

    if clave_dos != 2910:
        print("Clave de departamento no existe, vuelve a intentarlo.")
    if clave_dos == 2910:
        print()
        print("***********************************************************************************************************")
        print("*Para recibir vacaciones el empleado debe cumplir con el requisito de tener un año laborando con nosotros.*")
        print("***********************************************************************************************************")
        print()

        cant_año = float(input("Ingresa la cantidad de años que ha laborado el empleado " + nombre + ": "))
        if cant_año < 1:
            print("Lo siento, al empleado: " + nombre + ", le falta cumplir el año como minimo para poder recibir vacaciones")
        elif cant_año == 1 and cant_año < 2:
            print("El empleado tiene derecho a 7 días de vacaciones.")
        elif cant_año >= 2 and cant_año <= 6:
            print("El empleado tiene derecho a 15 días de vacaciones.")
        elif cant_año >= 7 and cant_año <= 12:
            print("El empleado tiene derecho a 22 días de vacaciones.")
        elif cant_año >= 12 and cant_año <= 20:
            print("El empleado tiene derecho a 36 días de vacaciones.")
        elif cant_año > 21 and cant_año <= 30:
            print("El empleado tiene derecho a ser pencionado.")
        else:
            print("Lo siento, el empleado no puede tener más de 30 años laborando con nosotros físicamente")

#DEPARTAMENTO DE GERENCIA
 
if Dep == "Dep.Gerencia":
    clave_tres = int(input("Ingresa la clave del empleado: "))

    if clave_tres != 3912:
        print("Clave de departamento no existe, vuelve a intentarlo.")
    if clave_tres == 3912:
        print()
        print("***********************************************************************************************************")
        print("*Para recibir vacaciones el empleado debe cumplir con el requisito de tener un año laborando con nosotros.*")
        print("***********************************************************************************************************")
        print()
        
        cant_año = float(input("Ingresa la cantidad de años que ha laborado el empleado " + nombre + ": "))
        if cant_año < 1:
            print("Lo siento, al empleado: " + nombre + ", le falta cumplir el año como minimo para poder recibir vacaciones")
        elif cant_año == 1 and cant_año < 2:
            print("El empleado tiene derecho a 10 días de vacaciones.")
        elif cant_año >= 2 and cant_año <= 6:
            print("El empleado tiene derecho a 20 días de vacaciones.")
        elif cant_año >= 7 and cant_año <= 12:
            print("El empleado tiene derecho a 30 días de vacaciones.")
        elif cant_año >= 12 and cant_año <= 20:
            print("El empleado tiene derecho a 45 días de vacaciones.")
        elif cant_año > 21 and cant_año <= 30:
            print("El empleado tiene derecho a ser pencionado.")
        else:
            print("Lo siento, el empleado no puede tener más de 30 años laborando con nosotros físicamente")







