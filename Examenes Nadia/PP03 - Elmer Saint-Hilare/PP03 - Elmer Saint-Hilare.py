"""
Examen Final - Sistema PowerGames
Valor: 100ptos.

Mediante el uso de Programación Orientada a Objetos, desarrollar un pequeño sistema que permita el mantenimiento de las ventas de videojuegos de PowerGames.

Indicaciones:

El sistema debe tener un menú de opciones que permita la interacción con el mismo.
El sistema debe realizar las 4 operaciones de un CRUD (Create, Read, Update, Delete) para las siguientes clases (modelos):
Clientes.
Videojuegos.
Ventas.
El sistema debe permitir la carga y la exportación de data a través de archivos .csv (para todos los modelos).
El sistema debe tener una opción que permita generar un archivo .csv con los videojuegos cuyas ventas sean mayores a RD$500.00.

Elmer Saint-Hilare 21-1354
"""

import PP03_Clientes as Cls
import PP03_Ventas as Vns
import PP03_VideoJuegos as VJs

ListaClientes = []
ListaActualizar = []
ListaActualizar1 = []
ListaActualizar2 = []
ListaActualizar3 = []
ListaActualizar4 = []
ListaActualizar5 = []
ListaActualizarAuxiliar = []


def MenuPrincipal():
    print(
"""
  Menú Principal
*----------------*
|1.| Clientes
|2.| Videojuegos
|3.| Ventas
*----------------*
""")
MenuPrincipal()

def Leer(c, control1, control2, control3, control4, control5):
    if c:
        contador1 = 0
        contador2 = 0
        contador3 = 0
        contador4 = 1
        prueba = 1
        while True:
            contador1 += 3
            contador2 += 4

            if len(ListaClientes) == contador2:
                global operacion
                operacion = contador2-contador1
                print(f"Se encontraron: {operacion} cliente/s.\n")
                for x in range((contador2-contador1)+1):
                    if prueba:
                        print("""       Cedula  |  Nombre   |  Apellido  |  Metodo de Pago""")
                        prueba = 0
                    else:
                        print("*---*------------------------------------------------------------*")
                        print(f"|{contador4}.-|",ListaClientes[contador3], ListaClientes[contador3+1], ListaClientes[contador3+2], ListaClientes[contador3+3])
                        contador3 += 4
                        contador4 += 1
                print("*---*------------------------------------------------------------*")
                print("""
   Menú CRUD
*--------------*
|1.| Crear
|2.| Leer
|3.| Actualizar
|4.| Eliminar
*--------------*""")
                Menus(0)
            elif len(ListaClientes) == 0:
                print("""\nNo hay data creada para 'Clientes'. Vuelva a intentarlo más tarde, por favor.\n
   Menú CRUD
*--------------*
|1.| Crear
|2.| Leer
|3.| Actualizar
|4.| Eliminar
*--------------*""")
                Menus(0)

# =========== AÑADIENDO LAS ACTUALIZACIONES ============ #
    if not c:
        ListaActualizarAuxiliar = ListaClientes.copy()
        ListaClientes.clear()
        if operacion == 1:
            # ============= Cliente 1 ============= #
            if control1: ListaClientes.append(ListaActualizar1[0]) ,ListaClientes.append(ListaActualizar1[1]) ,ListaClientes.append(ListaActualizar1[2]) ,ListaClientes.append(ListaActualizar1[3])
            else: ListaClientes.append(ListaActualizarAuxiliar[0]),ListaClientes.append(ListaActualizarAuxiliar[1]),ListaClientes.append(ListaActualizarAuxiliar[2]),ListaClientes.append(ListaActualizarAuxiliar[3])
            
        elif operacion == 2:
            # ============= Cliente 1 ============= #
            if control1: ListaClientes.append(ListaActualizar1[0]) ,ListaClientes.append(ListaActualizar1[1]) ,ListaClientes.append(ListaActualizar1[2]) ,ListaClientes.append(ListaActualizar1[3])
            else: ListaClientes.append(ListaActualizarAuxiliar[0]),ListaClientes.append(ListaActualizarAuxiliar[1]),ListaClientes.append(ListaActualizarAuxiliar[2]),ListaClientes.append(ListaActualizarAuxiliar[3])
                
            # ============= Cliente 2 ============= #
            if control2: ListaClientes.append(ListaActualizar2[0]) ,ListaClientes.append(ListaActualizar2[1]) ,ListaClientes.append(ListaActualizar2[2]) ,ListaClientes.append(ListaActualizar2[3])
            else: ListaClientes.append(ListaActualizarAuxiliar[4]),ListaClientes.append(ListaActualizarAuxiliar[5]),ListaClientes.append(ListaActualizarAuxiliar[6]),ListaClientes.append(ListaActualizarAuxiliar[7])
                
        elif operacion == 3:
            # ============= Cliente 1 ============= #
            if control1: ListaClientes.append(ListaActualizar1[0]) ,ListaClientes.append(ListaActualizar1[1]) ,ListaClientes.append(ListaActualizar1[2]) ,ListaClientes.append(ListaActualizar1[3])
            else: ListaClientes.append(ListaActualizarAuxiliar[0]),ListaClientes.append(ListaActualizarAuxiliar[1]),ListaClientes.append(ListaActualizarAuxiliar[2]),ListaClientes.append(ListaActualizarAuxiliar[3])
            
            # ============= Cliente 2 ============= #
            if control2: ListaClientes.append(ListaActualizar2[0]) ,ListaClientes.append(ListaActualizar2[1]) ,ListaClientes.append(ListaActualizar2[2]) ,ListaClientes.append(ListaActualizar2[3])
            else: ListaClientes.append(ListaActualizarAuxiliar[4]),ListaClientes.append(ListaActualizarAuxiliar[5]),ListaClientes.append(ListaActualizarAuxiliar[6]),ListaClientes.append(ListaActualizarAuxiliar[7])
            
            # ============= Cliente 3 ============= #    
            if control3: ListaClientes.append(ListaActualizar3[0]) ,ListaClientes.append(ListaActualizar3[1]) ,ListaClientes.append(ListaActualizar3[2]) ,ListaClientes.append(ListaActualizar3[3])
            else: ListaClientes.append(ListaActualizarAuxiliar[8]),ListaClientes.append(ListaActualizarAuxiliar[9]),ListaClientes.append(ListaActualizarAuxiliar[10]),ListaClientes.append(ListaActualizarAuxiliar[11])
                
        elif operacion == 4:
            # ============= Cliente 1 ============= #
            if control1: ListaClientes.append(ListaActualizar1[0]) ,ListaClientes.append(ListaActualizar1[1]) ,ListaClientes.append(ListaActualizar1[2]) ,ListaClientes.append(ListaActualizar1[3])
            else: ListaClientes.append(ListaActualizarAuxiliar[0]),ListaClientes.append(ListaActualizarAuxiliar[1]),ListaClientes.append(ListaActualizarAuxiliar[2]),ListaClientes.append(ListaActualizarAuxiliar[3])
            
            # ============= Cliente 2 ============= #
            if control2: ListaClientes.append(ListaActualizar2[0]) ,ListaClientes.append(ListaActualizar2[1]) ,ListaClientes.append(ListaActualizar2[2]) ,ListaClientes.append(ListaActualizar2[3])
            else: ListaClientes.append(ListaActualizarAuxiliar[4]),ListaClientes.append(ListaActualizarAuxiliar[5]),ListaClientes.append(ListaActualizarAuxiliar[6]),ListaClientes.append(ListaActualizarAuxiliar[7])
            
            # ============= Cliente 3 ============= #    
            if control3: ListaClientes.append(ListaActualizar3[0]) ,ListaClientes.append(ListaActualizar3[1]) ,ListaClientes.append(ListaActualizar3[2]) ,ListaClientes.append(ListaActualizar3[3])
            else: ListaClientes.append(ListaActualizarAuxiliar[8]),ListaClientes.append(ListaActualizarAuxiliar[9]),ListaClientes.append(ListaActualizarAuxiliar[10]),ListaClientes.append(ListaActualizarAuxiliar[11])
            
            # ============= Cliente 4 ============= #    
            if control4: ListaClientes.append(ListaActualizar4[0]) ,ListaClientes.append(ListaActualizar4[1]) ,ListaClientes.append(ListaActualizar4[2]) ,ListaClientes.append(ListaActualizar4[3])
            else: ListaClientes.append(ListaActualizarAuxiliar[12]),ListaClientes.append(ListaActualizarAuxiliar[13]),ListaClientes.append(ListaActualizarAuxiliar[14]),ListaClientes.append(ListaActualizarAuxiliar[15])
                
        elif operacion == 5:
            # ============= Cliente 1 ============= #
            if control1: ListaClientes.append(ListaActualizar1[0]) ,ListaClientes.append(ListaActualizar1[1]) ,ListaClientes.append(ListaActualizar1[2]) ,ListaClientes.append(ListaActualizar1[3])
            else: ListaClientes.append(ListaActualizarAuxiliar[0]),ListaClientes.append(ListaActualizarAuxiliar[1]),ListaClientes.append(ListaActualizarAuxiliar[2]),ListaClientes.append(ListaActualizarAuxiliar[3])
            
            # ============= Cliente 2 ============= #
            if control2: ListaClientes.append(ListaActualizar2[0]),ListaClientes.append(ListaActualizar2[1]),ListaClientes.append(ListaActualizar2[2]),ListaClientes.append(ListaActualizar2[3])
            else: ListaClientes.append(ListaActualizarAuxiliar[4]),ListaClientes.append(ListaActualizarAuxiliar[5]),ListaClientes.append(ListaActualizarAuxiliar[6]),ListaClientes.append(ListaActualizarAuxiliar[7])
            
            # ============= Cliente 3 ============= #    
            if control3: ListaClientes.append(ListaActualizar3[0]) ,ListaClientes.append(ListaActualizar3[1]) ,ListaClientes.append(ListaActualizar3[2]) ,ListaClientes.append(ListaActualizar3[3])
            else: ListaClientes.append(ListaActualizarAuxiliar[8]),ListaClientes.append(ListaActualizarAuxiliar[9]),ListaClientes.append(ListaActualizarAuxiliar[10]),ListaClientes.append(ListaActualizarAuxiliar[11]) 
               
            # ============= Cliente 4 ============= #    
            if control4: ListaClientes.append(ListaActualizar4[0]),ListaClientes.append(ListaActualizar4[1]),ListaClientes.append(ListaActualizar4[2]),ListaClientes.append(ListaActualizar4[3])
            else: ListaClientes.append(ListaActualizarAuxiliar[12]),ListaClientes.append(ListaActualizarAuxiliar[13]),ListaClientes.append(ListaActualizarAuxiliar[14]),ListaClientes.append(ListaActualizarAuxiliar[15])
            
            # ============= Cliente 5 ============= #
            if control5: ListaClientes.append(ListaActualizar5[0]),ListaClientes.append(ListaActualizar5[1]),ListaClientes.append(ListaActualizar5[2]),ListaClientes.append(ListaActualizar5[3])
            else: ListaClientes.append(ListaActualizarAuxiliar[16]),ListaClientes.append(ListaActualizarAuxiliar[17]),ListaClientes.append(ListaActualizarAuxiliar[18]),ListaClientes.append(ListaActualizarAuxiliar[19])
                
# =========== FIN AÑADIENDO LAS ACTUALIZACIONES ============ #

        
def Menus(a):
    if a:
        print(
"""
   Menú CRUD
*--------------*
|1.| Crear
|2.| Leer
|3.| Actualizar
|4.| Eliminar
*--------------*

       Menú adicional
*---------------------------*
|1.-| Carga-Exportacion CSV
|2.-| Videojuegos Ventas CSV 
*---------------------------*
""")

    def elegirOpcionEnMenu(x, y):
        while True:
            try:
# ---------------------------------------------------------------- CLIENTES MENU 1 ---------------------------------------------------------------- #
                if x == 1 and y == 1: # CONFIGURACION MENU 1 EN CLIENTES
                    eleccionCRUD = int(input("¿Qué desea hacer?\n> "))
                    if eleccionCRUD == 0:
                        print(f"Lo siento, el '{eleccionCRUD}' no se encuentra en el menú. \n")
                    elif eleccionCRUD >= 1 and eleccionCRUD <= 4:
# ================================================================== Crear =================================================================== #
                        if eleccionCRUD == 1:
                            contador = 0
                            while True:
                                try:
                                    CantidadClientes = int(input("Cantidad de clientes a ingresar: \n> "))
                                    break
                                except ValueError:
                                    print("No aceptamos data basuta.")
                                    continue
                                
                            while True:
                                try:
                                    while CantidadClientes != contador:
                                        cedula = int(input("Ingrese su identificación personal (ID): \n>"))
                                        cedulaModificada = str(cedula)
                                        nombre = input("Ingrese su/s nombre/s:")
                                        apellido = input("Ingrese su/s apellido/s:")
                                        print("\n'1' para pagar con tarjeta de crédito o débito. '2' para pagar en efectivo.")
                                        metodoPago = input("Ingrese su método de pago:")
                                        if metodoPago == "1":
                                            clientes = Cls.Clientes(cedulaModificada, nombre, apellido, "Tarjeta de crédito o débito")
                                        elif metodoPago == "2":
                                            clientes = Cls.Clientes(cedulaModificada, nombre, apellido, "Efectivo")
                                        ListaClientes.append(clientes.cedula_clientes)
                                        ListaClientes.append(clientes.nombre_clientes)
                                        ListaClientes.append(clientes.apellido_clientes)
                                        ListaClientes.append(clientes.metodoPago_clientes)
                                        
                                        contador += 1
                                    break
                                except ValueError:
                                    print("Lo siento, no aceptamos data basura.\n")
                                    continue
                                
# ================================================================== LEER =================================================================== #
                        elif eleccionCRUD == 2:
                            if len(ListaClientes) == 0:
                                print("\nNo hay data creada para 'Clientes'. Vuelva a intentarlo más tarde, por favor.\n")
                                print(
"""
   Menú CRUD
*--------------*
|1.| Crear
|2.| Leer
|3.| Actualizar
|4.| Eliminar
*--------------*""")
                                elegirOpcionEnMenu(x,y)
                            else:
                                Leer(1,0,0,0,0,0)
                            
# ================================================================== Actualizar =================================================================== #
                        elif eleccionCRUD == 3:
                            print("¿Quieres primero leer la data para saber cuál vas a actualizar? '1' para Sí y '0' para No")
                            while True:
                                eleccionData = int(input("> "))
                                if eleccionData:
                                    Leer(1,0,0,0,0,0)
                                else:
                                    contador = 0
                                    control1 = 0
                                    control2 = 0
                                    control3 = 0
                                    control4 = 0
                                    control5 = 0
                                    
                                    while True:
                                            
                                        contador += 1
                                        
                                        print("\nPara dejar de actualizar y guardar todas las actualizaciones, presionar: '6'")
                                        eleccionUsuarioActualizar = int(input("¿Cuál quieres actualizar?\nIngresa el número: "))
                                        
#===================================================================================ACTUALIZACION CLIENTE 1==================================================================================================================================== #
                                        if eleccionUsuarioActualizar == 1:
                                            print(f"El usuario seleccionado es: {ListaClientes[0]} {ListaClientes[1]} {ListaClientes[2]} {ListaClientes[3]}")
                                            print("¿Seguro que quieres actualizar este usuario?\n '1' para Sí y '0' para No.")
                                            respuestaSioNo = int(input("> "))
                                            while respuestaSioNo:
                                                if respuestaSioNo:
                                                    print("|1.-| Cédula\n|2.-| Nombre\n|3.-| Apellidos\n|4.-| Método de pag\n|5.-| Dejar actualizar")
                                                    UsuarioQuiereActualizarEl = input(f"¿Qué quiere actualizar del usuario {eleccionUsuarioActualizar}?\n> ")
                                                    
                                                    if UsuarioQuiereActualizarEl == "1": # ACTUALIZAR CEDULA DEL CLIENTE
                                                        print(f"Ha seleccionado el usuario {eleccionUsuarioActualizar}, para actualizar la cédula.\n")
                                                        nuevaCedula = int(input("Ingrese la nueva cédula: "))
                                                        NuevaCedulaEnString = str(nuevaCedula)
                                                        ListaActualizar1.append(NuevaCedulaEnString)
                                                        ListaActualizar1.append(ListaClientes[1])
                                                        ListaActualizar1.append(ListaClientes[2])
                                                        ListaActualizar1.append(ListaClientes[3])
                                                        print(f"Cédula actualizada éxitosamente...\nUsuario: {ListaActualizar1[0]} {ListaActualizar1[1]} {ListaActualizar1[2]} {ListaActualizar1[3]}")
                                                        control1 = 1

                                                    elif UsuarioQuiereActualizarEl == "2": # ACTUALIZAR NOMBRE DEL CLIENTE
                                                        print(f"Ha seleccionado el usuario {eleccionUsuarioActualizar}, para actualizar el nombre.\n")
                                                        nuevoNombre = input("Ingrese el nuevo nombre: ")
                                                        ListaActualizar1.append(ListaClientes[0])
                                                        ListaActualizar1.append(nuevoNombre)
                                                        ListaActualizar1.append(ListaClientes[2])
                                                        ListaActualizar1.append(ListaClientes[3])
                                                        print(f"Nombre actualizado éxitosamente...\nUsuario: {ListaActualizar1[0]} {ListaActualizar1[1]} {ListaActualizar1[2]} {ListaActualizar1[3]}")
                                                        control1 = 1
                                                                                                                
                                                    elif UsuarioQuiereActualizarEl == "3": # ACTUALIZAR APELLIDO DEL CLIENTE
                                                        print(f"Ha seleccionado el usuario {eleccionUsuarioActualizar}, para actualizar el apellido.\n")
                                                        nuevoApellido = input("Ingrese el nuevo apellido: ")
                                                        ListaActualizar1.append(ListaClientes[0])
                                                        ListaActualizar1.append(ListaClientes[1])
                                                        ListaActualizar1.append(nuevoApellido)
                                                        ListaActualizar1.append(ListaClientes[3])
                                                        print(f"Apellido actualizado éxitosamente...\nUsuario: {ListaActualizar1[0]} {ListaActualizar1[1]} {ListaActualizar1[2]} {ListaActualizar1[3]}")
                                                        control1 = 1
                                                                                                                
                                                    elif UsuarioQuiereActualizarEl == "4": # ACTUALIZAR MÉTODO DEL CLIENTE
                                                        print(f"Ha seleccionado el usuario {eleccionUsuarioActualizar}, para actualizar el método de pago.\n")
                                                        nuevoMetodo = input("Ingrese el nuevo método. '1' para pagar con tarjeta de crédito o débito. '2' para pagar en efectivo.\n> ")
                                                        if nuevoMetodo == "1":
                                                            nuevoMetodoActualizado = "Tarjeta de crédito o débito"
                                                        elif nuevoMetodo == "2":
                                                            nuevoMetodoActualizado = "Efectivo"                                                            
                                                        ListaActualizar1.append(ListaClientes[0])
                                                        ListaActualizar1.append(ListaClientes[1])
                                                        ListaActualizar1.append(ListaClientes[2])
                                                        ListaActualizar1.append(nuevoMetodoActualizado)
                                                        print(f"Método de pago actualizado éxitosamente...\nUsuario: {ListaActualizar1[0]} {ListaActualizar1[1]} {ListaActualizar1[2]} {ListaActualizar1[3]}")
                                                        control1 = 1
                                                        
                                                    elif UsuarioQuiereActualizarEl == "5":
                                                        break
                                
#===================================================================================ACTUALIZACION CLIENTE 2==================================================================================================================================== #

                                        elif eleccionUsuarioActualizar == 2:
                                            print(f"El usuario seleccionado es: {ListaClientes[4]} {ListaClientes[5]} {ListaClientes[6]} {ListaClientes[7]}")
                                            print("¿Seguro que quieres actualizar este usuario?\n '1' para Sí y '0' para No.")
                                            respuestaSioNo = int(input("> "))
                                            while respuestaSioNo:
                                                if respuestaSioNo:
                                                    print("|1.-| Cédula\n|2.-| Nombre\n|3.-| Apellidos\n|4.-| Método de pag\n|5.-| Dejar actualizar")
                                                    UsuarioQuiereActualizarEl = input(f"¿Qué quiere actualizar del usuario {eleccionUsuarioActualizar}?\n> ")
                                                    
                                                    if UsuarioQuiereActualizarEl == "1": # ACTUALIZAR CEDULA DEL CLIENTE
                                                        print(f"Ha seleccionado el usuario {eleccionUsuarioActualizar}, para actualizar la cédula.\n")
                                                        nuevaCedula = int(input("Ingrese la nueva cédula: "))
                                                        NuevaCedulaEnString = str(nuevaCedula)
                                                        ListaActualizar2.append(NuevaCedulaEnString)
                                                        ListaActualizar2.append(ListaClientes[5])
                                                        ListaActualizar2.append(ListaClientes[6])
                                                        ListaActualizar2.append(ListaClientes[7])
                                                        print(f"Cédula actualizada éxitosamente...\nUsuario: {ListaActualizar2[0]} {ListaActualizar2[1]} {ListaActualizar2[2]} {ListaActualizar2[3]}")
                                                        control2 = 1

                                                    elif UsuarioQuiereActualizarEl == "2": # ACTUALIZAR NOMBRE DEL CLIENTE
                                                        print(f"Ha seleccionado el usuario {eleccionUsuarioActualizar}, para actualizar el nombre.\n")
                                                        nuevoNombre = input("Ingrese el nuevo nombre: ")
                                                        ListaActualizar2.append(ListaClientes[4])
                                                        ListaActualizar2.append(nuevoNombre)
                                                        ListaActualizar2.append(ListaClientes[6])
                                                        ListaActualizar2.append(ListaClientes[7])
                                                        print(f"Nombre actualizado éxitosamente...\nUsuario: {ListaActualizar2[0]} {ListaActualizar2[1]} {ListaActualizar2[2]} {ListaActualizar2[3]}")
                                                        control2 = 1
                                                                                                                
                                                    elif UsuarioQuiereActualizarEl == "3": # ACTUALIZAR APELLIDO DEL CLIENTE
                                                        print(f"Ha seleccionado el usuario {eleccionUsuarioActualizar}, para actualizar el apellido.\n")
                                                        nuevoApellido = input("Ingrese el nuevo apellido: ")
                                                        ListaActualizar2.append(ListaClientes[4])
                                                        ListaActualizar2.append(ListaClientes[5])
                                                        ListaActualizar2.append(nuevoApellido)
                                                        ListaActualizar2.append(ListaClientes[7])
                                                        print(f"Apellido actualizado éxitosamente...\nUsuario: {ListaActualizar2[0]} {ListaActualizar2[1]} {ListaActualizar2[2]} {ListaActualizar2[3]}")
                                                        control2 = 1
                                                                                                                
                                                    elif UsuarioQuiereActualizarEl == "4": # ACTUALIZAR MÉTODO DEL CLIENTE
                                                        print(f"Ha seleccionado el usuario {eleccionUsuarioActualizar}, para actualizar el método de pago.\n")
                                                        nuevoMetodo = input("Ingrese el nuevo método. '1' para pagar con tarjeta de crédito o débito. '2' para pagar en efectivo.\n> ")
                                                        if nuevoMetodo == "1":
                                                            nuevoMetodoActualizado = "Tarjeta de crédito o débito"
                                                        elif nuevoMetodo == "2":
                                                            nuevoMetodoActualizado = "Efectivo"                                                            
                                                        ListaActualizar2.append(ListaClientes[4])
                                                        ListaActualizar2.append(ListaClientes[5])
                                                        ListaActualizar2.append(ListaClientes[6])
                                                        ListaActualizar2.append(nuevoMetodoActualizado)
                                                        print(f"Método de pago actualizado éxitosamente...\nUsuario: {ListaActualizar2[0]} {ListaActualizar2[1]} {ListaActualizar2[2]} {ListaActualizar2[3]}")
                                                        control2 = 1
                                                        
                                                    elif UsuarioQuiereActualizarEl == "5":
                                                        break
                                                    
                                                
                                            else:
                                                print("Lo siento, no hay  esa cantidad de clientes registrados.\n")
                                                
#=======================================================================================ACTUALIZACION CLIENTE 3================================================================================================================================ #

                                        elif eleccionUsuarioActualizar == 3:
                                            print(f"El usuario seleccionado es: {ListaClientes[8]} {ListaClientes[9]} {ListaClientes[10]} {ListaClientes[11]}")
                                            print("¿Seguro que quieres actualizar este usuario?\n '1' para Sí y '0' para No.")
                                            respuestaSioNo = int(input("> "))
                                            while respuestaSioNo:
                                                if respuestaSioNo:
                                                    print("|1.-| Cédula\n|2.-| Nombre\n|3.-| Apellidos\n|4.-| Método de pag\n|5.-| Dejar actualizar")
                                                    UsuarioQuiereActualizarEl = input(f"¿Qué quiere actualizar del usuario {eleccionUsuarioActualizar}?\n> ")
                                                    
                                                    if UsuarioQuiereActualizarEl == "1": # ACTUALIZAR CEDULA DEL CLIENTE
                                                        print(f"Ha seleccionado el usuario {eleccionUsuarioActualizar}, para actualizar la cédula.\n")
                                                        nuevaCedula = int(input("Ingrese la nueva cédula: "))
                                                        NuevaCedulaEnString = str(nuevaCedula)
                                                        ListaActualizar3.append(NuevaCedulaEnString)
                                                        ListaActualizar3.append(ListaClientes[9])
                                                        ListaActualizar3.append(ListaClientes[10])
                                                        ListaActualizar3.append(ListaClientes[11])
                                                        print(f"Cédula actualizada éxitosamente...\nUsuario: {ListaActualizar3[0]} {ListaActualizar3[1]} {ListaActualizar3[2]} {ListaActualizar3[3]}")
                                                        control3 = 1

                                                    elif UsuarioQuiereActualizarEl == "2": # ACTUALIZAR NOMBRE DEL CLIENTE
                                                        print(f"Ha seleccionado el usuario {eleccionUsuarioActualizar}, para actualizar el nombre.\n")
                                                        nuevoNombre = input("Ingrese el nuevo nombre: ")
                                                        ListaActualizar3.append(ListaClientes[8])
                                                        ListaActualizar3.append(nuevoNombre)
                                                        ListaActualizar3.append(ListaClientes[10])
                                                        ListaActualizar3.append(ListaClientes[11])
                                                        print(f"Nombre actualizado éxitosamente...\nUsuario: {ListaActualizar3[0]} {ListaActualizar3[1]} {ListaActualizar3[2]} {ListaActualizar3[3]}")
                                                        control3 = 1
                                                                                                                
                                                    elif UsuarioQuiereActualizarEl == "3": # ACTUALIZAR APELLIDO DEL CLIENTE
                                                        print(f"Ha seleccionado el usuario {eleccionUsuarioActualizar}, para actualizar el apellido.\n")
                                                        nuevoApellido = input("Ingrese el nuevo apellido: ")
                                                        ListaActualizar3.append(ListaClientes[8])
                                                        ListaActualizar3.append(ListaClientes[9])
                                                        ListaActualizar3.append(nuevoApellido)
                                                        ListaActualizar3.append(ListaClientes[11])
                                                        print(f"Apellido actualizado éxitosamente...\nUsuario: {ListaActualizar3[0]} {ListaActualizar3[1]} {ListaActualizar3[2]} {ListaActualizar3[3]}")
                                                        control3 = 1
                                                                                                                
                                                    elif UsuarioQuiereActualizarEl == "4": # ACTUALIZAR MÉTODO DEL CLIENTE
                                                        print(f"Ha seleccionado el usuario {eleccionUsuarioActualizar}, para actualizar el método de pago.\n")
                                                        nuevoMetodo = input("Ingrese el nuevo método. '1' para pagar con tarjeta de crédito o débito. '2' para pagar en efectivo.\n> ")
                                                        if nuevoMetodo == "1":
                                                            nuevoMetodoActualizado = "Tarjeta de crédito o débito"
                                                        elif nuevoMetodo == "2":
                                                            nuevoMetodoActualizado = "Efectivo"                                                            
                                                        ListaActualizar3.append(ListaClientes[8])
                                                        ListaActualizar3.append(ListaClientes[9])
                                                        ListaActualizar3.append(ListaClientes[10])
                                                        ListaActualizar3.append(nuevoMetodoActualizado)
                                                        print(f"Método de pago actualizado éxitosamente...\nUsuario: {ListaActualizar3[0]} {ListaActualizar3[1]} {ListaActualizar3[2]} {ListaActualizar3[3]}")
                                                        control3 = 1
                                                        
                                                    elif UsuarioQuiereActualizarEl == "5":
                                                        break
                                                    
                                            else:
                                                print("Lo siento, no hay  esa cantidad de clientes registrados.\n")
#====================================================================================ACTUALIZACION CLIENTE 4=================================================================================================================================== #

                                        elif eleccionUsuarioActualizar == 4:
                                            print(f"El usuario seleccionado es: {ListaClientes[12]} {ListaClientes[13]} {ListaClientes[14]} {ListaClientes[15]}")
                                            print("¿Seguro que quieres actualizar este usuario?\n '1' para Sí y '0' para No.")
                                            respuestaSioNo = int(input("> "))
                                            while respuestaSioNo:
                                                if respuestaSioNo:
                                                    print("|1.-| Cédula\n|2.-| Nombre\n|3.-| Apellidos\n|4.-| Método de pag\n|5.-| Dejar actualizar")
                                                    UsuarioQuiereActualizarEl = input(f"¿Qué quiere actualizar del usuario {eleccionUsuarioActualizar}?\n> ")
                                                    
                                                    if UsuarioQuiereActualizarEl == "1": # ACTUALIZAR CEDULA DEL CLIENTE
                                                        print(f"Ha seleccionado el usuario {eleccionUsuarioActualizar}, para actualizar la cédula.\n")
                                                        nuevaCedula = int(input("Ingrese la nueva cédula: "))
                                                        NuevaCedulaEnString = str(nuevaCedula)
                                                        ListaActualizar4.append(NuevaCedulaEnString)
                                                        ListaActualizar4.append(ListaClientes[13])
                                                        ListaActualizar4.append(ListaClientes[14])
                                                        ListaActualizar4.append(ListaClientes[15])
                                                        print(f"Cédula actualizada éxitosamente...\nUsuario: {ListaActualizar4[0]} {ListaActualizar4[1]} {ListaActualizar4[2]} {ListaActualizar4[3]}")
                                                        control4 = 1

                                                    elif UsuarioQuiereActualizarEl == "2": # ACTUALIZAR NOMBRE DEL CLIENTE
                                                        print(f"Ha seleccionado el usuario {eleccionUsuarioActualizar}, para actualizar el nombre.\n")
                                                        nuevoNombre = input("Ingrese el nuevo nombre: ")
                                                        ListaActualizar4.append(ListaClientes[12])
                                                        ListaActualizar4.append(nuevoNombre)
                                                        ListaActualizar4.append(ListaClientes[13])
                                                        ListaActualizar4.append(ListaClientes[14])
                                                        print(f"Nombre actualizado éxitosamente...\nUsuario: {ListaActualizar4[0]} {ListaActualizar4[1]} {ListaActualizar4[2]} {ListaActualizar4[3]}")
                                                        control4 = 1
                                                                                                                
                                                    elif UsuarioQuiereActualizarEl == "3": # ACTUALIZAR APELLIDO DEL CLIENTE
                                                        print(f"Ha seleccionado el usuario {eleccionUsuarioActualizar}, para actualizar el apellido.\n")
                                                        nuevoApellido = input("Ingrese el nuevo apellido: ")
                                                        ListaActualizar4.append(ListaClientes[12])
                                                        ListaActualizar4.append(ListaClientes[13])
                                                        ListaActualizar4.append(nuevoApellido)
                                                        ListaActualizar4.append(ListaClientes[15])
                                                        print(f"Apellido actualizado éxitosamente...\nUsuario: {ListaActualizar4[0]} {ListaActualizar4[1]} {ListaActualizar4[2]} {ListaActualizar4[3]}")
                                                        control4 = 1
                                                                                                                
                                                    elif UsuarioQuiereActualizarEl == "4": # ACTUALIZAR MÉTODO DEL CLIENTE
                                                        print(f"Ha seleccionado el usuario {eleccionUsuarioActualizar}, para actualizar el método de pago.\n")
                                                        nuevoMetodo = input("Ingrese el nuevo método. '1' para pagar con tarjeta de crédito o débito. '2' para pagar en efectivo.\n> ")
                                                        if nuevoMetodo == "1":
                                                            nuevoMetodoActualizado = "Tarjeta de crédito o débito"
                                                        elif nuevoMetodo == "2":
                                                            nuevoMetodoActualizado = "Efectivo"                                                            
                                                        ListaActualizar4.append(ListaClientes[12])
                                                        ListaActualizar4.append(ListaClientes[13])
                                                        ListaActualizar4.append(ListaClientes[14])
                                                        ListaActualizar4.append(nuevoMetodoActualizado)
                                                        print(f"Método de pago actualizado éxitosamente...\nUsuario: {ListaActualizar4[0]} {ListaActualizar4[1]} {ListaActualizar4[2]} {ListaActualizar4[3]}")
                                                        control4 = 1
                                                        
                                                    elif UsuarioQuiereActualizarEl == "5":
                                                        break

#======================================================================================ACTUALIZACION CLIENTE 5================================================================================================================================= #

                                        elif eleccionUsuarioActualizar == 5:
                                            print(f"El usuario seleccionado es: {ListaClientes[16]} {ListaClientes[17]} {ListaClientes[18]} {ListaClientes[19]}")
                                            print("¿Seguro que quieres actualizar este usuario?\n '1' para Sí y '0' para No.")
                                            respuestaSioNo = int(input("> "))
                                            while respuestaSioNo:
                                                print(f"Para dejar de actualizar el cliente: {eleccionUsuarioActualizar}, presione '5'")
                                                if respuestaSioNo:
                                                    print("|1.-| Cédula\n|2.-| Nombre\n|3.-| Apellidos\n|4.-| Método de pag\n|5.-| Dejar actualizar")
                                                    UsuarioQuiereActualizarEl = input(f"¿Qué quiere actualizar del usuario {eleccionUsuarioActualizar}?\n> ")
                                                    
                                                    if UsuarioQuiereActualizarEl == "1": # ACTUALIZAR CEDULA DEL CLIENTE
                                                        print(f"Ha seleccionado el usuario {eleccionUsuarioActualizar}, para actualizar la cédula.\n")
                                                        nuevaCedula = int(input("Ingrese la nueva cédula: "))
                                                        NuevaCedulaEnString = str(nuevaCedula)
                                                        ListaActualizar5.append(NuevaCedulaEnString)
                                                        ListaActualizar5.append(ListaClientes[17])
                                                        ListaActualizar5.append(ListaClientes[18])
                                                        ListaActualizar5.append(ListaClientes[19])
                                                        print(f"Cédula actualizada éxitosamente...\nUsuario: {ListaActualizar5[0]} {ListaActualizar5[1]} {ListaActualizar5[2]} {ListaActualizar5[3]}")
                                                        control5 = 1

                                                    elif UsuarioQuiereActualizarEl == "2": # ACTUALIZAR NOMBRE DEL CLIENTE
                                                        print(f"Ha seleccionado el usuario {eleccionUsuarioActualizar}, para actualizar el nombre.\n")
                                                        nuevoNombre = input("Ingrese el nuevo nombre: ")
                                                        ListaActualizar5.append(ListaClientes[16])
                                                        ListaActualizar5.append(nuevoNombre)
                                                        ListaActualizar5.append(ListaClientes[18])
                                                        ListaActualizar5.append(ListaClientes[19])
                                                        print(f"Nombre actualizado éxitosamente...\nUsuario: {ListaActualizar5[0]} {ListaActualizar5[1]} {ListaActualizar5[2]} {ListaActualizar5[3]}")
                                                        control5 = 1
                                                                                                                
                                                    elif UsuarioQuiereActualizarEl == "3": # ACTUALIZAR APELLIDO DEL CLIENTE
                                                        print(f"Ha seleccionado el usuario {eleccionUsuarioActualizar}, para actualizar el apellido.\n")
                                                        nuevoApellido = input("Ingrese el nuevo apellido: ")
                                                        ListaActualizar5.append(ListaClientes[16])
                                                        ListaActualizar5.append(ListaClientes[17])
                                                        ListaActualizar5.append(nuevoApellido)
                                                        ListaActualizar5.append(ListaClientes[19])
                                                        print(f"Apellido actualizado éxitosamente...\nUsuario: {ListaActualizar5[0]} {ListaActualizar5[1]} {ListaActualizar5[2]} {ListaActualizar5[3]}")
                                                        control5 = 1
                                                                                                                
                                                    elif UsuarioQuiereActualizarEl == "4": # ACTUALIZAR MÉTODO DEL CLIENTE
                                                        print(f"Ha seleccionado el usuario {eleccionUsuarioActualizar}, para actualizar el método de pago.\n")
                                                        nuevoMetodo = input("Ingrese el nuevo método. '1' para pagar con tarjeta de crédito o débito. '2' para pagar en efectivo.\n> ")
                                                        if nuevoMetodo == "1":
                                                            nuevoMetodoActualizado = "Tarjeta de crédito o débito"
                                                        elif nuevoMetodo == "2":
                                                            nuevoMetodoActualizado = "Efectivo"                                                            
                                                        ListaActualizar5.append(ListaClientes[16])
                                                        ListaActualizar5.append(ListaClientes[17])
                                                        ListaActualizar5.append(ListaClientes[18])
                                                        ListaActualizar5.append(nuevoMetodoActualizado)
                                                        print(f"Método de pago actualizado éxitosamente...\nUsuario: {ListaActualizar5[0]} {ListaActualizar5[1]} {ListaActualizar5[2]} {ListaActualizar5[3]}")
                                                        control5 = 1
                                                        
                                                    elif UsuarioQuiereActualizarEl == "5":
                                                        break
                                                
                                            else:
                                                print("Lo siento, no hay  esa cantidad de clientes registrados.\n")

                                        elif eleccionUsuarioActualizar == 6:
                                            Leer(0, control1,control2,control3,control4,control5)
                                            break
                                        
                                    break
                                        
                                                    
                                            
                                   
# ================================================================== Eliminar =================================================================== #
                        else:
                            while True:
                                try:
                                    print("Haz seleeccionado eliminar.\n\n¿Qué cliente desea eliminar?\n")
                                    eliminarOpcion = int(input("> "))
                                    break
                                except ValueError:
                                    print("No aceptamos data basura. Vuelva intentarlo.\n")
                                    continue
                                
                            while True:
                                if eliminarOpcion == 1:
                                    break
                                elif eliminarOpcion == 2:
                                    break
                                elif eliminarOpcion == 3:
                                    break
                                elif eliminarOpcion == 4:
                                    break
                                elif eliminarOpcion == 5:
                                    break
                                else:
                                    print("Lo siento, no existe esa cantidad de clientes... Vuelva intentarlo.\n")
                                    continue
                            
                        
                    else:
                        print(f"Lo siento, el '{eleccionCRUD}' no se encuentra en el menú. \n")
                        continue
                    
# ---------------------------------------------------------------- VIDEOJUEGOS MENU 1 ---------------------------------------------------------------- #
                elif x == 1 and y == 2: # CONFIGURACION MENU 1 EN VIDEO JUEGOS
                    eleccionCRUD = int(input("¿Qué desea hacer?\n> "))
                    if eleccionCRUD == 0:
                        print(f"Lo siento, el '{eleccionCRUD}' no se encuentra en el menú. \n")
                    elif eleccionCRUD >= 1 and eleccionCRUD <= 4:

# ================================================================== Crear =================================================================== #
                        if eleccionCRUD == 1:
                            pass
# ================================================================== LEER =================================================================== #
                        elif eleccionCRUD == 2:
                            pass
# ================================================================== Actualizar =================================================================== #
                        elif eleccionCRUD == 3:
                            pass
# ================================================================== Eliminar =================================================================== #
                        else:
                            pass
                        break
                    else:
                        print(f"Lo siento, el '{eleccionCRUD}' no se encuentra en el menú. \n")
                        continue
                    
# ---------------------------------------------------------------- VENTAS MENU 1 ---------------------------------------------------------------- #
                elif x == 1 and y == 3: # CONFIGURACION MENU 1 EN VENTAS
                    eleccionCRUD = int(input("¿Qué desea hacer?\n> "))
                    if eleccionCRUD == 0:
                        print(f"Lo siento, el '{eleccionCRUD}' no se encuentra en el menú. \n")
                    elif eleccionCRUD >= 1 and eleccionCRUD <= 4:
                        
# ================================================================== Crear =================================================================== #
                        if eleccionCRUD == 1:
                            pass
# ================================================================== LEER =================================================================== #
                        elif eleccionCRUD == 2:
                            pass
# ================================================================== Actualizar =================================================================== #
                        elif eleccionCRUD == 3:
                            pass
# ================================================================== Eliminar =================================================================== #
                        else:
                            pass
                        break
                    else:
                        print(f"Lo siento, el '{eleccionCRUD}' no se encuentra en el menú. \n")
                        continue
                        
# ---------------------------------------------------------------- CLIENTES MENU 2 ---------------------------------------------------------------- #
                elif x == 2 and y == 1: # CONFIGURACION MENU 2 EN CLIENTES
                    eleccionAdicional = int(input("¿Qué desea hacer?\n> "))
                    if eleccionAdicional == 0:
                        print(f"Lo siento, el '{eleccionAdicional}' no se encuentra en el menú. \n")   
                    elif eleccionAdicional >= 1 and eleccionAdicional <= 2:
# ================================================================== CARGA-EXPORTACION CSV =================================================================== #
                        if eleccionAdicional == 1:
                            pass
# ================================================================== CSV VENTAS MAYOR A RD$500.00 =================================================================== #
                        else:
                            pass
                        break
                    else:
                        print(f"Lo siento, el '{eleccionAdicional}' no se encuentra en el menú. \n")
                        continue
                    
# ---------------------------------------------------------------- VIDEOJUEGOS MENU 2 ---------------------------------------------------------------- #
                elif x == 2 and y == 2: # CONFIGURACION MENU 2 EN VIDEOJUEGOS
                    eleccionAdicional = int(input("¿Qué desea hacer?\n> "))
                    if eleccionAdicional == 0:
                        print(f"Lo siento, el '{eleccionAdicional}' no se encuentra en el menú. \n")   
                    elif eleccionAdicional >= 1 and eleccionAdicional <= 2:
# ================================================================== CARGA-EXPORTACION CSV =================================================================== #
                        if eleccionAdicional == 1:
                            pass
# ================================================================== CSV VENTAS MAYOR A RD$500.00 =================================================================== #
                        else:
                            pass
                        break
                    else:
                        print(f"Lo siento, el '{eleccionAdicional}' no se encuentra en el menú. \n")
                        continue
                    
# ---------------------------------------------------------------- VENTAS MENU 2 ---------------------------------------------------------------- #
                elif x == 2 and y == 3: # CONFIGURACION MENU 2 EN VENTAS
                    eleccionAdicional = int(input("¿Qué desea hacer?\n> "))
                    if eleccionAdicional == 0:
                        print(f"Lo siento, el '{eleccionAdicional}' no se encuentra en el menú. \n")   
                    elif eleccionAdicional >= 1 and eleccionAdicional <= 2:
# ================================================================== CARGA-EXPORTACION CSV =================================================================== #
                        if eleccionAdicional == 1:
                            pass
# ================================================================== CSV VENTAS MAYOR A RD$500.00 =================================================================== #
                        else:
                            pass
                        break
                    else:
                        print(f"Lo siento, el '{eleccionAdicional}' no se encuentra en el menú. \n")
                        continue
                elegirMenu()
            except ValueError:
                print("Lo siento, no aceptamos data basura.\n")
                continue
            
    def elegirMenu():
        while True:
            try:
                eleccionMenu = int(input("\n¿Qué menú desea utilizar? '1' para 'Menú CRUD' y '2' para 'Menú adicional' y '3' para mostrar el menú\n> "))
                if eleccionMenu == 0:
                    print(f"Lo siento, el '{eleccionMenu}' no se encuentra dentro de las opciones (1 y 2). \n")
                elif eleccionMenu == 1:
                    print("Haz seleccionado el menú CRUD...")
                    elegirOpcionEnMenu(1, eleccionPrincipal)
                elif eleccionMenu == 2:
                    print("Haz seleccionado el menú adicional...")
                    elegirOpcionEnMenu(2, eleccionPrincipal)
                
                elif eleccionMenu == 3:
                    Menus(1)
                else:
                    print(f"Lo siento, el '{eleccionMenu}' no se encuentra dentro de las opciones (1 y 2). \n")
                    continue
                break
            except ValueError:
                print("Lo siento, no aceptamos data basura.\n")
                continue
    if a == 0:
        elegirOpcionEnMenu(1,eleccionPrincipal)
    else:        
        elegirMenu()

while True:
    try:
        eleccionPrincipal = int(input("¿Qué desea hacer?\n> "))
        if eleccionPrincipal == 0:
            print(f"Lo siento, el '{eleccionPrincipal}' no se encuentra en el menú. \n")
        elif eleccionPrincipal >= 1 and eleccionPrincipal <= 3:
            if eleccionPrincipal == 1:
                print("Haz seleccionado 'Clientes'...")
                Menus(1)
            elif eleccionPrincipal == 2:
                print("Haz seleccionado 'VideoJuegos'...")
                Menus(1)
            else:
                print("Haz seleccionado 'Ventas'...")
                Menus(1)
            break
        else:
            print(f"Lo siento, el '{eleccionPrincipal}' no se encuentra en el menú. \n")
            continue

    except ValueError:
        print("Lo siento, no aceptamos data basura.\n")
        continue