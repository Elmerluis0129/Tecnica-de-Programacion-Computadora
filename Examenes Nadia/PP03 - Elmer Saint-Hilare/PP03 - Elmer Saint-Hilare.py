"""
Examen Final - Sistema PowerGames
Valor: 100ptos.

Mediante el uso de Programación Orientada a Objetos, desarrollar un pequeño sistema que permita el mantenimiento de las ventas de Ventas de PowerGames.

Indicaciones:

El sistema debe tener un menú de opciones que permita la interacción con el mismo.
El sistema debe realizar las 4 operaciones de un CRUD (Create, Read, Update, Delete) para las siguientes clases (modelos):
Clientes.
Ventas.
Ventas.
El sistema debe permitir la carga y la exportación de data a través de archivos .csv (para todos los modelos).
El sistema debe tener una opción que permita generar un archivo .csv con los Ventas cuyas ventas sean mayores a RD$500.00.

Elmer Saint-Hilare 21-1354
"""

import PP03_Clientes as Cls
import PP03_Ventas as Vns
import PP03_VideoJuegos as Vjs

# ============= CLIENTES LISTAS ============= #
ListaClientes = []
ListaActualizar1 = []
ListaActualizar2 = []
ListaActualizar3 = []
ListaActualizar4 = []
ListaActualizar5 = []
ListaActualizarAuxiliar = []
ListaEliminarAuxiliar = []

# ============= VENTAS LISTAS ============= #
ListaVentas = []
ListaActualizarVentas1 = [] 
ListaActualizarVentas2 = [] 
ListaActualizarVentas3 = [] 
ListaActualizarVentas4 = [] 
ListaActualizarVentas5 = [] 
ListaEliminarAuxiliarVentas = []
ListaActualizarAuxiliarVentas = []

# ============= VideoJuegos LISTAS ============= #
ListaVideoJuegos = []
ListaActualizarVideoJuegos1 = [] 
ListaActualizarVideoJuegos2 = [] 
ListaActualizarVideoJuegos3 = [] 
ListaActualizarVideoJuegos4 = [] 
ListaActualizarVideoJuegos5 = [] 
ListaEliminarAuxiliarVideoJuegos = []
ListaActualizarAuxiliarVideoJuegos = []


def MenuPrincipal():
    print(
"""
  Menú Principal
*----------------*
|1.| Clientes
|2.| Ventas
|3.| Videojuegos
*----------------*
""")
MenuPrincipal()

def EliminarClientes(control):
    if len(ListaClientes) == 4:
        print(f"Eliminando cédula del cliente: {ListaClientes[0]}")
        ListaClientes.remove(ListaClientes[0])
        print("¡Cédula eliminada exitosamente")
        print(f"Eliminando nombre del cliente: {ListaClientes[0]}")
        ListaClientes.remove(ListaClientes[0])
        print("¡Nombre eliminado exitosamente")
        print(f"Eliminando apellido del cliente: {ListaClientes[0]}")
        ListaClientes.remove(ListaClientes[0])
        print("¡Apellido eliminado exitosamente")
        print(f"Eliminando método de pago del cliente: {ListaClientes[0]}")
        ListaClientes.remove(ListaClientes[0])
        print("¡Método eliminado exitosamente")
        print("Cliente eliminado exitosamente")
        
    elif len(ListaClientes) == 8:
        if control == 1:
            print(f"Eliminando cédula del cliente: {ListaClientes[0]}")
            ListaClientes.remove(ListaClientes[0])
            print("¡Cédula eliminada exitosamente")
            print(f"Eliminando nombre del cliente: {ListaClientes[0]}")
            ListaClientes.remove(ListaClientes[0])
            print("¡Nombre eliminado exitosamente")
            print(f"Eliminando apellido del cliente: {ListaClientes[0]}")
            ListaClientes.remove(ListaClientes[0])
            print("¡Apellido eliminado exitosamente")
            print(f"Eliminando método de pago del cliente: {ListaClientes[0]}")
            ListaClientes.remove(ListaClientes[0])
            print("¡Método eliminado exitosamente")
            print("Cliente eliminado exitosamente")
        elif control == 2:
            print(f"Eliminando cédula del cliente: {ListaClientes[4]}")
            ListaClientes.remove(ListaClientes[4])
            print("¡Cédula eliminada exitosamente")
            print(f"Eliminando nombre del cliente: {ListaClientes[4]}")
            ListaClientes.remove(ListaClientes[4])
            print("¡Nombre eliminado exitosamente")
            print(f"Eliminando apellido del cliente: {ListaClientes[4]}")
            ListaClientes.remove(ListaClientes[4])
            print("¡Apellido eliminado exitosamente")
            print(f"Eliminando método de pago del cliente: {ListaClientes[4]}")
            ListaClientes.remove(ListaClientes[4])
            print("¡Método eliminado exitosamente")
            print("Cliente eliminado exitosamente")

    elif len(ListaClientes) == 12:
        if control == 1:
            print(f"Eliminando cédula del cliente: {ListaClientes[0]}")
            ListaClientes.remove(ListaClientes[0])
            print("¡Cédula eliminada exitosamente")
            print(f"Eliminando nombre del cliente: {ListaClientes[0]}")
            ListaClientes.remove(ListaClientes[0])
            print("¡Nombre eliminado exitosamente")
            print(f"Eliminando apellido del cliente: {ListaClientes[0]}")
            ListaClientes.remove(ListaClientes[0])
            print("¡Apellido eliminado exitosamente")
            print(f"Eliminando método de pago del cliente: {ListaClientes[0]}")
            ListaClientes.remove(ListaClientes[0])
            print("¡Método eliminado exitosamente")
            print("Cliente eliminado exitosamente")
        elif control == 2:
            print(f"Eliminando cédula del cliente: {ListaClientes[4]}")
            ListaClientes.remove(ListaClientes[4])
            print("¡Cédula eliminada exitosamente")
            print(f"Eliminando nombre del cliente: {ListaClientes[4]}")
            ListaClientes.remove(ListaClientes[4])
            print("¡Nombre eliminado exitosamente")
            print(f"Eliminando apellido del cliente: {ListaClientes[4]}")
            ListaClientes.remove(ListaClientes[4])
            print("¡Apellido eliminado exitosamente")
            print(f"Eliminando método de pago del cliente: {ListaClientes[4]}")
            ListaClientes.remove(ListaClientes[4])
            print("¡Método eliminado exitosamente")
            print("Cliente eliminado exitosamente")
        elif control == 3:
            print(f"Eliminando cédula del cliente: {ListaClientes[8]}")
            ListaClientes.remove(ListaClientes[8])
            print("¡Cédula eliminada exitosamente")
            print(f"Eliminando nombre del cliente: {ListaClientes[8]}")
            ListaClientes.remove(ListaClientes[8])
            print("¡Nombre eliminado exitosamente")
            print(f"Eliminando apellido del cliente: {ListaClientes[8]}")
            ListaClientes.remove(ListaClientes[8])
            print("¡Apellido eliminado exitosamente")
            print(f"Eliminando método de pago del cliente: {ListaClientes[8]}")
            ListaClientes.remove(ListaClientes[8])
            print("¡Método eliminado exitosamente")
            print("Cliente eliminado exitosamente")
    
    elif len(ListaClientes) == 16:
        if control == 1:
            print(f"Eliminando cédula del cliente: {ListaClientes[0]}")
            ListaClientes.remove(ListaClientes[0])
            print("¡Cédula eliminada exitosamente")
            print(f"Eliminando nombre del cliente: {ListaClientes[0]}")
            ListaClientes.remove(ListaClientes[0])
            print("¡Nombre eliminado exitosamente")
            print(f"Eliminando apellido del cliente: {ListaClientes[0]}")
            ListaClientes.remove(ListaClientes[0])
            print("¡Apellido eliminado exitosamente")
            print(f"Eliminando método de pago del cliente: {ListaClientes[0]}")
            ListaClientes.remove(ListaClientes[0])
            print("¡Método eliminado exitosamente")
            print("Cliente eliminado exitosamente")
        elif control == 2:
            print(f"Eliminando cédula del cliente: {ListaClientes[4]}")
            ListaClientes.remove(ListaClientes[4])
            print("¡Cédula eliminada exitosamente")
            print(f"Eliminando nombre del cliente: {ListaClientes[4]}")
            ListaClientes.remove(ListaClientes[4])
            print("¡Nombre eliminado exitosamente")
            print(f"Eliminando apellido del cliente: {ListaClientes[4]}")
            ListaClientes.remove(ListaClientes[4])
            print("¡Apellido eliminado exitosamente")
            print(f"Eliminando método de pago del cliente: {ListaClientes[4]}")
            ListaClientes.remove(ListaClientes[4])
            print("¡Método eliminado exitosamente")
            print("Cliente eliminado exitosamente")
        elif control == 3:
            print(f"Eliminando cédula del cliente: {ListaClientes[8]}")
            ListaClientes.remove(ListaClientes[8])
            print("¡Cédula eliminada exitosamente")
            print(f"Eliminando nombre del cliente: {ListaClientes[8]}")
            ListaClientes.remove(ListaClientes[8])
            print("¡Nombre eliminado exitosamente")
            print(f"Eliminando apellido del cliente: {ListaClientes[8]}")
            ListaClientes.remove(ListaClientes[8])
            print("¡Apellido eliminado exitosamente")
            print(f"Eliminando método de pago del cliente: {ListaClientes[8]}")
            ListaClientes.remove(ListaClientes[8])
            print("¡Método eliminado exitosamente")
            print("Cliente eliminado exitosamente")
        elif control == 4:
            print(f"Eliminando cédula del cliente: {ListaClientes[12]}")
            ListaClientes.remove(ListaClientes[12])
            print("¡Cédula eliminada exitosamente")
            print(f"Eliminando nombre del cliente: {ListaClientes[12]}")
            ListaClientes.remove(ListaClientes[12])
            print("¡Nombre eliminado exitosamente")
            print(f"Eliminando apellido del cliente: {ListaClientes[12]}")
            ListaClientes.remove(ListaClientes[12])
            print("¡Apellido eliminado exitosamente")
            print(f"Eliminando método de pago del cliente: {ListaClientes[12]}")
            ListaClientes.remove(ListaClientes[12])
            print("¡Método eliminado exitosamente")
            print("Cliente eliminado exitosamente")
    
    elif len(ListaClientes) == 20:
        if control == 1:
            print(f"Eliminando cédula del cliente: {ListaClientes[0]}")
            ListaClientes.remove(ListaClientes[0])
            print("¡Cédula eliminada exitosamente")
            print(f"Eliminando nombre del cliente: {ListaClientes[0]}")
            ListaClientes.remove(ListaClientes[0])
            print("¡Nombre eliminado exitosamente")
            print(f"Eliminando apellido del cliente: {ListaClientes[0]}")
            ListaClientes.remove(ListaClientes[0])
            print("¡Apellido eliminado exitosamente")
            print(f"Eliminando método de pago del cliente: {ListaClientes[0]}")
            ListaClientes.remove(ListaClientes[0])
            print("¡Método eliminado exitosamente")
            print("Cliente eliminado exitosamente")
            
        elif control == 2:
            print(f"Eliminando cédula del cliente: {ListaClientes[4]}")
            ListaClientes.remove(ListaClientes[4])
            print("¡Cédula eliminada exitosamente")
            print(f"Eliminando nombre del cliente: {ListaClientes[4]}")
            ListaClientes.remove(ListaClientes[4])
            print("¡Nombre eliminado exitosamente")
            print(f"Eliminando apellido del cliente: {ListaClientes[4]}")
            ListaClientes.remove(ListaClientes[4])
            print("¡Apellido eliminado exitosamente")
            print(f"Eliminando método de pago del cliente: {ListaClientes[4]}")
            ListaClientes.remove(ListaClientes[4])
            print("¡Método eliminado exitosamente")
            print("Cliente eliminado exitosamente")
            
        elif control == 3:
            print(f"Eliminando cédula del cliente: {ListaClientes[8]}")
            ListaClientes.remove(ListaClientes[8])
            print("¡Cédula eliminada exitosamente")
            print(f"Eliminando nombre del cliente: {ListaClientes[8]}")
            ListaClientes.remove(ListaClientes[8])
            print("¡Nombre eliminado exitosamente")
            print(f"Eliminando apellido del cliente: {ListaClientes[8]}")
            ListaClientes.remove(ListaClientes[8])
            print("¡Apellido eliminado exitosamente")
            print(f"Eliminando método de pago del cliente: {ListaClientes[8]}")
            ListaClientes.remove(ListaClientes[8])
            print("¡Método eliminado exitosamente")
            print("Cliente eliminado exitosamente")
            
        elif control == 4:
            print(f"Eliminando cédula del cliente: {ListaClientes[12]}")
            ListaClientes.remove(ListaClientes[12])
            print("¡Cédula eliminada exitosamente")
            print(f"Eliminando nombre del cliente: {ListaClientes[12]}")
            ListaClientes.remove(ListaClientes[12])
            print("¡Nombre eliminado exitosamente")
            print(f"Eliminando apellido del cliente: {ListaClientes[12]}")
            ListaClientes.remove(ListaClientes[12])
            print("¡Apellido eliminado exitosamente")
            print(f"Eliminando método de pago del cliente: {ListaClientes[12]}")
            ListaClientes.remove(ListaClientes[12])
            print("¡Método eliminado exitosamente")
            print("Cliente eliminado exitosamente")
            
        elif control == 5:
            print(f"Eliminando cédula del cliente: {ListaClientes[16]}")
            ListaClientes.remove(ListaClientes[16])
            print("¡Cédula eliminada exitosamente")
            print(f"Eliminando nombre del cliente: {ListaClientes[16]}")
            ListaClientes.remove(ListaClientes[16])
            print("¡Nombre eliminado exitosamente")
            print(f"Eliminando apellido del cliente: {ListaClientes[16]}")
            ListaClientes.remove(ListaClientes[16])
            print("¡Apellido eliminado exitosamente")
            print(f"Eliminando método de pago del cliente: {ListaClientes[16]}")
            ListaClientes.remove(ListaClientes[16])
            print("¡Método eliminado exitosamente")
            print("Cliente eliminado exitosamente")



# ======================== ELIMINAR VENTAS ======================== #
def EliminarVentas(control):
    if len(ListaVideoJuegos) == 5:
        print(f"Eliminando no. de venta: {ListaVentas[0]}"), ListaVentas.remove(ListaVentas[0]), print("No. de venta eliminado exitosamente")
        print(f"Eliminando nombre del videojuego: {ListaVentas[0]}"), ListaVentas.remove(ListaVentas[0]), print("¡Nombre eliminado exitosamente")
        print(f"Eliminando cedula del cliente: {ListaVentas[0]}"), ListaVentas.remove(ListaVentas[0]), print("Cedula eliminada exitosamente")
        print(f"Eliminando precio del videojuego: {ListaVentas[0]}"), ListaVentas.remove(ListaVentas[0]), print("Precio eliminado exitosamente")
        print(f"Eliminando tipo del videojuego: {ListaVentas[0]}"), ListaVentas.remove(ListaVentas[0]), print("Tipo eliminado exitosamente")
        
    elif len(ListaVentas) == 10:
        if control == 1:
            print(f"Eliminando no. de venta: {ListaVentas[0]}"), ListaVentas.remove(ListaVentas[0]), print("No. de venta eliminado exitosamente")
            print(f"Eliminando nombre del videojuego: {ListaVentas[0]}"), ListaVentas.remove(ListaVentas[0]), print("¡Nombre eliminado exitosamente")
            print(f"Eliminando cedula del cliente: {ListaVentas[0]}"), ListaVentas.remove(ListaVentas[0]), print("Cedula eliminada exitosamente")
            print(f"Eliminando precio del videojuego: {ListaVentas[0]}"), ListaVentas.remove(ListaVentas[0]), print("Precio eliminado exitosamente")
            print(f"Eliminando tipo del videojuego: {ListaVentas[0]}"), ListaVentas.remove(ListaVentas[0]), print("Tipo eliminado exitosamente")
        elif control == 2:
            print(f"Eliminando no. de venta: {ListaVentas[5]}"), ListaVentas.remove(ListaVentas[5]), print("No. de venta eliminado exitosamente")
            print(f"Eliminando nombre del videojuego: {ListaVentas[5]}"), ListaVentas.remove(ListaVentas[5]), print("¡Nombre eliminado exitosamente")
            print(f"Eliminando cedula del cliente: {ListaVentas[5]}"), ListaVentas.remove(ListaVentas[5]), print("Cedula eliminada exitosamente")
            print(f"Eliminando precio del videojuego: {ListaVentas[5]}"), ListaVentas.remove(ListaVentas[5]), print("Precio eliminado exitosamente")
            print(f"Eliminando tipo del videojuego: {ListaVentas[5]}"), ListaVentas.remove(ListaVentas[5]), print("Tipo eliminado exitosamente")

    elif len(ListaVentas) == 15:
        if control == 1:
            print(f"Eliminando no. de venta: {ListaVentas[0]}"), ListaVentas.remove(ListaVentas[0]), print("No. de venta eliminado exitosamente")
            print(f"Eliminando nombre del videojuego: {ListaVentas[0]}"), ListaVentas.remove(ListaVentas[0]), print("¡Nombre eliminado exitosamente")
            print(f"Eliminando cedula del cliente: {ListaVentas[0]}"), ListaVentas.remove(ListaVentas[0]), print("Cedula eliminada exitosamente")
            print(f"Eliminando precio del videojuego: {ListaVentas[0]}"), ListaVentas.remove(ListaVentas[0]), print("Precio eliminado exitosamente")
            print(f"Eliminando tipo del videojuego: {ListaVentas[0]}"), ListaVentas.remove(ListaVentas[0]), print("Tipo eliminado exitosamente")
        elif control == 2:
            print(f"Eliminando no. de venta: {ListaVentas[5]}"), ListaVentas.remove(ListaVentas[5]), print("No. de venta eliminado exitosamente")
            print(f"Eliminando nombre del videojuego: {ListaVentas[5]}"), ListaVentas.remove(ListaVentas[5]), print("¡Nombre eliminado exitosamente")
            print(f"Eliminando cedula del cliente: {ListaVentas[5]}"), ListaVentas.remove(ListaVentas[5]), print("Cedula eliminada exitosamente")
            print(f"Eliminando precio del videojuego: {ListaVentas[5]}"), ListaVentas.remove(ListaVentas[5]), print("Precio eliminado exitosamente")
            print(f"Eliminando tipo del videojuego: {ListaVentas[5]}"), ListaVentas.remove(ListaVentas[5]), print("Tipo eliminado exitosamente")
        elif control == 3:
            print(f"Eliminando no. de venta: {ListaVentas[10]}"), ListaVentas.remove(ListaVentas[10]), print("No. de venta eliminado exitosamente")
            print(f"Eliminando nombre del videojuego: {ListaVentas[10]}"), ListaVentas.remove(ListaVentas[10]), print("¡Nombre eliminado exitosamente")
            print(f"Eliminando cedula del cliente: {ListaVentas[10]}"), ListaVentas.remove(ListaVentas[10]), print("Cedula eliminada exitosamente")
            print(f"Eliminando precio del videojuego: {ListaVentas[10]}"), ListaVentas.remove(ListaVentas[10]), print("Precio eliminado exitosamente")
            print(f"Eliminando tipo del videojuego: {ListaVentas[10]}"), ListaVentas.remove(ListaVentas[10]), print("Tipo eliminado exitosamente")
    
    elif len(ListaVentas) == 20:
        if control == 1:
            print(f"Eliminando no. de venta: {ListaVentas[0]}"), ListaVentas.remove(ListaVentas[0]), print("No. de venta eliminado exitosamente")
            print(f"Eliminando nombre del videojuego: {ListaVentas[0]}"), ListaVentas.remove(ListaVentas[0]), print("¡Nombre eliminado exitosamente")
            print(f"Eliminando cedula del cliente: {ListaVentas[0]}"), ListaVentas.remove(ListaVentas[0]), print("Cedula eliminada exitosamente")
            print(f"Eliminando precio del videojuego: {ListaVentas[0]}"), ListaVentas.remove(ListaVentas[0]), print("Precio eliminado exitosamente")
            print(f"Eliminando tipo del videojuego: {ListaVentas[0]}"), ListaVentas.remove(ListaVentas[0]), print("Tipo eliminado exitosamente")
            
        elif control == 2:
            print(f"Eliminando no. de venta: {ListaVentas[5]}"), ListaVentas.remove(ListaVentas[5]), print("No. de venta eliminado exitosamente")
            print(f"Eliminando nombre del videojuego: {ListaVentas[5]}"), ListaVentas.remove(ListaVentas[5]), print("¡Nombre eliminado exitosamente")
            print(f"Eliminando cedula del cliente: {ListaVentas[5]}"), ListaVentas.remove(ListaVentas[5]), print("Cedula eliminada exitosamente")
            print(f"Eliminando precio del videojuego: {ListaVentas[5]}"), ListaVentas.remove(ListaVentas[5]), print("Precio eliminado exitosamente")
            print(f"Eliminando tipo del videojuego: {ListaVentas[5]}"), ListaVentas.remove(ListaVentas[5]), print("Tipo eliminado exitosamente")
            
        elif control == 3:
            print(f"Eliminando no. de venta: {ListaVentas[10]}"), ListaVentas.remove(ListaVentas[10]), print("No. de venta eliminado exitosamente")
            print(f"Eliminando nombre del videojuego: {ListaVentas[10]}"), ListaVentas.remove(ListaVentas[10]), print("¡Nombre eliminado exitosamente")
            print(f"Eliminando cedula del cliente: {ListaVentas[10]}"), ListaVentas.remove(ListaVentas[10]), print("Cedula eliminada exitosamente")
            print(f"Eliminando precio del videojuego: {ListaVentas[10]}"), ListaVentas.remove(ListaVentas[10]), print("Precio eliminado exitosamente")
            print(f"Eliminando tipo del videojuego: {ListaVentas[10]}"), ListaVentas.remove(ListaVentas[10]), print("Tipo eliminado exitosamente")
            
        elif control == 4:
            print(f"Eliminando no. de venta: {ListaVentas[15]}"), ListaVentas.remove(ListaVentas[15]), print("No. de venta eliminado exitosamente")
            print(f"Eliminando nombre del videojuego: {ListaVentas[15]}"), ListaVentas.remove(ListaVentas[15]), print("¡Nombre eliminado exitosamente")
            print(f"Eliminando cedula del cliente: {ListaVentas[15]}"), ListaVentas.remove(ListaVentas[15]), print("Cedula eliminada exitosamente")
            print(f"Eliminando precio del videojuego: {ListaVentas[15]}"), ListaVentas.remove(ListaVentas[15]), print("Precio eliminado exitosamente")
            print(f"Eliminando tipo del videojuego: {ListaVentas[15]}"), ListaVentas.remove(ListaVentas[15]), print("Tipo eliminado exitosamente")
    
    elif len(ListaVentas) == 25:
        if control == 1:
            print(f"Eliminando no. de venta: {ListaVentas[0]}"), ListaVentas.remove(ListaVentas[0]), print("No. de venta eliminado exitosamente")
            print(f"Eliminando nombre del videojuego: {ListaVentas[0]}"), ListaVentas.remove(ListaVentas[0]), print("¡Nombre eliminado exitosamente")
            print(f"Eliminando cedula del cliente: {ListaVentas[0]}"), ListaVentas.remove(ListaVentas[0]), print("Cedula eliminada exitosamente")
            print(f"Eliminando precio del videojuego: {ListaVentas[0]}"), ListaVentas.remove(ListaVentas[0]), print("Precio eliminado exitosamente")
            print(f"Eliminando tipo del videojuego: {ListaVentas[0]}"), ListaVentas.remove(ListaVentas[0]), print("Tipo eliminado exitosamente")
            
        elif control == 2:
            print(f"Eliminando no. de venta: {ListaVentas[5]}"), ListaVentas.remove(ListaVentas[5]), print("No. de venta eliminado exitosamente")
            print(f"Eliminando nombre del videojuego: {ListaVentas[5]}"), ListaVentas.remove(ListaVentas[5]), print("¡Nombre eliminado exitosamente")
            print(f"Eliminando cedula del cliente: {ListaVentas[5]}"), ListaVentas.remove(ListaVentas[5]), print("Cedula eliminada exitosamente")
            print(f"Eliminando precio del videojuego: {ListaVentas[5]}"), ListaVentas.remove(ListaVentas[5]), print("Precio eliminado exitosamente")
            print(f"Eliminando tipo del videojuego: {ListaVentas[5]}"), ListaVentas.remove(ListaVentas[5]), print("Tipo eliminado exitosamente")
            
        elif control == 3:
            print(f"Eliminando no. de venta: {ListaVentas[10]}"), ListaVentas.remove(ListaVentas[10]), print("No. de venta eliminado exitosamente")
            print(f"Eliminando nombre del videojuego: {ListaVentas[10]}"), ListaVentas.remove(ListaVentas[10]), print("¡Nombre eliminado exitosamente")
            print(f"Eliminando cedula del cliente: {ListaVentas[10]}"), ListaVentas.remove(ListaVentas[10]), print("Cedula eliminada exitosamente")
            print(f"Eliminando precio del videojuego: {ListaVentas[10]}"), ListaVentas.remove(ListaVentas[10]), print("Precio eliminado exitosamente")
            print(f"Eliminando tipo del videojuego: {ListaVentas[10]}"), ListaVentas.remove(ListaVentas[10]), print("Tipo eliminado exitosamente")
            
        elif control == 4:
            print(f"Eliminando no. de venta: {ListaVentas[15]}"), ListaVentas.remove(ListaVentas[15]), print("No. de venta eliminado exitosamente")
            print(f"Eliminando nombre del videojuego: {ListaVentas[15]}"), ListaVentas.remove(ListaVentas[15]), print("¡Nombre eliminado exitosamente")
            print(f"Eliminando cedula del cliente: {ListaVentas[15]}"), ListaVentas.remove(ListaVentas[15]), print("Cedula eliminada exitosamente")
            print(f"Eliminando precio del videojuego: {ListaVentas[15]}"), ListaVentas.remove(ListaVentas[15]), print("Precio eliminado exitosamente")
            print(f"Eliminando tipo del videojuego: {ListaVentas[15]}"), ListaVentas.remove(ListaVentas[15]), print("Tipo eliminado exitosamente")
            
        elif control == 5:
            print(f"Eliminando no. de venta: {ListaVentas[20]}"), ListaVentas.remove(ListaVentas[20]), print("No. de venta eliminado exitosamente")
            print(f"Eliminando nombre del videojuego: {ListaVentas[20]}"), ListaVentas.remove(ListaVentas[20]), print("¡Nombre eliminado exitosamente")
            print(f"Eliminando cedula del cliente: {ListaVentas[20]}"), ListaVentas.remove(ListaVentas[20]), print("Cedula eliminada exitosamente")
            print(f"Eliminando precio del videojuego: {ListaVentas[20]}"), ListaVentas.remove(ListaVentas[20]), print("Precio eliminado exitosamente")
            print(f"Eliminando tipo del videojuego: {ListaVentas[20]}"), ListaVentas.remove(ListaVentas[20]), print("Tipo eliminado exitosamente")
            
            
            
            
            
            
            
# ======================== ELIMINAR VIDEOJUEGO ======================== #
def EliminarVideoJuegos(control):
    if len(ListaVideoJuegos) == 3:
        print(f"Eliminando nombre del videojuego: {ListaVideoJuegos[0]}"), ListaVideoJuegos.remove(ListaVideoJuegos[0]), print("¡Nombre eliminado exitosamente")
        print(f"Eliminando tipo del videojuego: {ListaVideoJuegos[0]}"), ListaVideoJuegos.remove(ListaVideoJuegos[0]), print("Tipo eliminado exitosamente")
        print(f"Eliminando precio del videojuego: {ListaVideoJuegos[0]}"), ListaVideoJuegos.remove(ListaVideoJuegos[0]), print("Precio eliminado exitosamente")
        
    elif len(ListaVideoJuegos) == 6:
        if control == 1:
            print(f"Eliminando nombre del videojuego: {ListaVideoJuegos[0]}"), ListaVideoJuegos.remove(ListaVideoJuegos[0]), print("¡Nombre eliminado exitosamente")
            print(f"Eliminando tipo del videojuego: {ListaVideoJuegos[0]}"), ListaVideoJuegos.remove(ListaVideoJuegos[0]), print("Tipo eliminado exitosamente")
            print(f"Eliminando precio del videojuego: {ListaVideoJuegos[0]}"), ListaVideoJuegos.remove(ListaVideoJuegos[0]), print("Precio eliminado exitosamente")
        elif control == 2:
            print(f"Eliminando nombre del videojuego: {ListaVideoJuegos[3]}"), ListaVideoJuegos.remove(ListaVideoJuegos[3]), print("¡Nombre eliminado exitosamente")
            print(f"Eliminando tipo del videojuego: {ListaVideoJuegos[3]}"), ListaVideoJuegos.remove(ListaVideoJuegos[3]), print("Tipo eliminado exitosamente")
            print(f"Eliminando precio del videojuego: {ListaVideoJuegos[3]}"), ListaVideoJuegos.remove(ListaVideoJuegos[3]), print("Precio eliminado exitosamente")

    elif len(ListaVideoJuegos) == 9:
        if control == 1:
            print(f"Eliminando nombre del videojuego: {ListaVideoJuegos[0]}"), ListaVideoJuegos.remove(ListaVideoJuegos[0]), print("¡Nombre eliminado exitosamente")
            print(f"Eliminando tipo del videojuego: {ListaVideoJuegos[0]}"), ListaVideoJuegos.remove(ListaVideoJuegos[0]), print("Tipo eliminado exitosamente")
            print(f"Eliminando precio del videojuego: {ListaVideoJuegos[0]}"), ListaVideoJuegos.remove(ListaVideoJuegos[0]), print("Precio eliminado exitosamente")
        elif control == 2:
            print(f"Eliminando nombre del videojuego: {ListaVideoJuegos[3]}"), ListaVideoJuegos.remove(ListaVideoJuegos[3]), print("¡Nombre eliminado exitosamente")
            print(f"Eliminando tipo del videojuego: {ListaVideoJuegos[3]}"), ListaVideoJuegos.remove(ListaVideoJuegos[3]), print("Tipo eliminado exitosamente")
            print(f"Eliminando precio del videojuego: {ListaVideoJuegos[3]}"), ListaVideoJuegos.remove(ListaVideoJuegos[3]), print("Precio eliminado exitosamente")
        elif control == 3:
            print(f"Eliminando nombre del videojuego: {ListaVideoJuegos[6]}"), ListaVideoJuegos.remove(ListaVideoJuegos[6]), print("¡Nombre eliminado exitosamente")
            print(f"Eliminando tipo del videojuego: {ListaVideoJuegos[6]}"), ListaVideoJuegos.remove(ListaVideoJuegos[6]), print("Tipo eliminado exitosamente")
            print(f"Eliminando precio del videojuego: {ListaVideoJuegos[6]}"), ListaVideoJuegos.remove(ListaVideoJuegos[6]), print("Precio eliminado exitosamente")
    
    elif len(ListaVideoJuegos) == 12:
        if control == 1:
            print(f"Eliminando nombre del videojuego: {ListaVideoJuegos[0]}"), ListaVideoJuegos.remove(ListaVideoJuegos[0]), print("¡Nombre eliminado exitosamente")
            print(f"Eliminando tipo del videojuego: {ListaVideoJuegos[0]}"), ListaVideoJuegos.remove(ListaVideoJuegos[0]), print("Tipo eliminado exitosamente")
            print(f"Eliminando precio del videojuego: {ListaVideoJuegos[0]}"), ListaVideoJuegos.remove(ListaVideoJuegos[0]), print("Precio eliminado exitosamente")
        elif control == 2:
            print(f"Eliminando nombre del videojuego: {ListaVideoJuegos[3]}"), ListaVideoJuegos.remove(ListaVideoJuegos[3]), print("¡Nombre eliminado exitosamente")
            print(f"Eliminando tipo del videojuego: {ListaVideoJuegos[3]}"), ListaVideoJuegos.remove(ListaVideoJuegos[3]), print("Tipo eliminado exitosamente")
            print(f"Eliminando precio del videojuego: {ListaVideoJuegos[3]}"), ListaVideoJuegos.remove(ListaVideoJuegos[3]), print("Precio eliminado exitosamente")
        elif control == 3:
            print(f"Eliminando nombre del videojuego: {ListaVideoJuegos[6]}"), ListaVideoJuegos.remove(ListaVideoJuegos[6]), print("¡Nombre eliminado exitosamente")
            print(f"Eliminando tipo del videojuego: {ListaVideoJuegos[6]}"), ListaVideoJuegos.remove(ListaVideoJuegos[6]), print("Tipo eliminado exitosamente")
            print(f"Eliminando precio del videojuego: {ListaVideoJuegos[6]}"), ListaVideoJuegos.remove(ListaVideoJuegos[6]), print("Precio eliminado exitosamente")
            
        elif control == 4:
            print(f"Eliminando nombre del videojuego: {ListaVideoJuegos[9]}"), ListaVideoJuegos.remove(ListaVideoJuegos[9]), print("¡Nombre eliminado exitosamente")
            print(f"Eliminando tipo del videojuego: {ListaVideoJuegos[9]}"), ListaVideoJuegos.remove(ListaVideoJuegos[9]), print("Tipo eliminado exitosamente")
            print(f"Eliminando precio del videojuego: {ListaVideoJuegos[9]}"), ListaVideoJuegos.remove(ListaVideoJuegos[9]), print("Precio eliminado exitosamente")
    
    elif len(ListaVideoJuegos) == 15:
        if control == 1:
            print(f"Eliminando nombre del videojuego: {ListaVideoJuegos[0]}"), ListaVideoJuegos.remove(ListaVideoJuegos[0]), print("¡Nombre eliminado exitosamente")
            print(f"Eliminando tipo del videojuego: {ListaVideoJuegos[0]}"), ListaVideoJuegos.remove(ListaVideoJuegos[0]), print("Tipo eliminado exitosamente")
            print(f"Eliminando precio del videojuego: {ListaVideoJuegos[0]}"), ListaVideoJuegos.remove(ListaVideoJuegos[0]), print("Precio eliminado exitosamente")
        elif control == 2:
            print(f"Eliminando nombre del videojuego: {ListaVideoJuegos[3]}"), ListaVideoJuegos.remove(ListaVideoJuegos[3]), print("¡Nombre eliminado exitosamente")
            print(f"Eliminando tipo del videojuego: {ListaVideoJuegos[3]}"), ListaVideoJuegos.remove(ListaVideoJuegos[3]), print("Tipo eliminado exitosamente")
            print(f"Eliminando precio del videojuego: {ListaVideoJuegos[3]}"), ListaVideoJuegos.remove(ListaVideoJuegos[3]), print("Precio eliminado exitosamente")
        elif control == 3:
            print(f"Eliminando nombre del videojuego: {ListaVideoJuegos[6]}"), ListaVideoJuegos.remove(ListaVideoJuegos[6]), print("¡Nombre eliminado exitosamente")
            print(f"Eliminando tipo del videojuego: {ListaVideoJuegos[6]}"), ListaVideoJuegos.remove(ListaVideoJuegos[6]), print("Tipo eliminado exitosamente")
            print(f"Eliminando precio del videojuego: {ListaVideoJuegos[6]}"), ListaVideoJuegos.remove(ListaVideoJuegos[6]), print("Precio eliminado exitosamente")
            
        elif control == 4:
            print(f"Eliminando nombre del videojuego: {ListaVideoJuegos[9]}"), ListaVideoJuegos.remove(ListaVideoJuegos[9]), print("¡Nombre eliminado exitosamente")
            print(f"Eliminando tipo del videojuego: {ListaVideoJuegos[9]}"), ListaVideoJuegos.remove(ListaVideoJuegos[9]), print("Tipo eliminado exitosamente")
            print(f"Eliminando precio del videojuego: {ListaVideoJuegos[9]}"), ListaVideoJuegos.remove(ListaVideoJuegos[9]), print("Precio eliminado exitosamente")
            
        elif control == 5:
            print(f"Eliminando nombre del videojuego: {ListaVideoJuegos[12]}"), ListaVideoJuegos.remove(ListaVideoJuegos[12]), print("¡Nombre eliminado exitosamente")
            print(f"Eliminando tipo del videojuego: {ListaVideoJuegos[12]}"), ListaVideoJuegos.remove(ListaVideoJuegos[12]), print("Tipo eliminado exitosamente")
            print(f"Eliminando precio del videojuego: {ListaVideoJuegos[12]}"), ListaVideoJuegos.remove(ListaVideoJuegos[12]), print("Precio eliminado exitosamente")

def LeerVentas():
    contador1 = 0
    contador2 = 0
    contador3 = 0
    contador4 = 1
    prueba = 1
    while True:
        contador1 += 4
        contador2 += 5
        if len(ListaVentas) == contador2:
            operacion1 = contador2-contador1
            print(f"Se encontraron: {operacion1} videojuego/s.\n")
            for a in range(0,(operacion1)+1):
                if prueba:
                    print("""       No. Venta  |  Nombre  |  Cedula Cliente  |  Precio  |  Tipo""")
                    prueba = 0
                else:
                    print("*---*------------------------------------------------------------*")
                    print(f"|{contador4}.-|",ListaVentas[contador3], ListaVentas[contador3+1], ListaVentas[contador3+2], ListaVentas[contador3+3], ListaVentas[contador3+4])
                    contador3 += 5
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
        elif len(ListaVentas) == 0:
            print("""\nNo hay data creada para 'Ventas'. Vuelva a intentarlo más tarde, por favor.\n
   Menú CRUD
*--------------*
|1.| Crear
|2.| Leer
|3.| Actualizar
|4.| Eliminar
*--------------*""")
            Menus(0)
            
def LeerVideoJuegos():
    contador1 = 0
    contador2 = 0
    contador3 = 0
    contador4 = 1
    prueba = 1
    while True:
        contador1 += 4
        contador2 += 5
        if len(ListaVideoJuegos) == contador2:
            operacion1 = contador2-contador1
            print(f"Se encontraron: {operacion1} videojuego/s.\n")
            for a in range(0,(operacion1)+1):
                if prueba:
                    print("""      Nombre  |  Tipo  |  Precio""")
                    prueba = 0
                else:
                    print("*---*------------------------------------------------------------*")
                    print(f"|{contador4}.-|",ListaVideoJuegos[contador3], ListaVideoJuegos[contador3+1], ListaVideoJuegos[contador3+2])
                    contador3 += 5
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
        elif len(ListaVideoJuegos) == 0:
            print("""\nNo hay data creada para 'Ventas'. Vuelva a intentarlo más tarde, por favor.\n
   Menú CRUD
*--------------*
|1.| Crear
|2.| Leer
|3.| Actualizar
|4.| Eliminar
*--------------*""")
            Menus(0)
        
def Leer(c, control1, control2, control3, control4, control5):
    if c == 1:
        contador1 = 0
        contador2 = 0
        contador3 = 0
        contador4 = 1
        prueba = 1
        while True:
            contador1 += 3
            contador2 += 4

            if len(ListaClientes) == contador2:
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

    # ============================== ============================== ============================= ACTUALIZAR LOS CLIENTES (GUARDARLOS ACTUALIZADOS O NO) ============================== ============================== ============================= ============================= ============================= ============================= ============================= =============================
    if c == 0:
        ListaActualizarAuxiliar = ListaClientes.copy()
        ListaClientes.clear()
        if len(ListaActualizarAuxiliar) == 4:
            # ============= Cliente 1 ============= #
            if control1: ListaClientes.append(ListaActualizar1[0]) ,ListaClientes.append(ListaActualizar1[1]) ,ListaClientes.append(ListaActualizar1[2]) ,ListaClientes.append(ListaActualizar1[3])
            else: ListaClientes.append(ListaActualizarAuxiliar[0]),ListaClientes.append(ListaActualizarAuxiliar[1]),ListaClientes.append(ListaActualizarAuxiliar[2]),ListaClientes.append(ListaActualizarAuxiliar[3])
            
        elif len(ListaActualizarAuxiliar) == 8:
            # ============= Cliente 1 ============= #
            if control1: ListaClientes.append(ListaActualizar1[0]) ,ListaClientes.append(ListaActualizar1[1]) ,ListaClientes.append(ListaActualizar1[2]) ,ListaClientes.append(ListaActualizar1[3])
            else: ListaClientes.append(ListaActualizarAuxiliar[0]),ListaClientes.append(ListaActualizarAuxiliar[1]),ListaClientes.append(ListaActualizarAuxiliar[2]),ListaClientes.append(ListaActualizarAuxiliar[3])
                
            # ============= Cliente 2 ============= #
            if control2: ListaClientes.append(ListaActualizar2[0]) ,ListaClientes.append(ListaActualizar2[1]) ,ListaClientes.append(ListaActualizar2[2]) ,ListaClientes.append(ListaActualizar2[3])
            else: ListaClientes.append(ListaActualizarAuxiliar[4]),ListaClientes.append(ListaActualizarAuxiliar[5]),ListaClientes.append(ListaActualizarAuxiliar[6]),ListaClientes.append(ListaActualizarAuxiliar[7])
                
        elif len(ListaActualizarAuxiliar) == 12:
            # ============= Cliente 1 ============= #
            if control1: ListaClientes.append(ListaActualizar1[0]) ,ListaClientes.append(ListaActualizar1[1]) ,ListaClientes.append(ListaActualizar1[2]) ,ListaClientes.append(ListaActualizar1[3])
            else: ListaClientes.append(ListaActualizarAuxiliar[0]),ListaClientes.append(ListaActualizarAuxiliar[1]),ListaClientes.append(ListaActualizarAuxiliar[2]),ListaClientes.append(ListaActualizarAuxiliar[3])
            
            # ============= Cliente 2 ============= #
            if control2: ListaClientes.append(ListaActualizar2[0]) ,ListaClientes.append(ListaActualizar2[1]) ,ListaClientes.append(ListaActualizar2[2]) ,ListaClientes.append(ListaActualizar2[3])
            else: ListaClientes.append(ListaActualizarAuxiliar[4]),ListaClientes.append(ListaActualizarAuxiliar[5]),ListaClientes.append(ListaActualizarAuxiliar[6]),ListaClientes.append(ListaActualizarAuxiliar[7])
            
            # ============= Cliente 3 ============= #    
            if control3: ListaClientes.append(ListaActualizar3[0]) ,ListaClientes.append(ListaActualizar3[1]) ,ListaClientes.append(ListaActualizar3[2]) ,ListaClientes.append(ListaActualizar3[3])
            else: ListaClientes.append(ListaActualizarAuxiliar[8]),ListaClientes.append(ListaActualizarAuxiliar[9]),ListaClientes.append(ListaActualizarAuxiliar[10]),ListaClientes.append(ListaActualizarAuxiliar[11])
                
        elif len(ListaActualizarAuxiliar) == 16:
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
                
        elif len(ListaActualizarAuxiliar) == 20:
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

    # ============================== ============================== ============================= ACTUALIZAR LAS VENTAS (GUARDARLAS ACTUALIZADAS O NO) ============================== ============================== ============================= ============================= ============================= ============================= ============================= =============================
    elif c == 3:
        ListaActualizarAuxiliarVentas = ListaVentas.copy()
        ListaVentas.clear()
        if len(ListaActualizarAuxiliarVentas) == 5:
            # ============= Venta 1 ============= #
            if control1: ListaVentas.append(ListaActualizarVentas1[0]) ,ListaVentas.append(ListaActualizarVentas1[1]) ,ListaVentas.append(ListaActualizarVentas1[2]) ,ListaVentas.append(ListaActualizarVentas1[3]),ListaVentas.append(ListaActualizarVentas1[4])
            else: ListaVentas.append(ListaActualizarAuxiliarVentas[0]) ,ListaVentas.append(ListaActualizarAuxiliarVentas[1]),ListaVentas.append(ListaActualizarAuxiliarVentas[2]),ListaVentas.append(ListaActualizarAuxiliarVentas[3]),ListaVentas.append(ListaActualizarAuxiliarVentas[4])
            
        elif len(ListaActualizarAuxiliarVentas) == 10:
            # ============= Venta 1 ============= #
            if control1: ListaVentas.append(ListaActualizarVentas1[0]) ,ListaVentas.append(ListaActualizarVentas1[1]) ,ListaVentas.append(ListaActualizarVentas1[2]) ,ListaVentas.append(ListaActualizarVentas1[3]),ListaVentas.append(ListaActualizarVentas1[4])
            else: ListaVentas.append(ListaActualizarAuxiliarVentas[0]),ListaVentas.append(ListaActualizarAuxiliarVentas[1]),ListaVentas.append(ListaActualizarAuxiliarVentas[2]),ListaVentas.append(ListaActualizarAuxiliarVentas[3]),ListaVentas.append(ListaActualizarAuxiliarVentas[4])
                
            # ============= Venta 2 ============= #
            if control2: ListaVentas.append(ListaActualizarVentas2[0]) ,ListaVentas.append(ListaActualizarVentas2[1]) ,ListaVentas.append(ListaActualizarVentas2[2]) ,ListaVentas.append(ListaActualizarVentas2[3]),ListaVentas.append(ListaActualizarVentas2[4])
            else: ListaVentas.append(ListaActualizarAuxiliarVentas[5]),ListaVentas.append(ListaActualizarAuxiliarVentas[6]),ListaVentas.append(ListaActualizarAuxiliarVentas[7]),ListaVentas.append(ListaActualizarAuxiliarVentas[8]),ListaVentas.append(ListaActualizarAuxiliarVentas[9])
                
        elif len(ListaActualizarAuxiliarVentas) == 15:
            # ============= Venta 1 ============= #
            if control1: ListaVentas.append(ListaActualizarVentas1[0]) ,ListaVentas.append(ListaActualizarVentas1[1]) ,ListaVentas.append(ListaActualizarVentas1[2]) ,ListaVentas.append(ListaActualizarVentas1[3]),ListaVentas.append(ListaActualizarVentas1[4])
            else: ListaVentas.append(ListaActualizarAuxiliarVentas[0]) ,ListaVentas.append(ListaActualizarAuxiliarVentas[1]),ListaVentas.append(ListaActualizarAuxiliarVentas[2]),ListaVentas.append(ListaActualizarAuxiliarVentas[3]),ListaVentas.append(ListaActualizarAuxiliarVentas[4])
            
            # ============= Venta 2 ============= #
            if control2: ListaVentas.append(ListaActualizarVentas2[0]) ,ListaVentas.append(ListaActualizarVentas2[1]) ,ListaVentas.append(ListaActualizarVentas2[2]) ,ListaVentas.append(ListaActualizarVentas2[3]),ListaVentas.append(ListaActualizarVentas2[4])
            else: ListaVentas.append(ListaActualizarAuxiliarVentas[5]),ListaVentas.append(ListaActualizarAuxiliarVentas[6]),ListaVentas.append(ListaActualizarAuxiliarVentas[7]),ListaVentas.append(ListaActualizarAuxiliarVentas[8]),ListaVentas.append(ListaActualizarAuxiliarVentas[9])
            
            # ============= Venta 3 ============= #    
            if control3: ListaVentas.append(ListaActualizarVentas3[0]) ,ListaVentas.append(ListaActualizarVentas3[1]) ,ListaVentas.append(ListaActualizarVentas3[2]) ,ListaVentas.append(ListaActualizarVentas3[3]),ListaVentas.append(ListaActualizarVentas3[4])
            else: ListaVentas.append(ListaActualizarAuxiliarVentas[10]),ListaVentas.append(ListaActualizarAuxiliarVentas[11]),ListaVentas.append(ListaActualizarAuxiliarVentas[12]),ListaVentas.append(ListaActualizarAuxiliarVentas[13]),ListaVentas.append(ListaActualizarAuxiliarVentas[14])
                
        elif len(ListaActualizarAuxiliarVentas) == 20:
            # ============= Venta 1 ============= #
            if control1: ListaVentas.append(ListaActualizarVentas1[0]) ,ListaVentas.append(ListaActualizarVentas1[1]) ,ListaVentas.append(ListaActualizarVentas1[2]) ,ListaVentas.append(ListaActualizarVentas1[3]),ListaVentas.append(ListaActualizarVentas1[4])
            else: ListaVentas.append(ListaActualizarAuxiliarVentas[0]) ,ListaVentas.append(ListaActualizarAuxiliarVentas[1]),ListaVentas.append(ListaActualizarAuxiliarVentas[2]),ListaVentas.append(ListaActualizarAuxiliarVentas[3]),ListaVentas.append(ListaActualizarAuxiliarVentas[4])
            
            # ============= Venta 2 ============= #
            if control2: ListaVentas.append(ListaActualizarVentas2[0]) ,ListaVentas.append(ListaActualizarVentas2[1]),ListaVentas.append(ListaActualizarVentas2[2]) ,ListaVentas.append(ListaActualizarVentas2[3]),ListaVentas.append(ListaActualizarVentas2[4])
            else: ListaVentas.append(ListaActualizarAuxiliarVentas[5]),ListaVentas.append(ListaActualizarAuxiliarVentas[6]),ListaVentas.append(ListaActualizarAuxiliarVentas[7]),ListaVentas.append(ListaActualizarAuxiliarVentas[8]),ListaVentas.append(ListaActualizarAuxiliarVentas[9])
            
            # ============= Venta 3 ============= #    
            if control3: ListaVentas.append(ListaActualizarVentas3[0]) ,ListaVentas.append(ListaActualizarVentas3[1]) ,ListaVentas.append(ListaActualizarVentas3[2]) ,ListaVentas.append(ListaActualizarVentas3[3]),ListaVentas.append(ListaActualizarVentas3[4])
            else: ListaVentas.append(ListaActualizarAuxiliarVentas[10]),ListaVentas.append(ListaActualizarAuxiliarVentas[11]),ListaVentas.append(ListaActualizarAuxiliarVentas[12]),ListaVentas.append(ListaActualizarAuxiliarVentas[13]),ListaVentas.append(ListaActualizarAuxiliarVentas[14])
            
            # ============= Venta 4 ============= #    
            if control4: ListaVentas.append(ListaActualizarVentas4[0]) ,ListaVentas.append(ListaActualizarVentas4[1]) ,ListaVentas.append(ListaActualizarVentas4[2]),ListaVentas.append(ListaActualizarVentas4[3]),ListaVentas.append(ListaActualizarVentas4[4])
            else: ListaVentas.append(ListaActualizarAuxiliarVentas[15]),ListaVentas.append(ListaActualizarAuxiliarVentas[16]),ListaVentas.append(ListaActualizarAuxiliarVentas[17]),ListaVentas.append(ListaActualizarAuxiliarVentas[18]),ListaVentas.append(ListaActualizarAuxiliarVentas[19])
                
        elif len(ListaActualizarAuxiliarVentas) == 25:
            # ============= Venta 1 ============= #
            if control1: ListaVentas.append(ListaActualizarVentas1[0]) ,ListaVentas.append(ListaActualizarVentas1[1]) ,ListaVentas.append(ListaActualizarVentas1[2]) ,ListaVentas.append(ListaActualizarVentas1[3]),ListaVentas.append(ListaActualizarVentas1[4])
            else: ListaVentas.append(ListaActualizarAuxiliarVentas[0]) ,ListaVentas.append(ListaActualizarAuxiliarVentas[1]),ListaVentas.append(ListaActualizarAuxiliarVentas[2]),ListaVentas.append(ListaActualizarAuxiliarVentas[3]),ListaVentas.append(ListaActualizarAuxiliarVentas[4])
            
            # ============= Venta 2 ============= #
            if control2: ListaVentas.append(ListaActualizarVentas2[0]),ListaVentas.append(ListaActualizarVentas2[1]),ListaVentas.append(ListaActualizarVentas2[2]),ListaVentas.append(ListaActualizarVentas2[3]),ListaVentas.append(ListaActualizarVentas2[4])
            else: ListaVentas.append(ListaActualizarAuxiliarVentas[5]),ListaVentas.append(ListaActualizarAuxiliarVentas[6]),ListaVentas.append(ListaActualizarAuxiliarVentas[7]),ListaVentas.append(ListaActualizarAuxiliarVentas[8]),ListaVentas.append(ListaActualizarAuxiliarVentas[9])
            
            # ============= Venta 3 ============= #    
            if control3: ListaVentas.append(ListaActualizarVentas3[0]) ,ListaVentas.append(ListaActualizarVentas3[1]) ,ListaVentas.append(ListaActualizarVentas3[2]) ,ListaVentas.append(ListaActualizarVentas3[3]),ListaVentas.append(ListaActualizarVentas3[4])
            else: ListaVentas.append(ListaActualizarAuxiliarVentas[10]),ListaVentas.append(ListaActualizarAuxiliarVentas[11]),ListaVentas.append(ListaActualizarAuxiliarVentas[12]),ListaVentas.append(ListaActualizarAuxiliarVentas[13]),ListaVentas.append(ListaActualizarAuxiliarVentas[14]) 
               
            # ============= Venta 4 ============= #    
            if control4: ListaVentas.append(ListaActualizarVentas4[0]),ListaVentas.append(ListaActualizarVentas4[1]),ListaVentas.append(ListaActualizarVentas4[2]),ListaVentas.append(ListaActualizarVentas4[3]),ListaVentas.append(ListaActualizarVentas4[4])
            else: ListaVentas.append(ListaActualizarAuxiliarVentas[15]),ListaVentas.append(ListaActualizarAuxiliarVentas[16]),ListaVentas.append(ListaActualizarAuxiliarVentas[17]),ListaVentas.append(ListaActualizarAuxiliarVentas[18]),ListaVentas.append(ListaActualizarAuxiliarVentas[19])
            
            # ============= Venta 5 ============= #
            if control5: ListaVentas.append(ListaActualizarVentas5[0]),ListaVentas.append(ListaActualizarVentas5[1]),ListaVentas.append(ListaActualizarVentas5[2]),ListaVentas.append(ListaActualizarVentas5[3]),ListaVentas.append(ListaActualizarVentas5[4])
            else: ListaVentas.append(ListaActualizarAuxiliarVentas[20]),ListaVentas.append(ListaActualizarAuxiliarVentas[21]),ListaVentas.append(ListaActualizarAuxiliarVentas[22]),ListaVentas.append(ListaActualizarAuxiliarVentas[23]),ListaVentas.append(ListaActualizarAuxiliarVentas[24])
    
    # ============================== ============================== ============================= ACTUALIZAR LOS VIDEOJUEGOS (GUARDARLOS ACTUALIZADOS O NO) ============================== ============================== ============================= ============================= ============================= ============================= ============================= =============================
    elif c == 4:
        if len(ListaActualizarAuxiliarVideoJuegos) == 3:
            # ============= Videojuego 1 ============= #
            if control1: ListaVideoJuegos.append(ListaActualizarVideoJuegos1[0]) ,ListaVideoJuegos.append(ListaActualizarVideoJuegos1[1]) ,ListaVideoJuegos.append(ListaActualizarVideoJuegos1[2])
            else: ListaVideoJuegos.append(ListaActualizarAuxiliarVideoJuegos[0]),ListaVideoJuegos.append(ListaActualizarAuxiliarVideoJuegos[1]),ListaVideoJuegos.append(ListaActualizarAuxiliarVideoJuegos[2])
        elif len(ListaActualizarAuxiliarVideoJuegos) == 6:
            # ============= Videojuego 1 ============= #
            if control1: ListaVideoJuegos.append(ListaActualizarVideoJuegos1[0]) ,ListaVideoJuegos.append(ListaActualizarVideoJuegos1[1]) ,ListaVideoJuegos.append(ListaActualizarVideoJuegos1[2])
            else: ListaVideoJuegos.append(ListaActualizarAuxiliarVideoJuegos[0]),ListaVideoJuegos.append(ListaActualizarAuxiliarVideoJuegos[1]),ListaVideoJuegos.append(ListaActualizarAuxiliarVideoJuegos[2])
                
            # ============= Videojuego 2 ============= #
            if control2: ListaVideoJuegos.append(ListaActualizarVideoJuegos2[0]) ,ListaVideoJuegos.append(ListaActualizarVideoJuegos2[1]) ,ListaVideoJuegos.append(ListaActualizarVideoJuegos2[2])
            else: ListaVideoJuegos.append(ListaActualizarAuxiliarVideoJuegos[3]),ListaVideoJuegos.append(ListaActualizarAuxiliarVideoJuegos[4]),ListaVideoJuegos.append(ListaActualizarAuxiliarVideoJuegos[5])
                
        elif len(ListaActualizarAuxiliarVideoJuegos) == 9:
            # ============= Videojuego 1 ============= #
            if control1: ListaVideoJuegos.append(ListaActualizarVideoJuegos1[0]) ,ListaVideoJuegos.append(ListaActualizarVideoJuegos1[1]) ,ListaVideoJuegos.append(ListaActualizarVideoJuegos1[2])
            else: ListaVideoJuegos.append(ListaActualizarAuxiliarVideoJuegos[0]),ListaVideoJuegos.append(ListaActualizarAuxiliarVideoJuegos[1]),ListaVideoJuegos.append(ListaActualizarAuxiliarVideoJuegos[2])
            
            # ============= Videojuego 2 ============= #
            if control2: ListaVideoJuegos.append(ListaActualizarVideoJuegos2[0]) ,ListaVideoJuegos.append(ListaActualizarVideoJuegos2[1]) ,ListaVideoJuegos.append(ListaActualizarVideoJuegos2[2])
            else: ListaVideoJuegos.append(ListaActualizarAuxiliarVideoJuegos[3]),ListaVideoJuegos.append(ListaActualizarAuxiliarVideoJuegos[4]),ListaVideoJuegos.append(ListaActualizarAuxiliarVideoJuegos[5])
            
            # ============= Videojuego 3 ============= #    
            if control3: ListaVideoJuegos.append(ListaActualizarVideoJuegos3[0]) ,ListaVideoJuegos.append(ListaActualizarVideoJuegos3[1]) ,ListaVideoJuegos.append(ListaActualizarVideoJuegos3[2])
            else: ListaVideoJuegos.append(ListaActualizarAuxiliarVideoJuegos[6]),ListaVideoJuegos.append(ListaActualizarAuxiliarVideoJuegos[7]),ListaVideoJuegos.append(ListaActualizarAuxiliarVideoJuegos[8])
                
        elif len(ListaActualizarAuxiliarVideoJuegos) == 12:
            # ============= Videojuego 1 ============= #
            if control1: ListaVideoJuegos.append(ListaActualizarVideoJuegos1[0]) ,ListaVideoJuegos.append(ListaActualizarVideoJuegos1[1]) ,ListaVideoJuegos.append(ListaActualizarVideoJuegos1[2])
            else: ListaVideoJuegos.append(ListaActualizarAuxiliarVideoJuegos[0]),ListaVideoJuegos.append(ListaActualizarAuxiliarVideoJuegos[1]),ListaVideoJuegos.append(ListaActualizarAuxiliarVideoJuegos[2])
            
            # ============= Videojuego 2 ============= #
            if control2: ListaVideoJuegos.append(ListaActualizarVideoJuegos2[0]) ,ListaVideoJuegos.append(ListaActualizarVideoJuegos2[1]) ,ListaVideoJuegos.append(ListaActualizarVideoJuegos2[2])
            else: ListaVideoJuegos.append(ListaActualizarAuxiliarVideoJuegos[3]),ListaVideoJuegos.append(ListaActualizarAuxiliarVideoJuegos[4]),ListaVideoJuegos.append(ListaActualizarAuxiliarVideoJuegos[5])
            
            # ============= Videojuego 3 ============= #    
            if control3: ListaVideoJuegos.append(ListaActualizarVideoJuegos3[0]) ,ListaVideoJuegos.append(ListaActualizarVideoJuegos3[1]) ,ListaVideoJuegos.append(ListaActualizarVideoJuegos3[2])
            else: ListaVideoJuegos.append(ListaActualizarAuxiliarVideoJuegos[6]),ListaVideoJuegos.append(ListaActualizarAuxiliarVideoJuegos[7]),ListaVideoJuegos.append(ListaActualizarAuxiliarVideoJuegos[8])
            
            # ============= Videojuego 4 ============= #    
            if control4: ListaVideoJuegos.append(ListaActualizarVideoJuegos4[0]) ,ListaVideoJuegos.append(ListaActualizarVideoJuegos4[1]) ,ListaVideoJuegos.append(ListaActualizarVideoJuegos4[2]) 
            else: ListaVideoJuegos.append(ListaActualizarAuxiliarVideoJuegos[9]),ListaVideoJuegos.append(ListaActualizarAuxiliarVideoJuegos[10]),ListaVideoJuegos.append(ListaActualizarAuxiliarVideoJuegos[11])
                
        elif len(ListaActualizarAuxiliarVideoJuegos) == 15:
            # ============= Videojuego 1 ============= #
            if control1: ListaVideoJuegos.append(ListaActualizarVideoJuegos1[0]) ,ListaVideoJuegos.append(ListaActualizarVideoJuegos1[1]) ,ListaVideoJuegos.append(ListaActualizarVideoJuegos1[2])
            else: ListaVideoJuegos.append(ListaActualizarAuxiliarVideoJuegos[0]),ListaVideoJuegos.append(ListaActualizarAuxiliarVideoJuegos[1]),ListaVideoJuegos.append(ListaActualizarAuxiliarVideoJuegos[2])
            
            # ============= Videojuego 2 ============= #
            if control2: ListaVideoJuegos.append(ListaActualizarVideoJuegos2[0]) ,ListaVideoJuegos.append(ListaActualizarVideoJuegos2[1]) ,ListaVideoJuegos.append(ListaActualizarVideoJuegos2[2])
            else: ListaVideoJuegos.append(ListaActualizarAuxiliarVideoJuegos[3]),ListaVideoJuegos.append(ListaActualizarAuxiliarVideoJuegos[4]),ListaVideoJuegos.append(ListaActualizarAuxiliarVideoJuegos[5])
            
            # ============= Videojuego 3 ============= #    
            if control3: ListaVideoJuegos.append(ListaActualizarVideoJuegos3[0]) ,ListaVideoJuegos.append(ListaActualizarVideoJuegos3[1]) ,ListaVideoJuegos.append(ListaActualizarVideoJuegos3[2])
            else: ListaVideoJuegos.append(ListaActualizarAuxiliarVideoJuegos[6]),ListaVideoJuegos.append(ListaActualizarAuxiliarVideoJuegos[7]),ListaVideoJuegos.append(ListaActualizarAuxiliarVideoJuegos[8])
               
            # ============= Videojuego 4 ============= #    
            if control4: ListaVideoJuegos.append(ListaActualizarVideoJuegos4[0]) ,ListaVideoJuegos.append(ListaActualizarVideoJuegos4[1]) ,ListaVideoJuegos.append(ListaActualizarVideoJuegos4[2]) 
            else: ListaVideoJuegos.append(ListaActualizarAuxiliarVideoJuegos[9]),ListaVideoJuegos.append(ListaActualizarAuxiliarVideoJuegos[10]),ListaVideoJuegos.append(ListaActualizarAuxiliarVideoJuegos[11])
            
            # ============= Videojuego 5 ============= #
            if control5: ListaVideoJuegos.append(ListaActualizarVideoJuegos5[0]),ListaVideoJuegos.append(ListaActualizarVideoJuegos5[1]),ListaVideoJuegos.append(ListaActualizarVideoJuegos5[2])
            else: ListaVideoJuegos.append(ListaActualizarAuxiliarVideoJuegos[12]),ListaVideoJuegos.append(ListaActualizarAuxiliarVideoJuegos[13]),ListaVideoJuegos.append(ListaActualizarAuxiliarVideoJuegos[14])
            
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
|2.-| Ventas Ventas CSV 
*---------------------------*
""")

    def elegirOpcionEnMenu(x, y):
        while True:
# ---------------------------------------------------------------- CLIENTES MENU 1 ---------------------------------------------------------------- #
            if x == 1 and y == 1: # CONFIGURACION MENU 1 EN CLIENTES
                eleccionCRUD = int(input("¿Qué desea hacer?\n> "))
                if eleccionCRUD == 0:
                    print(f"Lo siento, el '{eleccionCRUD}' no se encuentra en el menú. \n")
                elif eleccionCRUD >= 1 and eleccionCRUD <= 4:
# ================================================================= Crear =================================================================== #
                    if eleccionCRUD == 1:
                        contador = 0
                        while True:
                            try:
                                CantidadClientes = int(input("Cantidad de clientes a registrar: \n> "))
                                break
                            except ValueError:
                                print("No aceptamos data basura.")
                                continue
                            
                        while True:
                            try:
                                while CantidadClientes != contador:
                                    print(f"\nCliente: {contador+1}")
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
# ================================================================= LEER =================================================================== #
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
                        
# ================================================================= Actualizar =================================================================== #
                    elif eleccionCRUD == 3:
                        print("¿Quieres primero leer la data para saber cuál vas actualizar? \nPresiona '1' para Sí y presiona '0' para No")
                        while True:
                            eleccionData = int(input("> "))
                            if eleccionData:
                                Leer(1,0,0,0,0,0)
                            else:
                                if len(ListaClientes) == 0:
                                    print("Lo siento, pero no hay data creada. Vuelve a intentarlo después de crearla con el Menú CRUD opción 1.\n")
                                    break
                                else:
                                    contador = 0
                                    control1 = 0
                                    control2 = 0
                                    control3 = 0
                                    control4 = 0
                                    control5 = 0
                                    ControlVueltas1 = 0
                                    ControlVueltas2 = 0
                                    ControlVueltas3 = 0
                                    ControlVueltas4 = 0
                                    ControlVueltas5 = 0
                                    
                                    while True:
                                        contador += 1
                                        print("\nPara dejar de actualizar y guardar todas las actualizaciones, presionar: '6'")
                                        eleccionUsuarioActualizar = int(input("¿Cuál quieres actualizar?\nIngresa el número: "))
#==================================================================================ACTUALIZACION CLIENTE 1==================================================================================================================================== #
                                        if eleccionUsuarioActualizar == 1:
                                            if ControlVueltas1 >= 1:
                                                print("\nOJO: DEBES GUARDAR LA ACTUALIZACIÓN ANTES DE VOLVER ACTUALIZAR EL MISMO USUARIO.")
                                                continue
                                            else:
                                                print(f"El cliente seleccionado es (sin actualizar): {ListaClientes[0]} {ListaClientes[1]} {ListaClientes[2]} {ListaClientes[3]}")
                                                print("¿Seguro que quieres actualizar este cliente?\n '1' para Sí y '0' para No.")
                                                respuestaSioNo = int(input("> "))
                                            while respuestaSioNo:
                                                if respuestaSioNo:
                                                    print("|1.-| Cédula\n|2.-| Nombre\n|3.-| Apellidos\n|4.-| Método de pago\n|5.-| Dejar actualizar")
                                                    UsuarioQuiereActualizarEl = input(f"¿Qué quiere actualizar del cliente {eleccionUsuarioActualizar}?\n> ")
                                                    if UsuarioQuiereActualizarEl == "1": # ACTUALIZAR CEDULA DEL CLIENTE
                                                        
                                                        print(f"Ha seleccionado el cliente {eleccionUsuarioActualizar}, para actualizar la cédula.\n")
                                                        nuevaCedula = int(input("Ingrese la nueva cédula: "))
                                                        NuevaCedulaEnString = str(nuevaCedula)
                                                        ListaActualizar1.clear()
                                                        ListaActualizar1.append(NuevaCedulaEnString)
                                                        ListaActualizar1.append(ListaClientes[1])
                                                        ListaActualizar1.append(ListaClientes[2])
                                                        ListaActualizar1.append(ListaClientes[3])
                                                        print(f"Cédula actualizada éxitosamente...\Cliente: {ListaActualizar1[0]} {ListaActualizar1[1]} {ListaActualizar1[2]} {ListaActualizar1[3]}")
                                                        control1 = 1
                                                        ControlVueltas1 += 1
                                                        break
                                                    elif UsuarioQuiereActualizarEl == "2": # ACTUALIZAR NOMBRE DEL CLIENTE
                                                        print(f"Ha seleccionado el CLiente {eleccionUsuarioActualizar}, para actualizar el nombre.\n")
                                                        nuevoNombre = input("Ingrese el nuevo nombre: ")
                                                        ListaActualizar1.clear()
                                                        ListaActualizar1.append(ListaClientes[0])
                                                        ListaActualizar1.append(nuevoNombre)
                                                        ListaActualizar1.append(ListaClientes[2])
                                                        ListaActualizar1.append(ListaClientes[3])
                                                        print(f"Nombre actualizado éxitosamente...\nCliente: {ListaActualizar1[0]} {ListaActualizar1[1]} {ListaActualizar1[2]} {ListaActualizar1[3]}")
                                                        control1 = 1
                                                        ControlVueltas1 += 1
                                                        break
                                                    elif UsuarioQuiereActualizarEl == "3": # ACTUALIZAR APELLIDO DEL CLIENTE
                                                        print(f"Ha seleccionado el cliente {eleccionUsuarioActualizar}, para actualizar el apellido.\n")
                                                        nuevoApellido = input("Ingrese el nuevo apellido: ")
                                                        ListaActualizar1.clear()                                                          
                                                        ListaActualizar1.append(ListaClientes[0])
                                                        ListaActualizar1.append(ListaClientes[1])
                                                        ListaActualizar1.append(nuevoApellido)
                                                        ListaActualizar1.append(ListaClientes[3])
                                                        print(f"Apellido actualizado éxitosamente...\nCliente: {ListaActualizar1[0]} {ListaActualizar1[1]} {ListaActualizar1[2]} {ListaActualizar1[3]}")
                                                        control1 = 1
                                                        ControlVueltas1 += 1
                                                        break
                                                    elif UsuarioQuiereActualizarEl == "4": # ACTUALIZAR MÉTODO DEL CLIENTE
                                                        print(f"Ha seleccionado el cliente {eleccionUsuarioActualizar}, para actualizar el método de pago.\n")
                                                        nuevoMetodo = input("Ingrese el nuevo método. '1' para pagar con tarjeta de crédito o débito. '2' para pagar en efectivo.\n> ")
                                                        if nuevoMetodo == "1":
                                                            nuevoMetodoActualizado = "Tarjeta de crédito o débito"
                                                        elif nuevoMetodo == "2":
                                                            nuevoMetodoActualizado = "Efectivo"  
                                                        ListaActualizar1.clear()                                                          
                                                        ListaActualizar1.append(ListaClientes[0])
                                                        ListaActualizar1.append(ListaClientes[1])
                                                        ListaActualizar1.append(ListaClientes[2])
                                                        ListaActualizar1.append(nuevoMetodoActualizado)
                                                        print(f"Método de pago actualizado éxitosamente...\nCliente: {ListaActualizar1[0]} {ListaActualizar1[1]} {ListaActualizar1[2]} {ListaActualizar1[3]}")
                                                        control1 = 1
                                                        ControlVueltas1 += 1
                                                        break
                                                    elif UsuarioQuiereActualizarEl == "5":
                                                        break
                                                    
#==================================================================================ACTUALIZACION CLIENTE 2==================================================================================================================================== #
                                        elif eleccionUsuarioActualizar == 2:
                                            if ControlVueltas2 >= 1:
                                                print("\nOJO: DEBES GUARDAR LA ACTUALIZACIÓN ANTES DE VOLVER ACTUALIZAR EL MISMO USUARIO.")
                                                continue
                                            else:
                                                print(f"El cliente seleccionado es: {ListaClientes[4]} {ListaClientes[5]} {ListaClientes[6]} {ListaClientes[7]}")
                                                print("¿Seguro que quieres actualizar este cliente?\n '1' para Sí y '0' para No.")
                                            respuestaSioNo = int(input("> "))
                                            while respuestaSioNo:
                                                if respuestaSioNo:
                                                    print("|1.-| Cédula\n|2.-| Nombre\n|3.-| Apellidos\n|4.-| Método de pago\n|5.-| Dejar actualizar")
                                                    UsuarioQuiereActualizarEl = input(f"¿Qué quiere actualizar del cliente {eleccionUsuarioActualizar}?\n> ")
                                                    if UsuarioQuiereActualizarEl == "1": # ACTUALIZAR CEDULA DEL CLIENTE
                                                        print(f"Ha seleccionado el cliente {eleccionUsuarioActualizar}, para actualizar la cédula.\n")
                                                        nuevaCedula = int(input("Ingrese la nueva cédula: "))
                                                        NuevaCedulaEnString = str(nuevaCedula)
                                                        ListaActualizar2.clear()
                                                        ListaActualizar2.append(NuevaCedulaEnString)
                                                        ListaActualizar2.append(ListaClientes[5])
                                                        ListaActualizar2.append(ListaClientes[6])
                                                        ListaActualizar2.append(ListaClientes[7])
                                                        print(f"Cédula actualizada éxitosamente...\nCliente: {ListaActualizar2[0]} {ListaActualizar2[1]} {ListaActualizar2[2]} {ListaActualizar2[3]}")
                                                        control2 = 1
                                                        ControlVueltas2 += 1
                                                        break
                                                    elif UsuarioQuiereActualizarEl == "2": # ACTUALIZAR NOMBRE DEL CLIENTE
                                                        print(f"Ha seleccionado el cliente {eleccionUsuarioActualizar}, para actualizar el nombre.\n")
                                                        nuevoNombre = input("Ingrese el nuevo nombre: ")
                                                        ListaActualizar2.clear()
                                                        ListaActualizar2.append(ListaClientes[4])
                                                        ListaActualizar2.append(nuevoNombre)
                                                        ListaActualizar2.append(ListaClientes[6])
                                                        ListaActualizar2.append(ListaClientes[7])
                                                        print(f"Nombre actualizado éxitosamente...\nCliente: {ListaActualizar2[0]} {ListaActualizar2[1]} {ListaActualizar2[2]} {ListaActualizar2[3]}")
                                                        control2 = 1
                                                        ControlVueltas2 += 1
                                                        break
                                                    elif UsuarioQuiereActualizarEl == "3": # ACTUALIZAR APELLIDO DEL CLIENTE
                                                        print(f"Ha seleccionado el cliente {eleccionUsuarioActualizar}, para actualizar el apellido.\n")
                                                        nuevoApellido = input("Ingrese el nuevo apellido: ")
                                                        ListaActualizar2.clear()
                                                        ListaActualizar2.append(ListaClientes[4])
                                                        ListaActualizar2.append(ListaClientes[5])
                                                        ListaActualizar2.append(nuevoApellido)
                                                        ListaActualizar2.append(ListaClientes[7])
                                                        print(f"Apellido actualizado éxitosamente...\nCliente: {ListaActualizar2[0]} {ListaActualizar2[1]} {ListaActualizar2[2]} {ListaActualizar2[3]}")
                                                        control2 = 1
                                                        ControlVueltas2 += 1
                                                        break
                                                    elif UsuarioQuiereActualizarEl == "4": # ACTUALIZAR MÉTODO DEL CLIENTE
                                                        print(f"Ha seleccionado el cliente {eleccionUsuarioActualizar}, para actualizar el método de pago.\n")
                                                        nuevoMetodo = input("Ingrese el nuevo método. '1' para pagar con tarjeta de crédito o débito. '2' para pagar en efectivo.\n> ")
                                                        if nuevoMetodo == "1":
                                                            nuevoMetodoActualizado = "Tarjeta de crédito o débito"
                                                        elif nuevoMetodo == "2":
                                                            nuevoMetodoActualizado = "Efectivo"  
                                                        ListaActualizar2.clear()                                                          
                                                        ListaActualizar2.append(ListaClientes[4])
                                                        ListaActualizar2.append(ListaClientes[5])
                                                        ListaActualizar2.append(ListaClientes[6])
                                                        ListaActualizar2.append(nuevoMetodoActualizado)
                                                        print(f"Método de pago actualizado éxitosamente...\nCliente: {ListaActualizar2[0]} {ListaActualizar2[1]} {ListaActualizar2[2]} {ListaActualizar2[3]}")
                                                        control2 = 1
                                                        ControlVueltas2 += 1
                                                        break
                                                    elif UsuarioQuiereActualizarEl == "5":
                                                        break
                                                    
                                                    
                                            else:
                                                print("Lo siento, no hay  esa cantidad de clientes registrados.\n")
#======================================================================================ACTUALIZACION CLIENTE 3================================================================================================================================ #
                                        elif eleccionUsuarioActualizar == 3:
                                            if ControlVueltas3 >= 1:
                                                print("\nOJO: DEBES GUARDAR LA ACTUALIZACIÓN ANTES DE VOLVER ACTUALIZAR EL MISMO USUARIO.")
                                                continue
                                            else:
                                                print(f"El cliente seleccionado es: {ListaClientes[8]} {ListaClientes[9]} {ListaClientes[10]} {ListaClientes[11]}")
                                                print("¿Seguro que quieres actualizar este cliente?\n '1' para Sí y '0' para No.")
                                            respuestaSioNo = int(input("> "))
                                            while respuestaSioNo:
                                                if respuestaSioNo:
                                                    print("|1.-| Cédula\n|2.-| Nombre\n|3.-| Apellidos\n|4.-| Método de pago\n|5.-| Dejar actualizar")
                                                    UsuarioQuiereActualizarEl = input(f"¿Qué quiere actualizar del cliente {eleccionUsuarioActualizar}?\n> ")
                                                    if UsuarioQuiereActualizarEl == "1": # ACTUALIZAR CEDULA DEL CLIENTE
                                                        print(f"Ha seleccionado el cliente {eleccionUsuarioActualizar}, para actualizar la cédula.\n")
                                                        nuevaCedula = int(input("Ingrese la nueva cédula: "))
                                                        NuevaCedulaEnString = str(nuevaCedula)
                                                        ListaActualizar3.clear()
                                                        ListaActualizar3.append(NuevaCedulaEnString)
                                                        ListaActualizar3.append(ListaClientes[9])
                                                        ListaActualizar3.append(ListaClientes[10])
                                                        ListaActualizar3.append(ListaClientes[11])
                                                        print(f"Cédula actualizada éxitosamente...\nCliente: {ListaActualizar3[0]} {ListaActualizar3[1]} {ListaActualizar3[2]} {ListaActualizar3[3]}")
                                                        control3 = 1
                                                        ControlVueltas3 += 1
                                                        break
                                                    elif UsuarioQuiereActualizarEl == "2": # ACTUALIZAR NOMBRE DEL CLIENTE
                                                        print(f"Ha seleccionado el cliente {eleccionUsuarioActualizar}, para actualizar el nombre.\n")
                                                        nuevoNombre = input("Ingrese el nuevo nombre: ")
                                                        ListaActualizar3.clear()
                                                        ListaActualizar3.append(ListaClientes[8])
                                                        ListaActualizar3.append(nuevoNombre)
                                                        ListaActualizar3.append(ListaClientes[10])
                                                        ListaActualizar3.append(ListaClientes[11])
                                                        print(f"Nombre actualizado éxitosamente...\nCliente: {ListaActualizar3[0]} {ListaActualizar3[1]} {ListaActualizar3[2]} {ListaActualizar3[3]}")
                                                        control3 = 1
                                                        ControlVueltas3 += 1
                                                        break
                                                    elif UsuarioQuiereActualizarEl == "3": # ACTUALIZAR APELLIDO DEL CLIENTE
                                                        print(f"Ha seleccionado el cliente {eleccionUsuarioActualizar}, para actualizar el apellido.\n")
                                                        nuevoApellido = input("Ingrese el nuevo apellido: ")
                                                        ListaActualizar3.clear()
                                                        ListaActualizar3.append(ListaClientes[8])
                                                        ListaActualizar3.append(ListaClientes[9])
                                                        ListaActualizar3.append(nuevoApellido)
                                                        ListaActualizar3.append(ListaClientes[11])
                                                        print(f"Apellido actualizado éxitosamente...\nCliente: {ListaActualizar3[0]} {ListaActualizar3[1]} {ListaActualizar3[2]} {ListaActualizar3[3]}")
                                                        control3 = 1
                                                        ControlVueltas3 += 1
                                                        break
                                                    elif UsuarioQuiereActualizarEl == "4": # ACTUALIZAR MÉTODO DEL CLIENTE
                                                        print(f"Ha seleccionado el cliente {eleccionUsuarioActualizar}, para actualizar el método de pago.\n")
                                                        nuevoMetodo = input("Ingrese el nuevo método. '1' para pagar con tarjeta de crédito o débito. '2' para pagar en efectivo.\n> ")
                                                        if nuevoMetodo == "1":
                                                            nuevoMetodoActualizado = "Tarjeta de crédito o débito"
                                                        elif nuevoMetodo == "2":
                                                            nuevoMetodoActualizado = "Efectivo"
                                                        ListaActualizar3.clear()
                                                        ListaActualizar3.append(ListaClientes[8])
                                                        ListaActualizar3.append(ListaClientes[9])
                                                        ListaActualizar3.append(ListaClientes[10])
                                                        ListaActualizar3.append(nuevoMetodoActualizado)
                                                        print(f"Método de pago actualizado éxitosamente...\nCliente: {ListaActualizar3[0]} {ListaActualizar3[1]} {ListaActualizar3[2]} {ListaActualizar3[3]}")
                                                        control3 = 1
                                                        ControlVueltas3 += 1
                                                        break
                                                    elif UsuarioQuiereActualizarEl == "5":
                                                        break
                                                    
                                            else:
                                                print("Lo siento, no hay  esa cantidad de clientes registrados.\n")
#===================================================================================ACTUALIZACION CLIENTE 4=================================================================================================================================== #
                                        elif eleccionUsuarioActualizar == 4:
                                            if ControlVueltas4 >= 1:
                                                print("\nOJO: DEBES GUARDAR LA ACTUALIZACIÓN ANTES DE VOLVER ACTUALIZAR EL MISMO USUARIO.")
                                                continue
                                            else:
                                                print(f"El cliente seleccionado es: {ListaClientes[12]} {ListaClientes[13]} {ListaClientes[14]} {ListaClientes[15]}")
                                                print("¿Seguro que quieres actualizar este cliente?\n '1' para Sí y '0' para No.")
                                            respuestaSioNo = int(input("> "))
                                            while respuestaSioNo:
                                                if respuestaSioNo:
                                                    print("|1.-| Cédula\n|2.-| Nombre\n|3.-| Apellidos\n|4.-| Método de pago\n|5.-| Dejar actualizar")
                                                    UsuarioQuiereActualizarEl = input(f"¿Qué quiere actualizar del cliente {eleccionUsuarioActualizar}?\n> ")
                                                    if UsuarioQuiereActualizarEl == "1": # ACTUALIZAR CEDULA DEL CLIENTE
                                                        print(f"Ha seleccionado el cliente {eleccionUsuarioActualizar}, para actualizar la cédula.\n")
                                                        nuevaCedula = int(input("Ingrese la nueva cédula: "))
                                                        NuevaCedulaEnString = str(nuevaCedula)
                                                        ListaActualizar4.clear()
                                                        ListaActualizar4.append(NuevaCedulaEnString)
                                                        ListaActualizar4.append(ListaClientes[13])
                                                        ListaActualizar4.append(ListaClientes[14])
                                                        ListaActualizar4.append(ListaClientes[15])
                                                        print(f"Cédula actualizada éxitosamente...\nCliente: {ListaActualizar4[0]} {ListaActualizar4[1]} {ListaActualizar4[2]} {ListaActualizar4[3]}")
                                                        control4 = 1
                                                        ControlVueltas4 += 1
                                                        break
                                                    elif UsuarioQuiereActualizarEl == "2": # ACTUALIZAR NOMBRE DEL CLIENTE
                                                        print(f"Ha seleccionado el cliente {eleccionUsuarioActualizar}, para actualizar el nombre.\n")
                                                        nuevoNombre = input("Ingrese el nuevo nombre: ")
                                                        ListaActualizar4.clear()
                                                        ListaActualizar4.append(ListaClientes[12])
                                                        ListaActualizar4.append(nuevoNombre)
                                                        ListaActualizar4.append(ListaClientes[13])
                                                        ListaActualizar4.append(ListaClientes[14])
                                                        print(f"Nombre actualizado éxitosamente...\nCliente: {ListaActualizar4[0]} {ListaActualizar4[1]} {ListaActualizar4[2]} {ListaActualizar4[3]}")
                                                        control4 = 1
                                                        ControlVueltas4 += 1
                                                        break
                                                    elif UsuarioQuiereActualizarEl == "3": # ACTUALIZAR APELLIDO DEL CLIENTE
                                                        print(f"Ha seleccionado el cliente {eleccionUsuarioActualizar}, para actualizar el apellido.\n")
                                                        nuevoApellido = input("Ingrese el nuevo apellido: ")
                                                        ListaActualizar4.clear()
                                                        ListaActualizar4.append(ListaClientes[12])
                                                        ListaActualizar4.append(ListaClientes[13])
                                                        ListaActualizar4.append(nuevoApellido)
                                                        ListaActualizar4.append(ListaClientes[15])
                                                        print(f"Apellido actualizado éxitosamente...\nCliente: {ListaActualizar4[0]} {ListaActualizar4[1]} {ListaActualizar4[2]} {ListaActualizar4[3]}")
                                                        control4 = 1
                                                        ControlVueltas4 += 1
                                                        break
                                                    elif UsuarioQuiereActualizarEl == "4": # ACTUALIZAR MÉTODO DEL CLIENTE
                                                        print(f"Ha seleccionado el cliente {eleccionUsuarioActualizar}, para actualizar el método de pago.\n")
                                                        nuevoMetodo = input("Ingrese el nuevo método. '1' para pagar con tarjeta de crédito o débito. '2' para pagar en efectivo.\n> ")
                                                        if nuevoMetodo == "1":
                                                            nuevoMetodoActualizado = "Tarjeta de crédito o débito"
                                                        elif nuevoMetodo == "2":
                                                            nuevoMetodoActualizado = "Efectivo"                                                            
                                                        ListaActualizar4.clear()
                                                        ListaActualizar4.append(ListaClientes[12])
                                                        ListaActualizar4.append(ListaClientes[13])
                                                        ListaActualizar4.append(ListaClientes[14])
                                                        ListaActualizar4.append(nuevoMetodoActualizado)
                                                        print(f"Método de pago actualizado éxitosamente...\nCliente: {ListaActualizar4[0]} {ListaActualizar4[1]} {ListaActualizar4[2]} {ListaActualizar4[3]}")
                                                        control4 = 1
                                                        ControlVueltas4 += 1
                                                        break
                                                    elif UsuarioQuiereActualizarEl == "5":
                                                        break
#=====================================================================================ACTUALIZACION CLIENTE 5================================================================================================================================= #
                                        elif eleccionUsuarioActualizar == 5:
                                            if ControlVueltas5 >= 1:
                                                print("\nOJO: DEBES GUARDAR LA ACTUALIZACIÓN ANTES DE VOLVER ACTUALIZAR EL MISMO USUARIO.")
                                                continue
                                            else:
                                                print(f"El cliente seleccionado es: {ListaClientes[16]} {ListaClientes[17]} {ListaClientes[18]} {ListaClientes[19]}")
                                                print("¿Seguro que quieres actualizar este cliente?\n '1' para Sí y '0' para No.")
                                            respuestaSioNo = int(input("> "))
                                            while respuestaSioNo:
                                                print(f"Para dejar de actualizar el cliente: {eleccionUsuarioActualizar}, presione '5'")
                                                if respuestaSioNo:
                                                    print("|1.-| Cédula\n|2.-| Nombre\n|3.-| Apellidos\n|4.-| Método de pago\n|5.-| Dejar actualizar")
                                                    UsuarioQuiereActualizarEl = input(f"¿Qué quiere actualizar del cliente {eleccionUsuarioActualizar}?\n> ")
                                                    if UsuarioQuiereActualizarEl == "1": # ACTUALIZAR CEDULA DEL CLIENTE
                                                        print(f"Ha seleccionado el cliente {eleccionUsuarioActualizar}, para actualizar la cédula.\n")
                                                        nuevaCedula = int(input("Ingrese la nueva cédula: "))
                                                        ListaActualizar5.clear()
                                                        NuevaCedulaEnString = str(nuevaCedula)
                                                        ListaActualizar5.append(NuevaCedulaEnString)
                                                        ListaActualizar5.append(ListaClientes[17])
                                                        ListaActualizar5.append(ListaClientes[18])
                                                        ListaActualizar5.append(ListaClientes[19])
                                                        print(f"Cédula actualizada éxitosamente...\nCliente: {ListaActualizar5[0]} {ListaActualizar5[1]} {ListaActualizar5[2]} {ListaActualizar5[3]}")
                                                        control5 = 1
                                                        ControlVueltas5 += 1
                                                        break
                                                    elif UsuarioQuiereActualizarEl == "2": # ACTUALIZAR NOMBRE DEL CLIENTE
                                                        print(f"Ha seleccionado el cliente {eleccionUsuarioActualizar}, para actualizar el nombre.\n")
                                                        nuevoNombre = input("Ingrese el nuevo nombre: ")
                                                        ListaActualizar5.clear()
                                                        ListaActualizar5.append(ListaClientes[16])
                                                        ListaActualizar5.append(nuevoNombre)
                                                        ListaActualizar5.append(ListaClientes[18])
                                                        ListaActualizar5.append(ListaClientes[19])
                                                        print(f"Nombre actualizado éxitosamente...\nCliente: {ListaActualizar5[0]} {ListaActualizar5[1]} {ListaActualizar5[2]} {ListaActualizar5[3]}")
                                                        control5 = 1
                                                        ControlVueltas5 += 1
                                                        break
                                                    elif UsuarioQuiereActualizarEl == "3": # ACTUALIZAR APELLIDO DEL CLIENTE
                                                        print(f"Ha seleccionado el cliente {eleccionUsuarioActualizar}, para actualizar el apellido.\n")
                                                        nuevoApellido = input("Ingrese el nuevo apellido: ")
                                                        ListaActualizar5.clear()
                                                        ListaActualizar5.append(ListaClientes[16])
                                                        ListaActualizar5.append(ListaClientes[17])
                                                        ListaActualizar5.append(nuevoApellido)
                                                        ListaActualizar5.append(ListaClientes[19])
                                                        print(f"Apellido actualizado éxitosamente...\nCliente: {ListaActualizar5[0]} {ListaActualizar5[1]} {ListaActualizar5[2]} {ListaActualizar5[3]}")
                                                        control5 = 1
                                                        ControlVueltas5 += 1
                                                        break
                                                    elif UsuarioQuiereActualizarEl == "4": # ACTUALIZAR MÉTODO DEL CLIENTE
                                                        print(f"Ha seleccionado el cliente {eleccionUsuarioActualizar}, para actualizar el método de pago.\n")
                                                        nuevoMetodo = input("Ingrese el nuevo método. '1' para pagar con tarjeta de crédito o débito. '2' para pagar en efectivo.\n> ")
                                                        if nuevoMetodo == "1":
                                                            nuevoMetodoActualizado = "Tarjeta de crédito o débito"
                                                        elif nuevoMetodo == "2":
                                                            nuevoMetodoActualizado = "Efectivo"                                                            
                                                        ListaActualizar5.clear()
                                                        ListaActualizar5.append(ListaClientes[16])
                                                        ListaActualizar5.append(ListaClientes[17])
                                                        ListaActualizar5.append(ListaClientes[18])
                                                        ListaActualizar5.append(nuevoMetodoActualizado)
                                                        print(f"Método de pago actualizado éxitosamente...\nCliente: {ListaActualizar5[0]} {ListaActualizar5[1]} {ListaActualizar5[2]} {ListaActualizar5[3]}")
                                                        control5 = 1
                                                        ControlVueltas5 += 1
                                                        break
                                                    elif UsuarioQuiereActualizarEl == "5":
                                                        break
                                                    
                                            else:
                                                print("Lo siento, no hay  esa cantidad de clientes registrados.\n")
                                        elif eleccionUsuarioActualizar == 6:
                                            Leer(0, control1,control2,control3,control4,control5)
                                            break
                                        
                                    break
# ================================================================= Eliminar =================================================================== #
                    else:
                        print("¿Quieres primero leer la data para saber cuál vas a eliminar? \nPresiona '1' para Sí y presiona '0' para No")
                        while True:
                            eleccionData = int(input("> "))
                            if eleccionData:
                                Leer(1,0,0,0,0,0)
                            else:
                                if len(ListaClientes) == 0:
                                    print("Lo siento, pero no hay data creada. Vuelve a intentarlo después de crearla con el Menú CRUD opción 1.\n")
                                    break
                                else:
                                    ListaEliminarAuxiliar = ListaClientes.copy()
                                    while True:
                                        while True:
                                            try:
                                                print("\nPara dejar de eliminar y guardar todas las eliminaciones, presionar: '6'")
                                                print("Haz seleeccionado eliminar.\n\n¿Qué cliente desea eliminar?")
                                                eliminarOpcion = int(input("> "))
                                                break
                                            except ValueError:
                                                print("No aceptamos data basura. Vuelva intentarlo.\n")
                                                continue
                                        # ============================== CLIENTE ELIMINAR 1 ============================== # 
                                        while True:
                                            try:
                                                if eliminarOpcion == 1:
                                                    print(f"Haz seleccionado el cliente: {ListaEliminarAuxiliar[0]} {ListaEliminarAuxiliar[1]} {ListaEliminarAuxiliar[2]} {ListaEliminarAuxiliar[3]}")
                                                    print("¿Estás seguro de que quieres eliminar este cliente?\nPresiona '1' para Sí y presiona '0' para No.")
                                                    eliminarVideoJuegoSIoNo = int(input("> "))
                                                    if eliminarVideoJuegoSIoNo:
                                                        EliminarClientes(eliminarOpcion)
                                                    else:
                                                        print("De acuerdo, el cliente no se ha eliminado. Saliendo...")
                                                    break
                                                else: break
                                            except ValueError:
                                                print("Lo siento, haz introducido algo que no es un dígito.")
                                                continue
                                            
                                        # ============================== CLIENTE ELIMINAR 2 ============================== # 
                                        while True:
                                            try:
                                                if eliminarOpcion == 2:
                                                    print(f"Haz seleccionado el cliente: {ListaEliminarAuxiliar[4]} {ListaEliminarAuxiliar[5]} {ListaEliminarAuxiliar[6]} {ListaEliminarAuxiliar[7]}")
                                                    print("¿Estás seguro de que quieres eliminar este cliente?\nPresiona '1' para Sí y presiona '0' para No.")
                                                    eliminarVideoJuegoSIoNo = int(input("> "))
                                                    if eliminarVideoJuegoSIoNo:
                                                        EliminarClientes(eliminarOpcion)
                                                    else:
                                                        print("De acuerdo, el cliente no se ha eliminado. Saliendo...")
                                                    break
                                                else: break
                                            except ValueError:
                                                print("Lo siento, haz introducido algo que no es un dígito.")
                                                continue
                                        # ============================== CLIENTE ELIMINAR 3 ============================== # 
                                        while True:
                                            try:
                                                if eliminarOpcion == 3:
                                                    print(f"Haz seleccionado el cliente: {ListaEliminarAuxiliar[8]} {ListaEliminarAuxiliar[9]} {ListaEliminarAuxiliar[10]} {ListaEliminarAuxiliar[11]}")
                                                    print("¿Estás seguro de que quieres eliminar este cliente?\nPresiona '1' para Sí y presiona '0' para No.\n")
                                                    eliminarVideoJuegoSIoNo = int(input("> "))
                                                    if eliminarVideoJuegoSIoNo:
                                                        EliminarClientes(eliminarOpcion)
                                                    else:
                                                        print("De acuerdo, el cliente no se ha eliminado. Saliendo...")
                                                    break
                                                else: break
                                            except ValueError:
                                                print("Lo siento, haz introducido algo que no es un dígito.")
                                                continue
                                        # ============================== CLIENTE ELIMINAR 4 ============================== # 
                                        while True:
                                            try:
                                                if eliminarOpcion == 4:
                                                    print(f"Haz seleccionado el cliente: {ListaClientes[12]} {ListaClientes[13]} {ListaClientes[14]} {ListaClientes[15]}")
                                                    print("¿Estás seguro de que quieres eliminar este cliente?\nPresiona '1' para Sí y presiona '0' para No.\n")
                                                    eliminarVideoJuegoSIoNo = int(input("> "))
                                                    if eliminarVideoJuegoSIoNo:
                                                        EliminarClientes(eliminarOpcion)
                                                    else:
                                                        print("De acuerdo, el cliente no se ha eliminado. Saliendo...")
                                                    break
                                                else: break
                                            except ValueError:
                                                print("Lo siento, haz introducido algo que no es un dígito.")
                                                continue
                                        # ============================== CLIENTE ELIMINAR 5 ============================== # 
                                        while True:
                                            try:
                                                if eliminarOpcion == 5:
                                                    print(f"Haz seleccionado el cliente: {ListaEliminarAuxiliar[16]} {ListaEliminarAuxiliar[17]} {ListaEliminarAuxiliar[18]} {ListaEliminarAuxiliar[19]}")
                                                    print("¿Estás seguro de que quieres eliminar este cliente?\nPresiona '1' para Sí y presiona '0' para No.\n")
                                                    eliminarVideoJuegoSIoNo = int(input("> "))
                                                    if eliminarVideoJuegoSIoNo:
                                                        EliminarClientes(eliminarOpcion)
                                                    else:
                                                        print("De acuerdo, el cliente no se ha eliminado. Saliendo...")
                                                    break
                                                else: break
                                            except ValueError:
                                                print("Lo siento, haz introducido algo que no es un dígito.")
                                                continue
                                        if eliminarOpcion == 6: # SALIR DE ELIMINAR
                                            break
                                        continue
                                    
                            if eliminarOpcion == 6: # SALIR DE ELIMINAR
                                break
                else:
                    print(f"Lo siento, el '{eleccionCRUD}' no se encuentra en el menú. \n")
                    continue
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
# --------------------------------------------------------------- Ventas MENU 1 ---------------------------------------------------------------- #
            elif x == 1 and y == 2: # CONFIGURACION MENU 1 EN VENTAS
                eleccionCRUD = int(input("¿Qué desea hacer?\n> "))
                if eleccionCRUD == 0:
                    print(f"Lo siento, el '{eleccionCRUD}' no se encuentra en el menú. \n")
                elif eleccionCRUD >= 1 and eleccionCRUD <= 4:
# ================================================================= Crear VENTAS =================================================================== #
                    if eleccionCRUD == 1:
                        contador = 0
                        while True:
                            try:
                                CantidadVentas = int(input("Cantidad de Ventas a registrar: \n> "))
                                break
                            except ValueError:
                                print("No aceptamos data basura.")
                                continue
                            
                        while True:
                            try:
                                while CantidadVentas != contador:
                                    print(f"\nVenta: {contador+1}")
                                    numero = int(input("Numero de venta: "))
                                    numeroEnString = str(numero)
                                    nombre = input("Ingrese el nombre del videojuego: ")
                                    cedulaCliente = int(input("Ingrese su cédula (ID): "))
                                    cedulaClienteEnString = str(cedulaCliente)
                                    precio = input("Ingrese el precio del videojuego: ")
                                    tipoJuego = input("Ingrese el tipo de videojuego: ")
                                    ventas = Vns.Ventas(numeroEnString, nombre, cedulaClienteEnString, precio, tipoJuego)
                                    
                                    ListaVentas.append(ventas.Numero_Venta)
                                    ListaVentas.append(ventas.Ventas_nombre_Videojuego)
                                    ListaVentas.append(ventas.Ventas_cedula_Videojuego)
                                    ListaVentas.append(ventas.Ventas_precio_Videojuego)
                                    ListaVentas.append(ventas.Ventas_tipo_Videojuego)
                                    
                                    contador += 1
                                break
                            except ValueError:
                                print("Lo siento, no aceptamos data basura.\n")
                                continue
# ================================================================= LEER Venta =================================================================== #
                    elif eleccionCRUD == 2:
                        if len(ListaVentas) == 0:
                            print("\nNo hay data creada para 'Ventas'. Vuelva a intentarlo más tarde, por favor.\n")
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
                            LeerVentas()
# ================================================================= Actualizar Venta =================================================================== #
                    elif eleccionCRUD == 3:
                        print("¿Quieres primero leer la data para saber cuál vas actualizar? \nPresiona '1' para Sí y presiona '0' para No")
                        while True:
                            eleccionData = int(input("> "))
                            if eleccionData:
                                LeerVentas()
                            else:
                                if len(ListaVentas) == 0:
                                    print("Lo siento, pero no hay data creada. Vuelve a intentarlo después de crearla con el Menú CRUD opción 1.\n")
                                    break
                                else:
                                    contador = 0
                                    control1 = 0
                                    control2 = 0
                                    control3 = 0
                                    control4 = 0
                                    control5 = 0
                                    ControlVueltas1 = 0
                                    ControlVueltas2 = 0
                                    ControlVueltas3 = 0
                                    ControlVueltas4 = 0
                                    ControlVueltas5 = 0
                                    
                                    while True:
                                        contador += 1
                                        print("\nPara dejar de actualizar y guardar todas las actualizaciones, presionar: '6'")
                                        eleccionVentaActualizar = int(input("¿Cuál quieres actualizar?\nIngresa el número: "))
#==================================================================================ACTUALIZACION Venta 1==================================================================================================================================== #
                                        if eleccionVentaActualizar == 1:
                                            if ControlVueltas1 >= 1:
                                                print("\nOJO: DEBES GUARDAR LA ACTUALIZACIÓN ANTES DE VOLVER ACTUALIZAR LA MISMA VENTA.")
                                                continue
                                            else:
                                                print(f"El cliente seleccionado es (sin actualizar): {ListaVentas[0]} {ListaVentas[1]} {ListaVentas[2]} {ListaVentas[3]} {ListaVentas[4]}")
                                                print("¿Seguro que quieres actualizar este Venta?\n '1' para Sí y '0' para No.")
                                                respuestaSioNo = int(input("> "))
                                            while respuestaSioNo:
                                                if respuestaSioNo:
                                                    print("|1.-| No. Venta\n|2.-| Nombre\n|3.-| Cedula Cliente\n|4.-| Precio\n|5.-| Tipo\n|6.-| Dejar actualizar")
                                                    UsuarioQuiereActualizarEl = input(f"¿Qué quiere actualizar del Venta {eleccionVentaActualizar}?\n> ")
                                                    if UsuarioQuiereActualizarEl == "1": # ACTUALIZAR No. Venta
                                                        
                                                        print(f"Ha seleccionado la Venta {eleccionVentaActualizar}, para actualizar el No. de Venta.\n")
                                                        nuevoNumeroVenta = int(input("Ingrese el nuevo número de venta: "))
                                                        NuevoNumeroVentaActualizado = str(nuevoNumeroVenta)
                                                        ListaActualizarVentas1.clear()
                                                        ListaActualizarVentas1.append(NuevoNumeroVentaActualizado)
                                                        ListaActualizarVentas1.append(ListaVentas[1])
                                                        ListaActualizarVentas1.append(ListaVentas[2])
                                                        ListaActualizarVentas1.append(ListaVentas[3])
                                                        ListaActualizarVentas1.append(ListaVentas[4])
                                                        print(f"Número venta actualizado éxitosamente...\Venta: {ListaActualizarVentas1[0]} {ListaActualizarVentas1[1]} {ListaActualizarVentas1[2]} {ListaActualizarVentas1[3]} {ListaActualizarVentas1[4]}")
                                                        control1 = 1
                                                        ControlVueltas1 += 1
                                                        break
                                                    elif UsuarioQuiereActualizarEl == "2": # ACTUALIZAR NOMBRE DEL Venta
                                                        print(f"Ha seleccionado la Venta {eleccionVentaActualizar}, para actualizar el nombre.\n")
                                                        nuevoNombre = input("Ingrese el nuevo nombre: ")
                                                        ListaActualizarVentas1.clear()
                                                        ListaActualizarVentas1.append(ListaVentas[0])
                                                        ListaActualizarVentas1.append(nuevoNombre)
                                                        ListaActualizarVentas1.append(ListaVentas[2])
                                                        ListaActualizarVentas1.append(ListaVentas[3])
                                                        ListaActualizarVentas1.append(ListaVentas[4])
                                                        print(f"Nombre actualizado éxitosamente...\nVenta {ListaActualizarVentas1[0]} {ListaActualizarVentas1[1]} {ListaActualizarVentas1[2]} {ListaActualizarVentas1[3]} {ListaActualizarVentas1[4]}")
                                                        control1 = 1
                                                        ControlVueltas1 += 1
                                                        break
                                                    elif UsuarioQuiereActualizarEl == "3": # ACTUALIZAR CEDULA CLIENTE DEL Venta
                                                        while True:
                                                            try:
                                                                print(f"Ha seleccionado la Venta {eleccionVentaActualizar}, para actualizar la cedula del cliente.\n")
                                                                nuevaCedulaCliente = int(input("Ingrese la nueva cedula: "))
                                                                break
                                                            except ValueError:
                                                                print("No aceptamos data basura.")
                                                                continue
                                                        ListaActualizarVentas1.clear()                                                          
                                                        ListaActualizarVentas1.append(ListaVentas[0])
                                                        ListaActualizarVentas1.append(ListaVentas[1])
                                                        ListaActualizarVentas1.append(nuevaCedulaCliente)
                                                        ListaActualizarVentas1.append(ListaVentas[3])
                                                        ListaActualizarVentas1.append(ListaVentas[4])
                                                        print(f"Cedula actualizada éxitosamente...\nVenta {ListaActualizarVentas1[0]} {ListaActualizarVentas1[1]} {ListaActualizarVentas1[2]} {ListaActualizarVentas1[3]} {ListaActualizarVentas1[4]}")
                                                        control1 = 1
                                                        ControlVueltas1 += 1
                                                        break
                                                    elif UsuarioQuiereActualizarEl == "4": # ACTUALIZAR PRECIO DEL Venta
                                                        while True:
                                                            try:
                                                                print(f"Ha seleccionado la Venta {eleccionVentaActualizar}, para actualizar el precio.\n")
                                                                nuevaCedula = int(input("Ingrese el nuevo precio\n> "))
                                                                break
                                                            except ValueError:
                                                                print("No aceptamos data basura.")
                                                                continue
                                                        
                                                        ListaActualizarVentas1.clear()                                                          
                                                        ListaActualizarVentas1.append(ListaVentas[0])
                                                        ListaActualizarVentas1.append(ListaVentas[1])
                                                        ListaActualizarVentas1.append(ListaVentas[2])
                                                        ListaActualizarVentas1.append(nuevaCedula)
                                                        ListaActualizarVentas1.append(ListaVentas[4])
                                                        print(f"Precio actualizado éxitosamente...\nVenta {ListaActualizarVentas1[0]} {ListaActualizarVentas1[1]} {ListaActualizarVentas1[2]} {ListaActualizarVentas1[3]} {ListaActualizarVentas1[4]}")
                                                        control1 = 1
                                                        ControlVueltas1 += 1
                                                        break
                                                    elif UsuarioQuiereActualizarEl == "5": # ACTUALIZAR TIPO DEL Venta
                                                        while True:
                                                            try:
                                                                print(f"Ha seleccionado la Venta {eleccionVentaActualizar}, para actualizar el tipo.\n")
                                                                nuevoTipo = input("Ingrese el nuevo tipo de Venta\n> ")
                                                                break
                                                            except ValueError:
                                                                print("No aceptamos data basura.")
                                                                continue
                                                        
                                                        
                                                        ListaActualizarVentas1.clear()                                                          
                                                        ListaActualizarVentas1.append(ListaVentas[0])
                                                        ListaActualizarVentas1.append(ListaVentas[1])
                                                        ListaActualizarVentas1.append(ListaVentas[2])
                                                        ListaActualizarVentas1.append(ListaVentas[3])
                                                        ListaActualizarVentas1.append(nuevoTipo)
                                                        print(f"Tipo actualizado éxitosamente...\nVenta: {ListaActualizarVentas1[0]} {ListaActualizarVentas1[1]} {ListaActualizarVentas1[2]} {ListaActualizarVentas1[3]} {ListaActualizarVentas1[4]}")
                                                        control1 = 1
                                                        ControlVueltas1 += 1
                                                        break
                                                    
                                                    elif UsuarioQuiereActualizarEl == "6":
                                                        break
                                                    else:
                                                        print("Lo siento, lo que ha introducido no está en las opciones.")
                                                        continue
                                                    
#==================================================================================ACTUALIZACION Venta 2==================================================================================================================================== #
                                        elif eleccionVentaActualizar == 2:
                                            if ControlVueltas2 >= 1:
                                                print("\nOJO: DEBES GUARDAR LA ACTUALIZACIÓN ANTES DE VOLVER ACTUALIZAR LA MISMA VENTA.")
                                                continue
                                            else:
                                                print(f"El Venta seleccionado es (sin actualizar): {ListaVentas[5]} {ListaVentas[6]} {ListaVentas[7]} {ListaVentas[8]} {ListaVentas[9]}")
                                                print("¿Seguro que quieres actualizar este Venta?\n '1' para Sí y '0' para No.")
                                                respuestaSioNo = int(input("> "))
                                            while respuestaSioNo:
                                                if respuestaSioNo:
                                                    print("|1.-| No. Venta\n|2.-| Nombre\n|3.-| Cedula Cliente\n|4.-| Precio\n|5.-| Tipo\n|6.-| Dejar actualizar")
                                                    UsuarioQuiereActualizarEl = input(f"¿Qué quiere actualizar del Venta {eleccionVentaActualizar}?\n> ")
                                                    if UsuarioQuiereActualizarEl == "1": # ACTUALIZAR No. Venta
                                                        
                                                        print(f"Ha seleccionado la Venta {eleccionVentaActualizar}, para actualizar el No. de Venta.\n")
                                                        nuevoNumeroVenta = int(input("Ingrese el nuevo número de venta: "))
                                                        NuevoNumeroVentaActualizado = str(nuevoNumeroVenta)
                                                        ListaActualizarVentas2.clear()
                                                        ListaActualizarVentas2.append(NuevoNumeroVentaActualizado)
                                                        ListaActualizarVentas2.append(ListaVentas[6])
                                                        ListaActualizarVentas2.append(ListaVentas[7])
                                                        ListaActualizarVentas2.append(ListaVentas[8])
                                                        ListaActualizarVentas2.append(ListaVentas[9])
                                                        print(f"Número venta actualizado éxitosamente...\Venta: {ListaActualizarVentas2[0]} {ListaActualizarVentas2[1]} {ListaActualizarVentas2[2]} {ListaActualizarVentas2[3]} {ListaActualizarVentas2[4]}")
                                                        control2 = 1
                                                        ControlVueltas2 += 1
                                                        break
                                                    elif UsuarioQuiereActualizarEl == "2": # ACTUALIZAR NOMBRE DEL Venta
                                                        print(f"Ha seleccionado la Venta {eleccionVentaActualizar}, para actualizar el nombre.\n")
                                                        nuevoNombre = input("Ingrese el nuevo nombre: ")
                                                        ListaActualizarVentas2.clear()
                                                        ListaActualizarVentas2.append(ListaVentas[5])
                                                        ListaActualizarVentas2.append(nuevoNombre)
                                                        ListaActualizarVentas2.append(ListaVentas[7])
                                                        ListaActualizarVentas2.append(ListaVentas[8])
                                                        ListaActualizarVentas2.append(ListaVentas[9])
                                                        print(f"Nombre actualizado éxitosamente...\nVenta {ListaActualizarVentas2[0]} {ListaActualizarVentas2[1]} {ListaActualizarVentas2[2]} {ListaActualizarVentas2[3]} {ListaActualizarVentas2[4]}")
                                                        control2 = 1
                                                        ControlVueltas2 += 1
                                                        break
                                                    elif UsuarioQuiereActualizarEl == "3": # ACTUALIZAR CEDULA CLIENTE
                                                        while True:
                                                            try:
                                                                print(f"Ha seleccionado la Venta {eleccionVentaActualizar}, para actualizar la cedula del cliente.\n")
                                                                nuevaCedulaCliente = int(input("Ingrese la nueva cedula: "))
                                                                break
                                                            except ValueError:
                                                                print("No aceptamos data basura.")
                                                                continue
                                                        ListaActualizarVentas2.clear()                                                          
                                                        ListaActualizarVentas2.append(ListaVentas[5])
                                                        ListaActualizarVentas2.append(ListaVentas[6])
                                                        ListaActualizarVentas2.append(nuevaCedulaCliente)
                                                        ListaActualizarVentas2.append(ListaVentas[8])
                                                        ListaActualizarVentas2.append(ListaVentas[9])
                                                        print(f"Cedula actualizada éxitosamente...\nVenta {ListaActualizarVentas2[0]} {ListaActualizarVentas2[1]} {ListaActualizarVentas2[2]} {ListaActualizarVentas2[3]} {ListaActualizarVentas2[4]}")
                                                        control2 = 1
                                                        ControlVueltas2 += 1
                                                        break
                                                    elif UsuarioQuiereActualizarEl == "4": # ACTUALIZAR PRECIO DEL Venta
                                                        while True:
                                                            try:
                                                                print(f"Ha seleccionado la Venta {eleccionVentaActualizar}, para actualizar el precio.\n")
                                                                nuevaCedula = int(input("Ingrese el nuevo precio\n> "))
                                                                break
                                                            except ValueError:
                                                                print("No aceptamos data basura.")
                                                                continue
                                                        
                                                        ListaActualizarVentas2.clear()                                                          
                                                        ListaActualizarVentas2.append(ListaVentas[5])
                                                        ListaActualizarVentas2.append(ListaVentas[6])
                                                        ListaActualizarVentas2.append(ListaVentas[7])
                                                        ListaActualizarVentas2.append(nuevaCedula)
                                                        ListaActualizarVentas2.append(ListaVentas[9])
                                                        print(f"Precio actualizado éxitosamente...\nVenta {ListaActualizarVentas2[0]} {ListaActualizarVentas2[1]} {ListaActualizarVentas2[2]} {ListaActualizarVentas2[3]} {ListaActualizarVentas2[4]}")
                                                        control2 = 1
                                                        ControlVueltas2 += 1
                                                        break
                                                    elif UsuarioQuiereActualizarEl == "5": # ACTUALIZAR TIPO DEL Venta
                                                        while True:
                                                            try:
                                                                print(f"Ha seleccionado la Venta {eleccionVentaActualizar}, para actualizar el tipo.\n")
                                                                nuevoTipo = input("Ingrese el nuevo tipo de Venta\n> ")
                                                                break
                                                            except ValueError:
                                                                print("No aceptamos data basura.")
                                                                continue
                                                        
                                                        
                                                        ListaActualizarVentas2.clear()                                                          
                                                        ListaActualizarVentas2.append(ListaVentas[5])
                                                        ListaActualizarVentas2.append(ListaVentas[6])
                                                        ListaActualizarVentas2.append(ListaVentas[7])
                                                        ListaActualizarVentas2.append(ListaVentas[8])
                                                        ListaActualizarVentas2.append(nuevoTipo)
                                                        print(f"Tipo actualizado éxitosamente...\nVenta: {ListaActualizarVentas2[0]} {ListaActualizarVentas2[1]} {ListaActualizarVentas2[2]} {ListaActualizarVentas2[3]} {ListaActualizarVentas2[4]}")
                                                        control2 = 1
                                                        ControlVueltas2 += 1
                                                        break
                                                    
                                                    elif UsuarioQuiereActualizarEl == "6":
                                                        break
                                                    else:
                                                        print("Lo siento, lo que ha introducido no está en las opciones.")
                                                        continue
#==================================================================================ACTUALIZACION Venta 3==================================================================================================================================== #
                                        elif eleccionVentaActualizar == 3:
                                            if ControlVueltas3 >= 1:
                                                print("\nOJO: DEBES GUARDAR LA ACTUALIZACIÓN ANTES DE VOLVER ACTUALIZAR LA MISMA VENTA.")
                                                continue
                                            else:
                                                print(f"El Venta seleccionado es (sin actualizar): {ListaVentas[10]} {ListaVentas[11]} {ListaVentas[12]} {ListaVentas[13]} {ListaVentas[14]}")
                                                print("¿Seguro que quieres actualizar este Venta?\n '1' para Sí y '0' para No.")
                                                respuestaSioNo = int(input("> "))
                                            while respuestaSioNo:
                                                if respuestaSioNo:
                                                    print("|1.-| No. Venta\n|2.-| Nombre\n|3.-| Cedula Cliente\n|4.-| Precio\n|5.-| Tipo\n|6.-| Dejar actualizar")
                                                    UsuarioQuiereActualizarEl = input(f"¿Qué quiere actualizar del Venta {eleccionVentaActualizar}?\n> ")
                                                    if UsuarioQuiereActualizarEl == "1": # ACTUALIZAR No. Venta
                                                        
                                                        print(f"Ha seleccionado la Venta {eleccionVentaActualizar}, para actualizar el No. de Venta.\n")
                                                        nuevoNumeroVenta = int(input("Ingrese el nuevo número de venta: "))
                                                        NuevoNumeroVentaActualizado = str(nuevoNumeroVenta)
                                                        ListaActualizarVentas3.clear()
                                                        ListaActualizarVentas3.append(NuevoNumeroVentaActualizado)
                                                        ListaActualizarVentas3.append(ListaVentas[11])
                                                        ListaActualizarVentas3.append(ListaVentas[12])
                                                        ListaActualizarVentas3.append(ListaVentas[13])
                                                        ListaActualizarVentas3.append(ListaVentas[14])
                                                        print(f"Número venta actualizado éxitosamente...\Venta: {ListaActualizarVentas3[0]} {ListaActualizarVentas3[1]} {ListaActualizarVentas3[2]} {ListaActualizarVentas3[3]} {ListaActualizarVentas3[4]}")
                                                        control3 = 1
                                                        ControlVueltas3 += 1
                                                        break
                                                    elif UsuarioQuiereActualizarEl == "2": # ACTUALIZAR NOMBRE DEL Venta
                                                        print(f"Ha seleccionado la Venta {eleccionVentaActualizar}, para actualizar el nombre.\n")
                                                        nuevoNombre = input("Ingrese el nuevo nombre: ")
                                                        ListaActualizarVentas3.clear()
                                                        ListaActualizarVentas3.append(ListaVentas[10])
                                                        ListaActualizarVentas3.append(nuevoNombre)
                                                        ListaActualizarVentas3.append(ListaVentas[12])
                                                        ListaActualizarVentas3.append(ListaVentas[13])
                                                        ListaActualizarVentas3.append(ListaVentas[14])
                                                        print(f"Nombre actualizado éxitosamente...\nVenta {ListaActualizarVentas3[0]} {ListaActualizarVentas3[1]} {ListaActualizarVentas3[2]} {ListaActualizarVentas3[3]} {ListaActualizarVentas3[4]}")
                                                        control3 = 1
                                                        ControlVueltas3 += 1
                                                        break
                                                    elif UsuarioQuiereActualizarEl == "3": # ACTUALIZAR CEDULA CLIENTE DEL Venta
                                                        while True:
                                                            try:
                                                                print(f"Ha seleccionado la Venta {eleccionVentaActualizar}, para actualizar la cedula del cliente.\n")
                                                                nuevaCedulaCliente = int(input("Ingrese la nueva cedula: "))
                                                                break
                                                            except ValueError:
                                                                print("No aceptamos data basura.")
                                                                continue
                                                        ListaActualizarVentas3.clear()                                                          
                                                        ListaActualizarVentas3.append(ListaVentas[10])
                                                        ListaActualizarVentas3.append(ListaVentas[11])
                                                        ListaActualizarVentas3.append(nuevaCedulaCliente)
                                                        ListaActualizarVentas3.append(ListaVentas[13])
                                                        ListaActualizarVentas3.append(ListaVentas[14])
                                                        print(f"Cedula actualizada éxitosamente...\nVenta {ListaActualizarVentas3[0]} {ListaActualizarVentas3[1]} {ListaActualizarVentas3[2]} {ListaActualizarVentas3[3]} {ListaActualizarVentas3[4]}")
                                                        control3 = 1
                                                        ControlVueltas3 += 1
                                                        break
                                                    elif UsuarioQuiereActualizarEl == "4": # ACTUALIZAR PRECIO DEL Venta
                                                        while True:
                                                            try:
                                                                print(f"Ha seleccionado la Venta {eleccionVentaActualizar}, para actualizar el precio.\n")
                                                                nuevaCedula = int(input("Ingrese el nuevo precio\n> "))
                                                                break
                                                            except ValueError:
                                                                print("No aceptamos data basura.")
                                                                continue
                                                        
                                                        ListaActualizarVentas3.clear()                                                          
                                                        ListaActualizarVentas3.append(ListaVentas[10])
                                                        ListaActualizarVentas3.append(ListaVentas[11])
                                                        ListaActualizarVentas3.append(ListaVentas[12])
                                                        ListaActualizarVentas3.append(nuevaCedula)
                                                        ListaActualizarVentas3.append(ListaVentas[14])
                                                        print(f"Precio actualizado éxitosamente...\nVenta {ListaActualizarVentas3[0]} {ListaActualizarVentas3[1]} {ListaActualizarVentas3[2]} {ListaActualizarVentas3[3]} {ListaActualizarVentas3[4]}")
                                                        control3 = 1
                                                        ControlVueltas3 += 1
                                                        break
                                                    elif UsuarioQuiereActualizarEl == "5": # ACTUALIZAR TIPO DEL Venta
                                                        while True:
                                                            try:
                                                                print(f"Ha seleccionado la Venta {eleccionVentaActualizar}, para actualizar el tipo.\n")
                                                                nuevoTipo = input("Ingrese el nuevo tipo de Venta\n> ")
                                                                break
                                                            except ValueError:
                                                                print("No aceptamos data basura.")
                                                                continue
                                                        
                                                        
                                                        ListaActualizarVentas3.clear()                                                          
                                                        ListaActualizarVentas3.append(ListaVentas[10])
                                                        ListaActualizarVentas3.append(ListaVentas[11])
                                                        ListaActualizarVentas3.append(ListaVentas[12])
                                                        ListaActualizarVentas3.append(ListaVentas[13])
                                                        ListaActualizarVentas3.append(nuevoTipo)
                                                        print(f"Tipo actualizado éxitosamente...\nVenta: {ListaActualizarVentas3[0]} {ListaActualizarVentas3[1]} {ListaActualizarVentas3[2]} {ListaActualizarVentas3[3]} {ListaActualizarVentas3[4]}")
                                                        control3 = 1
                                                        ControlVueltas3 += 1
                                                        break
                                                    
                                                    elif UsuarioQuiereActualizarEl == "6":
                                                        break
                                                    else:
                                                        print("Lo siento, lo que ha introducido no está en las opciones.")
                                                        continue
                                                    
#==================================================================================ACTUALIZACION Venta 4==================================================================================================================================== #
                                        elif eleccionVentaActualizar == 4:
                                            if ControlVueltas4 >= 1:
                                                print("\nOJO: DEBES GUARDAR LA ACTUALIZACIÓN ANTES DE VOLVER ACTUALIZAR LA MISMA VENTA.")
                                                continue
                                            else:
                                                print(f"El Venta seleccionado es (sin actualizar): {ListaVentas[15]} {ListaVentas[16]} {ListaVentas[17]} {ListaVentas[18]} {ListaVentas[19]}")
                                                print("¿Seguro que quieres actualizar este Venta?\n '1' para Sí y '0' para No.")
                                                respuestaSioNo = int(input("> "))
                                            while respuestaSioNo:
                                                if respuestaSioNo:
                                                    print("|1.-| No. Venta\n|2.-| Nombre\n|3.-| Cedula Cliente\n|4.-| Precio\n|5.-| Tipo\n|6.-| Dejar actualizar")
                                                    UsuarioQuiereActualizarEl = input(f"¿Qué quiere actualizar del Venta {eleccionVentaActualizar}?\n> ")
                                                    if UsuarioQuiereActualizarEl == "1": # ACTUALIZAR No. Venta
                                                        
                                                        print(f"Ha seleccionado la Venta {eleccionVentaActualizar}, para actualizar el No. de Venta.\n")
                                                        nuevoNumeroVenta = int(input("Ingrese el nuevo número de venta: "))
                                                        NuevoNumeroVentaActualizado = str(nuevoNumeroVenta)
                                                        ListaActualizarVentas4.clear()
                                                        ListaActualizarVentas4.append(NuevoNumeroVentaActualizado)
                                                        ListaActualizarVentas4.append(ListaVentas[16])
                                                        ListaActualizarVentas4.append(ListaVentas[17])
                                                        ListaActualizarVentas4.append(ListaVentas[18])
                                                        ListaActualizarVentas4.append(ListaVentas[19])
                                                        print(f"Número venta actualizado éxitosamente...\Venta: {ListaActualizarVentas4[0]} {ListaActualizarVentas4[1]} {ListaActualizarVentas4[2]} {ListaActualizarVentas4[3]} {ListaActualizarVentas4[4]}")
                                                        control4 = 1
                                                        ControlVueltas4 += 1
                                                        break
                                                    elif UsuarioQuiereActualizarEl == "2": # ACTUALIZAR NOMBRE DEL Venta
                                                        print(f"Ha seleccionado la Venta {eleccionVentaActualizar}, para actualizar el nombre.\n")
                                                        nuevoNombre = input("Ingrese el nuevo nombre: ")
                                                        ListaActualizarVentas4.clear()
                                                        ListaActualizarVentas4.append(ListaVentas[15])
                                                        ListaActualizarVentas4.append(nuevoNombre)
                                                        ListaActualizarVentas4.append(ListaVentas[17])
                                                        ListaActualizarVentas4.append(ListaVentas[18])
                                                        ListaActualizarVentas4.append(ListaVentas[19])
                                                        print(f"Nombre actualizado éxitosamente...\nVenta {ListaActualizarVentas4[0]} {ListaActualizarVentas4[1]} {ListaActualizarVentas4[2]} {ListaActualizarVentas4[3]} {ListaActualizarVentas4[4]}")
                                                        control4 = 1
                                                        ControlVueltas4 += 1
                                                        break
                                                    elif UsuarioQuiereActualizarEl == "3": # ACTUALIZAR CEDULA CLIENTE DEL Venta
                                                        while True:
                                                            try:
                                                                print(f"Ha seleccionado la Venta {eleccionVentaActualizar}, para actualizar la cedula del cliente.\n")
                                                                nuevaCedulaCliente = int(input("Ingrese la nueva cedula: "))
                                                                break
                                                            except ValueError:
                                                                print("No aceptamos data basura.")
                                                                continue
                                                        ListaActualizarVentas4.clear()                                                          
                                                        ListaActualizarVentas4.append(ListaVentas[15])
                                                        ListaActualizarVentas4.append(ListaVentas[16])
                                                        ListaActualizarVentas4.append(nuevaCedulaCliente)
                                                        ListaActualizarVentas4.append(ListaVentas[18])
                                                        ListaActualizarVentas4.append(ListaVentas[19])
                                                        print(f"Cedula actualizada éxitosamente...\nVenta {ListaActualizarVentas4[0]} {ListaActualizarVentas4[1]} {ListaActualizarVentas4[2]} {ListaActualizarVentas4[3]} {ListaActualizarVentas4[4]}")
                                                        control4 = 1
                                                        ControlVueltas4 += 1
                                                        break
                                                    elif UsuarioQuiereActualizarEl == "4": # ACTUALIZAR PRECIO DEL Venta
                                                        while True:
                                                            try:
                                                                print(f"Ha seleccionado la Venta {eleccionVentaActualizar}, para actualizar el precio.\n")
                                                                nuevaCedula = int(input("Ingrese el nuevo precio\n> "))
                                                                break
                                                            except ValueError:
                                                                print("No aceptamos data basura.")
                                                                continue
                                                        
                                                        ListaActualizarVentas4.clear()                                                          
                                                        ListaActualizarVentas4.append(ListaVentas[15])
                                                        ListaActualizarVentas4.append(ListaVentas[16])
                                                        ListaActualizarVentas4.append(ListaVentas[17])
                                                        ListaActualizarVentas4.append(nuevaCedula)
                                                        ListaActualizarVentas4.append(ListaVentas[19])
                                                        print(f"Precio actualizado éxitosamente...\nVenta {ListaActualizarVentas4[0]} {ListaActualizarVentas4[1]} {ListaActualizarVentas4[2]} {ListaActualizarVentas4[3]} {ListaActualizarVentas4[4]}")
                                                        control4 = 1
                                                        ControlVueltas4 += 1
                                                        break
                                                    elif UsuarioQuiereActualizarEl == "5": # ACTUALIZAR TIPO DEL Venta
                                                        while True:
                                                            try:
                                                                print(f"Ha seleccionado la Venta {eleccionVentaActualizar}, para actualizar el tipo.\n")
                                                                nuevoTipo = input("Ingrese el nuevo tipo de Venta\n> ")
                                                                break
                                                            except ValueError:
                                                                print("No aceptamos data basura.")
                                                                continue
                                                        
                                                        
                                                        ListaActualizarVentas4.clear()                                                          
                                                        ListaActualizarVentas4.append(ListaVentas[15])
                                                        ListaActualizarVentas4.append(ListaVentas[16])
                                                        ListaActualizarVentas4.append(ListaVentas[17])
                                                        ListaActualizarVentas4.append(ListaVentas[18])
                                                        ListaActualizarVentas4.append(nuevoTipo)
                                                        print(f"Tipo actualizado éxitosamente...\nVenta: {ListaActualizarVentas4[0]} {ListaActualizarVentas4[1]} {ListaActualizarVentas4[2]} {ListaActualizarVentas4[3]} {ListaActualizarVentas4[4]}")
                                                        control4 = 1
                                                        ControlVueltas4 += 1
                                                        break
                                                    
                                                    elif UsuarioQuiereActualizarEl == "6":
                                                        break
                                                    else:
                                                        print("Lo siento, lo que ha introducido no está en las opciones.")
                                                        continue
                                                
#==================================================================================ACTUALIZACION Venta 5==================================================================================================================================== #
                                        elif eleccionVentaActualizar == 5:
                                            if ControlVueltas5 >= 1:
                                                print("\nOJO: DEBES GUARDAR LA ACTUALIZACIÓN ANTES DE VOLVER ACTUALIZAR LA MISMA VENTA.")
                                                continue
                                            else:
                                                print(f"El Venta seleccionado es (sin actualizar): {ListaVentas[20]} {ListaVentas[21]} {ListaVentas[22]} {ListaVentas[23]} {ListaVentas[24]}")
                                                print("¿Seguro que quieres actualizar este Venta?\n '1' para Sí y '0' para No.")
                                                respuestaSioNo = int(input("> "))
                                            while respuestaSioNo:
                                                if respuestaSioNo:
                                                    print("|1.-| No. Venta\n|2.-| Nombre\n|3.-| Cedula Cliente\n|4.-| Precio\n|5.-| Tipo\n|6.-| Dejar actualizar")
                                                    UsuarioQuiereActualizarEl = input(f"¿Qué quiere actualizar del Venta {eleccionVentaActualizar}?\n> ")
                                                    if UsuarioQuiereActualizarEl == "1": # ACTUALIZAR No. Venta
                                                        
                                                        print(f"Ha seleccionado la Venta {eleccionVentaActualizar}, para actualizar el No. de Venta.\n")
                                                        nuevoNumeroVenta = int(input("Ingrese el nuevo número de venta: "))
                                                        NuevoNumeroVentaActualizado = str(nuevoNumeroVenta)
                                                        ListaActualizarVentas5.clear()
                                                        ListaActualizarVentas5.append(NuevoNumeroVentaActualizado)
                                                        ListaActualizarVentas5.append(ListaVentas[21])
                                                        ListaActualizarVentas5.append(ListaVentas[22])
                                                        ListaActualizarVentas5.append(ListaVentas[23])
                                                        ListaActualizarVentas5.append(ListaVentas[24])
                                                        print(f"Número venta actualizado éxitosamente...\Venta: {ListaActualizarVentas5[0]} {ListaActualizarVentas5[1]} {ListaActualizarVentas5[2]} {ListaActualizarVentas5[3]} {ListaActualizarVentas5[4]}")
                                                        control5 = 1
                                                        ControlVueltas5 += 1
                                                        break
                                                    elif UsuarioQuiereActualizarEl == "2": # ACTUALIZAR NOMBRE DEL Venta
                                                        print(f"Ha seleccionado la Venta {eleccionVentaActualizar}, para actualizar el nombre.\n")
                                                        nuevoNombre = input("Ingrese el nuevo nombre: ")
                                                        ListaActualizarVentas5.clear()
                                                        ListaActualizarVentas5.append(ListaVentas[20])
                                                        ListaActualizarVentas5.append(nuevoNombre)
                                                        ListaActualizarVentas5.append(ListaVentas[22])
                                                        ListaActualizarVentas5.append(ListaVentas[23])
                                                        ListaActualizarVentas5.append(ListaVentas[24])
                                                        print(f"Nombre actualizado éxitosamente...\nVenta {ListaActualizarVentas5[0]} {ListaActualizarVentas5[1]} {ListaActualizarVentas5[2]} {ListaActualizarVentas5[3]} {ListaActualizarVentas5[4]}")
                                                        control5 = 1
                                                        ControlVueltas5 += 1
                                                        break
                                                    elif UsuarioQuiereActualizarEl == "3": # ACTUALIZAR CEDULA CLIENTE DEL Venta
                                                        while True:
                                                            try:
                                                                print(f"Ha seleccionado la Venta {eleccionVentaActualizar}, para actualizar la cedula del cliente.\n")
                                                                nuevaCedulaCliente = int(input("Ingrese la nueva cedula: "))
                                                                break
                                                            except ValueError:
                                                                print("No aceptamos data basura.")
                                                                continue
                                                        ListaActualizarVentas5.clear()                                                          
                                                        ListaActualizarVentas5.append(ListaVentas[20])
                                                        ListaActualizarVentas5.append(ListaVentas[21])
                                                        ListaActualizarVentas5.append(nuevaCedulaCliente)
                                                        ListaActualizarVentas5.append(ListaVentas[23])
                                                        ListaActualizarVentas5.append(ListaVentas[24])
                                                        print(f"Cedula actualizada éxitosamente...\nVenta {ListaActualizarVentas5[0]} {ListaActualizarVentas5[1]} {ListaActualizarVentas5[2]} {ListaActualizarVentas5[3]} {ListaActualizarVentas5[4]}")
                                                        control5 = 1
                                                        ControlVueltas5 += 1
                                                        break
                                                    elif UsuarioQuiereActualizarEl == "4": # ACTUALIZAR PRECIO DEL Venta
                                                        while True:
                                                            try:
                                                                print(f"Ha seleccionado la Venta {eleccionVentaActualizar}, para actualizar el precio.\n")
                                                                nuevaCedula = int(input("Ingrese el nuevo precio\n> "))
                                                                break
                                                            except ValueError:
                                                                print("No aceptamos data basura.")
                                                                continue
                                                        
                                                        ListaActualizarVentas5.clear()                                                          
                                                        ListaActualizarVentas5.append(ListaVentas[20])
                                                        ListaActualizarVentas5.append(ListaVentas[21])
                                                        ListaActualizarVentas5.append(ListaVentas[22])
                                                        ListaActualizarVentas5.append(nuevaCedula)
                                                        ListaActualizarVentas5.append(ListaVentas[24])
                                                        print(f"Precio actualizado éxitosamente...\nVenta {ListaActualizarVentas5[0]} {ListaActualizarVentas5[1]} {ListaActualizarVentas5[2]} {ListaActualizarVentas5[3]} {ListaActualizarVentas5[4]}")
                                                        control5 = 1
                                                        ControlVueltas5 += 1
                                                        break
                                                    elif UsuarioQuiereActualizarEl == "5": # ACTUALIZAR TIPO DEL Venta
                                                        while True:
                                                            try:
                                                                print(f"Ha seleccionado la Venta {eleccionVentaActualizar}, para actualizar el tipo.\n")
                                                                nuevoTipo = input("Ingrese el nuevo tipo de Venta\n> ")
                                                                break
                                                            except ValueError:
                                                                print("No aceptamos data basura.")
                                                                continue
                                                        
                                                        
                                                        ListaActualizarVentas5.clear()                                                          
                                                        ListaActualizarVentas5.append(ListaVentas[20])
                                                        ListaActualizarVentas5.append(ListaVentas[21])
                                                        ListaActualizarVentas5.append(ListaVentas[22])
                                                        ListaActualizarVentas5.append(ListaVentas[23])
                                                        ListaActualizarVentas5.append(nuevoTipo)
                                                        print(f"Tipo actualizado éxitosamente...\nVenta: {ListaActualizarVentas5[0]} {ListaActualizarVentas5[1]} {ListaActualizarVentas5[2]} {ListaActualizarVentas5[3]} {ListaActualizarVentas5[4]}")
                                                        control5 = 1
                                                        ControlVueltas5 += 1
                                                        break
                                                    
                                                    elif UsuarioQuiereActualizarEl == "6":
                                                        break
                                                    else:
                                                        print("Lo siento, lo que ha introducido no está en las opciones.")
                                                        continue
                                        elif eleccionVentaActualizar == 6:
                                            Leer(3,control1, control2, control3, control4, control5)
                                            break 
                                    break                      
# ================================================================= Eliminar Venta =================================================================== #
                    else:
                        print("¿Quieres primero leer la data para saber cuál vas a eliminar? \nPresiona '1' para Sí y presiona '0' para No")
                        while True:
                            eleccionData = int(input("> "))
                            if eleccionData:
                                LeerVentas()
                            else:
                                if len(ListaVentas) == 0:
                                    print("Lo siento, pero no hay data creada. Vuelve a intentarlo después de crearla con el Menú CRUD opción 1.\n")
                                    break
                                else:
                                    ListaEliminarAuxiliarVentas = ListaVentas.copy()
                                    while True:
                                        while True:
                                            try:
                                                print("\nPara dejar de eliminar y guardar todas las eliminaciones, presionar: '6'")
                                                print("Haz seleeccionado eliminar.\n\n¿Qué Venta desea eliminar?")
                                                eliminarOpcion = int(input("> "))
                                                break
                                            except ValueError:
                                                print("No aceptamos data basura. Vuelva intentarlo.\n")
                                                continue
                                        # ============================== Venta ELIMINAR 1 ============================== # 
                                        while True:
                                            try:
                                                if eliminarOpcion == 1:
                                                    print(f"Haz seleccionado la Venta: {ListaEliminarAuxiliarVentas[0]} {ListaEliminarAuxiliarVentas[1]} {ListaEliminarAuxiliarVentas[2]} {ListaEliminarAuxiliarVentas[3]} {ListaEliminarAuxiliarVentas[4]}")
                                                    print("¿Estás seguro de que quieres eliminar este cliente?\nPresiona '1' para Sí y presiona '0' para No.")
                                                    eliminarClienteOpcionSIoNo = int(input("> "))
                                                    if eliminarClienteOpcionSIoNo:
                                                        EliminarVentas(eliminarOpcion)
                                                    else:
                                                        print("De acuerdo, el cliente no se ha eliminado. Saliendo...")
                                                    break
                                                else: break
                                            except ValueError:
                                                print("Lo siento, haz introducido algo que no es un dígito.")
                                                continue
                                            
                                        # ============================== Venta ELIMINAR 2 ============================== # 
                                        while True:
                                            try:
                                                if eliminarOpcion == 2:
                                                    print(f"Haz seleccionado la Venta: {ListaEliminarAuxiliarVentas[5]} {ListaEliminarAuxiliarVentas[6]} {ListaEliminarAuxiliarVentas[7]} {ListaEliminarAuxiliarVentas[8]} {ListaEliminarAuxiliarVentas[9]}")
                                                    print("¿Estás seguro de que quieres eliminar este cliente?\nPresiona '1' para Sí y presiona '0' para No.")
                                                    eliminarClienteOpcionSIoNo = int(input("> "))
                                                    if eliminarClienteOpcionSIoNo:
                                                        EliminarVentas(eliminarOpcion)
                                                    else:
                                                        print("De acuerdo, el cliente no se ha eliminado. Saliendo...")
                                                    break
                                                else: break
                                            except ValueError:
                                                print("Lo siento, haz introducido algo que no es un dígito.")
                                                continue
                                        # ============================== Venta ELIMINAR 3 ============================== # 
                                        while True:
                                            try:
                                                if eliminarOpcion == 3:
                                                    print(f"Haz seleccionado la Venta: {ListaEliminarAuxiliarVentas[10]} {ListaEliminarAuxiliarVentas[11]} {ListaEliminarAuxiliarVentas[12]} {ListaEliminarAuxiliarVentas[13]} {ListaEliminarAuxiliarVentas[14]}")
                                                    print("¿Estás seguro de que quieres eliminar este cliente?\nPresiona '1' para Sí y presiona '0' para No.\n")
                                                    eliminarClienteOpcionSIoNo = int(input("> "))
                                                    if eliminarClienteOpcionSIoNo:
                                                        EliminarVentas(eliminarOpcion)
                                                    else:
                                                        print("De acuerdo, el cliente no se ha eliminado. Saliendo...")
                                                    break
                                                else: break
                                            except ValueError:
                                                print("Lo siento, haz introducido algo que no es un dígito.")
                                                continue
                                        # ============================== Venta ELIMINAR 4 ============================== # 
                                        while True:
                                            try:
                                                if eliminarOpcion == 4:
                                                    print(f"Haz seleccionado la Venta: {ListaEliminarAuxiliarVentas[15]} {ListaEliminarAuxiliarVentas[16]} {ListaEliminarAuxiliarVentas[17]} {ListaEliminarAuxiliarVentas[18]} {ListaEliminarAuxiliarVentas[19]}")
                                                    print("¿Estás seguro de que quieres eliminar este cliente?\nPresiona '1' para Sí y presiona '0' para No.\n")
                                                    eliminarClienteOpcionSIoNo = int(input("> "))
                                                    if eliminarClienteOpcionSIoNo:
                                                        EliminarVentas(eliminarOpcion)
                                                    else:
                                                        print("De acuerdo, el cliente no se ha eliminado. Saliendo...")
                                                    break
                                                else: break
                                            except ValueError:
                                                print("Lo siento, haz introducido algo que no es un dígito.")
                                                continue
                                        # ============================== Venta ELIMINAR 5 ============================== # 
                                        while True:
                                            try:
                                                if eliminarOpcion == 5:
                                                    print(f"Haz seleccionado la Venta: {ListaEliminarAuxiliarVentas[20]} {ListaEliminarAuxiliarVentas[21]} {ListaEliminarAuxiliarVentas[22]} {ListaEliminarAuxiliarVentas[23]} {ListaEliminarAuxiliarVentas[24]}")
                                                    print("¿Estás seguro de que quieres eliminar este cliente?\nPresiona '1' para Sí y presiona '0' para No.\n")
                                                    eliminarClienteOpcionSIoNo = int(input("> "))
                                                    if eliminarClienteOpcionSIoNo:
                                                        EliminarVentas(eliminarOpcion)
                                                    else:
                                                        print("De acuerdo, el cliente no se ha eliminado. Saliendo...")
                                                    break
                                                else: break
                                            except ValueError:
                                                print("Lo siento, haz introducido algo que no es un dígito.")
                                                continue
                                        if eliminarOpcion == 6: # SALIR DE ELIMINAR
                                            break
                                        continue
                                    
                            if eliminarOpcion == 6: # SALIR DE ELIMINAR
                                break
                    elegirMenu()
                else:
                    print(f"Lo siento, el '{eleccionCRUD}' no se encuentra en el menú. \n")
                    continue
                
                
                
                
                                      
                                      
                                      
                                      
                                      
                                      
                                      
                                      
                                      
                                      
                                      
                                      
                                      
                                      
                                      
                                      
                                      
                                      
                                      
                                      
                                      
                                      
                
                
                
                
                
# --------------------------------------------------------------- VIDEOJUEGO MENU 1 ---------------------------------------------------------------- #
            elif x == 1 and y == 3: # CONFIGURACION MENU 1 EN VIDEOJUEGO
                eleccionCRUD = int(input("¿Qué desea hacer?\n> "))
                if eleccionCRUD == 0:
                    print(f"Lo siento, el '{eleccionCRUD}' no se encuentra en el menú. \n")
                elif eleccionCRUD >= 1 and eleccionCRUD <= 4:
# ================================================================= Crear VIDEOJUEGO =================================================================== #
                    if eleccionCRUD == 1:
                        contador = 0
                        while True:
                            try:
                                CantidadVideojuegos = int(input("Cantidad de Videojuegos a registrar: \n> "))
                                break
                            except ValueError:
                                print("No aceptamos data basura.")
                                continue
                            
                        while True:
                            try:
                                while CantidadVideojuegos != contador:
                                    print(f"\nVideoJuegos {contador+1}")
                                    nombre = input("Ingrese el nombre del videojuego: ")
                                    tipoJuego = input("Ingrese el tipo de videojuego: ")
                                    precio = int(input("Ingrese el precio del videojuego: "))
                                    Videojuegos = Vjs.Videojuegos(nombre, tipoJuego, precio)
                                    
                                    ListaVideoJuegos.append(Videojuegos.nombre_VideoJuegos)
                                    ListaVideoJuegos.append(Videojuegos.tipo_VideoJuegos)
                                    ListaVideoJuegos.append(Videojuegos.precio_VideoJuegos)
                                    
                                    contador += 1
                                break
                            except ValueError:
                                print("Lo siento, no aceptamos data basura.\n")
                                continue
# ================================================================= LEER VIDEOJUEGO =================================================================== #
                    elif eleccionCRUD == 2:
                        if len(ListaVideoJuegos) == 0:
                            print("\nNo hay data creada para 'VideoJuegos'. Vuelva a intentarlo más tarde, por favor.\n")
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
                            LeerVideoJuegos()
# ================================================================= Actualizar VIDEOJUEGO =================================================================== #
                    elif eleccionCRUD == 3:
                        print("¿Quieres primero leer la data para saber cuál vas actualizar? \nPresiona '1' para Sí y presiona '0' para No")
                        while True:
                            eleccionData = int(input("> "))
                            if eleccionData:
                                LeerVideoJuegos()
                            else:
                                if len(ListaVideoJuegos) == 0:
                                    print("Lo siento, pero no hay data creada. Vuelve a intentarlo después de crearla con el Menú CRUD opción 1.\n")
                                    break
                                else:
                                    contador = 0
                                    control1 = 0
                                    control2 = 0
                                    control3 = 0
                                    control4 = 0
                                    control5 = 0
                                    ControlVueltas1 = 0
                                    ControlVueltas2 = 0
                                    ControlVueltas3 = 0
                                    ControlVueltas4 = 0
                                    ControlVueltas5 = 0
                                    
                                    while True:
                                        contador += 1
                                        print("\nPara dejar de actualizar y guardar todas las actualizaciones, presionar: '6'")
                                        eleccionVideojuegoActualizar = int(input("¿Cuál quieres actualizar?\nIngresa el número: "))
#==================================================================================ACTUALIZACION VIDEOJUEGO 1==================================================================================================================================== #
                                        if eleccionVideojuegoActualizar == 1:
                                            if ControlVueltas1 >= 1:
                                                print("\nOJO: DEBES GUARDAR LA ACTUALIZACIÓN ANTES DE VOLVER ACTUALIZAR EL MISMO VIDEOJUEGO.")
                                                continue
                                            else:
                                                print(f"El videojuego seleccionado es (sin actualizar): {ListaVideoJuegos[0]} {ListaVideoJuegos[1]} {ListaVideoJuegos[2]}")
                                                print("¿Seguro que quieres actualizar este videojuego?\n '1' para Sí y '0' para No.")
                                                respuestaSioNo = int(input("> "))
                                            while respuestaSioNo:
                                                if respuestaSioNo:
                                                    print("|1.-| Nombre\n|2.-| Tipo\n|3.-| Precio\n|4.-| Dejar actualizar")
                                                    UsuarioQuiereActualizarEl = input(f"¿Qué quiere actualizar del videojuego {eleccionVideojuegoActualizar}?\n> ")
                                                    if UsuarioQuiereActualizarEl == "1": # ACTUALIZAR NOMBRE DEL VIDEOJUEGO
                                                        print(f"Ha seleccionado el videojuego {eleccionVideojuegoActualizar}, para actualizar el nombre.\n")
                                                        nuevoNombre = input("Ingrese el nuevo nombre: ")
                                                        ListaActualizarVideoJuegos1.clear()
                                                        ListaActualizarVideoJuegos1.append(nuevoNombre)
                                                        ListaActualizarVideoJuegos1.append(ListaVideoJuegos[1])
                                                        ListaActualizarVideoJuegos1.append(ListaVideoJuegos[2])
                                                        print(f"Nombre actualizado éxitosamente...\Videojuego: {ListaActualizarVideoJuegos1[0]} {ListaActualizarVideoJuegos1[1]} {ListaActualizarVideoJuegos1[2]}")
                                                        control1 = 1
                                                        ControlVueltas1 += 1
                                                        break
                                                    elif UsuarioQuiereActualizarEl == "2": # ACTUALIZAR TIPO DEL VIDEOJUEGO
                                                        print(f"Ha seleccionado el videojuego {eleccionVideojuegoActualizar}, para actualizar el nombre.\n")
                                                        nuevoTipo = input("Ingrese el nuevo tipo: ")
                                                        ListaActualizarVideoJuegos1.clear()
                                                        ListaActualizarVideoJuegos1.append(ListaVideoJuegos[0])
                                                        ListaActualizarVideoJuegos1.append(nuevoTipo)
                                                        ListaActualizarVideoJuegos1.append(ListaVideoJuegos[2])
                                                        print(f"Tipo actualizado éxitosamente...\nVideojuego {ListaActualizarVideoJuegos1[0]} {ListaActualizarVideoJuegos1[1]} {ListaActualizarVideoJuegos1[2]}")
                                                        control1 = 1
                                                        ControlVueltas1 += 1
                                                        break
                                                    elif UsuarioQuiereActualizarEl == "3": # ACTUALIZAR PRECIO DEL VIDEOJUEGO
                                                        while True:
                                                            try:
                                                                print(f"Ha seleccionado el videojuego {eleccionVideojuegoActualizar}, para actualizar el precio.\n")
                                                                nuevoPrecio = int(input("Ingrese el nuevo precio: "))
                                                                break
                                                            except ValueError:
                                                                print("No aceptamos data basura.")
                                                                continue
                                                        ListaActualizarVideoJuegos1.clear()                                                          
                                                        ListaActualizarVideoJuegos1.append(ListaVideoJuegos[0])
                                                        ListaActualizarVideoJuegos1.append(ListaVideoJuegos[1])
                                                        ListaActualizarVideoJuegos1.append(nuevoPrecio)
                                                        print(f"Precio actualizado éxitosamente...\nVideojuego {ListaActualizarVideoJuegos1[0]} {ListaActualizarVideoJuegos1[1]} {ListaActualizarVideoJuegos1[2]}")
                                                        control1 = 1
                                                        ControlVueltas1 += 1
                                                        break
                                                    elif UsuarioQuiereActualizarEl == "4": # ACTUALIZAR PRECIO DEL VIDEOJUEGO
                                                        break
                                                    else:
                                                        print("Lo siento, lo que ha introducido no está en las opciones.")
                                                        continue
                                                    
#==================================================================================ACTUALIZACION VIDEOJUEGO 2==================================================================================================================================== #
                                        elif eleccionVideojuegoActualizar == 2:
                                            if ControlVueltas2 >= 1:
                                                print("\nOJO: DEBES GUARDAR LA ACTUALIZACIÓN ANTES DE VOLVER ACTUALIZAR EL MISMO VIDEOJUEGO.")
                                                continue
                                            else:
                                                print(f"El videojuego seleccionado es (sin actualizar): {ListaActualizarVideoJuegos2[3]} {ListaActualizarVideoJuegos2[4]} {ListaActualizarVideoJuegos2[5]}")
                                                print("¿Seguro que quieres actualizar este videojuego?\n '1' para Sí y '0' para No.")
                                                respuestaSioNo = int(input("> "))
                                            while respuestaSioNo:
                                                if respuestaSioNo:
                                                    print("|1.-| Nombre\n|2.-| Tipo\n|3.-| Precio\n|4.-| Dejar actualizar")
                                                    UsuarioQuiereActualizarEl = input(f"¿Qué quiere actualizar del videojuego {eleccionVideojuegoActualizar}?\n> ")
                                                    if UsuarioQuiereActualizarEl == "1": # ACTUALIZAR NOMBRE DEL VIDEOJUEGO
                                                        print(f"Ha seleccionado el videojuego {eleccionVideojuegoActualizar}, para actualizar el nombre.\n")
                                                        nuevoNombre = input("Ingrese el nuevo nombre: ")
                                                        ListaActualizarVideoJuegos2.clear()
                                                        ListaActualizarVideoJuegos2.append(nuevoNombre)
                                                        ListaActualizarVideoJuegos2.append(ListaVideoJuegos[4])
                                                        ListaActualizarVideoJuegos2.append(ListaVideoJuegos[5])
                                                        print(f"Nombre actualizado éxitosamente...\Videojuego: {ListaActualizarVideoJuegos2[3]} {ListaActualizarVideoJuegos2[4]} {ListaActualizarVideoJuegos2[5]}")
                                                        control2 = 1
                                                        ControlVueltas2 += 1
                                                        break
                                                    elif UsuarioQuiereActualizarEl == "2": # ACTUALIZAR TIPO DEL VIDEOJUEGO
                                                        print(f"Ha seleccionado el videojuego {eleccionVideojuegoActualizar}, para actualizar el nombre.\n")
                                                        nuevoTipo = input("Ingrese el nuevo tipo: ")
                                                        ListaActualizarVideoJuegos2.clear()
                                                        ListaActualizarVideoJuegos2.append(ListaVideoJuegos[3])
                                                        ListaActualizarVideoJuegos2.append(nuevoTipo)
                                                        ListaActualizarVideoJuegos2.append(ListaVideoJuegos[5])
                                                        print(f"Tipo actualizado éxitosamente...\nVideojuego {ListaActualizarVideoJuegos2[3]} {ListaActualizarVideoJuegos2[4]} {ListaActualizarVideoJuegos2[5]}")
                                                        control2 = 1
                                                        ControlVueltas2 += 1
                                                        break
                                                    elif UsuarioQuiereActualizarEl == "3": # ACTUALIZAR PRECIO DEL VIDEOJUEGO
                                                        while True:
                                                            try:
                                                                print(f"Ha seleccionado el videojuego {eleccionVideojuegoActualizar}, para actualizar el precio.\n")
                                                                nuevoPrecio = int(input("Ingrese el nuevo precio: "))
                                                                break
                                                            except ValueError:
                                                                print("No aceptamos data basura.")
                                                                continue
                                                        ListaActualizarVideoJuegos2.clear()                                                          
                                                        ListaActualizarVideoJuegos2.append(ListaVideoJuegos[3])
                                                        ListaActualizarVideoJuegos2.append(ListaVideoJuegos[4])
                                                        ListaActualizarVideoJuegos2.append(nuevoPrecio)
                                                        print(f"Precio actualizado éxitosamente...\nVideojuego {ListaActualizarVideoJuegos2[3]} {ListaActualizarVideoJuegos2[4]} {ListaActualizarVideoJuegos2[5]}")
                                                        control2 = 1
                                                        ControlVueltas2 += 1
                                                        break
                                                    elif UsuarioQuiereActualizarEl == "4": # ACTUALIZAR PRECIO DEL VIDEOJUEGO
                                                        break
                                                    else:
                                                        print("Lo siento, lo que ha introducido no está en las opciones.")
                                                        continue
                                                    
#==================================================================================ACTUALIZACION VIDEOJUEGO 3==================================================================================================================================== #
                                        elif eleccionVideojuegoActualizar == 2:
                                            if ControlVueltas3 >= 1:
                                                print("\nOJO: DEBES GUARDAR LA ACTUALIZACIÓN ANTES DE VOLVER ACTUALIZAR EL MISMO VIDEOJUEGO.")
                                                continue
                                            else:
                                                print(f"El videojuego seleccionado es (sin actualizar): {ListaActualizarVideoJuegos3[6]} {ListaActualizarVideoJuegos3[7]} {ListaActualizarVideoJuegos3[8]}")
                                                print("¿Seguro que quieres actualizar este videojuego?\n '1' para Sí y '0' para No.")
                                                respuestaSioNo = int(input("> "))
                                            while respuestaSioNo:
                                                if respuestaSioNo:
                                                    print("|1.-| Nombre\n|2.-| Tipo\n|3.-| Precio\n|4.-| Dejar actualizar")
                                                    UsuarioQuiereActualizarEl = input(f"¿Qué quiere actualizar del videojuego {eleccionVideojuegoActualizar}?\n> ")
                                                    if UsuarioQuiereActualizarEl == "1": # ACTUALIZAR NOMBRE DEL VIDEOJUEGO
                                                        print(f"Ha seleccionado el videojuego {eleccionVideojuegoActualizar}, para actualizar el nombre.\n")
                                                        nuevoNombre = input("Ingrese el nuevo nombre: ")
                                                        ListaActualizarVideoJuegos3.clear()
                                                        ListaActualizarVideoJuegos3.append(nuevoNombre)
                                                        ListaActualizarVideoJuegos3.append(ListaVideoJuegos[7])
                                                        ListaActualizarVideoJuegos3.append(ListaVideoJuegos[8])
                                                        print(f"Nombre actualizado éxitosamente...\Videojuego: {ListaActualizarVideoJuegos3[6]} {ListaActualizarVideoJuegos3[7]} {ListaActualizarVideoJuegos3[8]}")
                                                        control3 = 1
                                                        ControlVueltas3 += 1
                                                        break
                                                    elif UsuarioQuiereActualizarEl == "2": # ACTUALIZAR TIPO DEL VIDEOJUEGO
                                                        print(f"Ha seleccionado el videojuego {eleccionVideojuegoActualizar}, para actualizar el nombre.\n")
                                                        nuevoTipo = input("Ingrese el nuevo tipo: ")
                                                        ListaActualizarVideoJuegos3.clear()
                                                        ListaActualizarVideoJuegos3.append(ListaVideoJuegos[6])
                                                        ListaActualizarVideoJuegos3.append(nuevoTipo)
                                                        ListaActualizarVideoJuegos3.append(ListaVideoJuegos[8])
                                                        print(f"Tipo actualizado éxitosamente...\nVideojuego {ListaActualizarVideoJuegos3[6]} {ListaActualizarVideoJuegos3[7]} {ListaActualizarVideoJuegos3[8]}")
                                                        control3 = 1
                                                        ControlVueltas3 += 1
                                                        break
                                                    elif UsuarioQuiereActualizarEl == "3": # ACTUALIZAR PRECIO DEL VIDEOJUEGO
                                                        while True:
                                                            try:
                                                                print(f"Ha seleccionado el videojuego {eleccionVideojuegoActualizar}, para actualizar el precio.\n")
                                                                nuevoPrecio = int(input("Ingrese el nuevo precio: "))
                                                                break
                                                            except ValueError:
                                                                print("No aceptamos data basura.")
                                                                continue
                                                        ListaActualizarVideoJuegos3.clear()                                                          
                                                        ListaActualizarVideoJuegos3.append(ListaVideoJuegos[6])
                                                        ListaActualizarVideoJuegos3.append(ListaVideoJuegos[7])
                                                        ListaActualizarVideoJuegos3.append(nuevoPrecio)
                                                        print(f"Precio actualizado éxitosamente...\nVideojuego {ListaActualizarVideoJuegos3[6]} {ListaActualizarVideoJuegos3[7]} {ListaActualizarVideoJuegos3[8]}")
                                                        control3 = 1
                                                        ControlVueltas3 += 1
                                                        break
                                                    elif UsuarioQuiereActualizarEl == "4": # ACTUALIZAR PRECIO DEL VIDEOJUEGO
                                                        break
                                                    else:
                                                        print("Lo siento, lo que ha introducido no está en las opciones.")
                                                        continue
                                                    
#==================================================================================ACTUALIZACION VIDEOJUEGO 4==================================================================================================================================== #
                                        elif eleccionVideojuegoActualizar == 4:
                                            if ControlVueltas4 >= 1:
                                                print("\nOJO: DEBES GUARDAR LA ACTUALIZACIÓN ANTES DE VOLVER ACTUALIZAR EL MISMO VIDEOJUEGO.")
                                                continue
                                            else:
                                                print(f"El videojuego seleccionado es (sin actualizar): {ListaActualizarVideoJuegos4[9]} {ListaActualizarVideoJuegos4[10]} {ListaActualizarVideoJuegos4[11]}")
                                                print("¿Seguro que quieres actualizar este videojuego?\n '1' para Sí y '0' para No.")
                                                respuestaSioNo = int(input("> "))
                                            while respuestaSioNo:
                                                if respuestaSioNo:
                                                    print("|1.-| Nombre\n|2.-| Tipo\n|3.-| Precio\n|4.-| Dejar actualizar")
                                                    UsuarioQuiereActualizarEl = input(f"¿Qué quiere actualizar del videojuego {eleccionVideojuegoActualizar}?\n> ")
                                                    if UsuarioQuiereActualizarEl == "1": # ACTUALIZAR NOMBRE DEL VIDEOJUEGO
                                                        print(f"Ha seleccionado el videojuego {eleccionVideojuegoActualizar}, para actualizar el nombre.\n")
                                                        nuevoNombre = input("Ingrese el nuevo nombre: ")
                                                        ListaActualizarVideoJuegos4.clear()
                                                        ListaActualizarVideoJuegos4.append(nuevoNombre)
                                                        ListaActualizarVideoJuegos4.append(ListaVideoJuegos[10])
                                                        ListaActualizarVideoJuegos4.append(ListaVideoJuegos[11])
                                                        print(f"Nombre actualizado éxitosamente...\Videojuego: {ListaActualizarVideoJuegos4[9]} {ListaActualizarVideoJuegos4[10]} {ListaActualizarVideoJuegos4[11]}")
                                                        control4 = 1
                                                        ControlVueltas4 += 1
                                                        break
                                                    elif UsuarioQuiereActualizarEl == "2": # ACTUALIZAR TIPO DEL VIDEOJUEGO
                                                        print(f"Ha seleccionado el videojuego {eleccionVideojuegoActualizar}, para actualizar el nombre.\n")
                                                        nuevoTipo = input("Ingrese el nuevo tipo: ")
                                                        ListaActualizarVideoJuegos4.clear()
                                                        ListaActualizarVideoJuegos4.append(ListaVideoJuegos[9])
                                                        ListaActualizarVideoJuegos4.append(nuevoTipo)
                                                        ListaActualizarVideoJuegos4.append(ListaVideoJuegos[11])
                                                        print(f"Tipo actualizado éxitosamente...\nVideojuego {ListaActualizarVideoJuegos4[9]} {ListaActualizarVideoJuegos4[10]} {ListaActualizarVideoJuegos4[11]}")
                                                        control4 = 1
                                                        ControlVueltas4 += 1
                                                        break
                                                    elif UsuarioQuiereActualizarEl == "3": # ACTUALIZAR PRECIO DEL VIDEOJUEGO
                                                        while True:
                                                            try:
                                                                print(f"Ha seleccionado el videojuego {eleccionVideojuegoActualizar}, para actualizar el precio.\n")
                                                                nuevoPrecio = int(input("Ingrese el nuevo precio: "))
                                                                break
                                                            except ValueError:
                                                                print("No aceptamos data basura.")
                                                                continue
                                                        ListaActualizarVideoJuegos4.clear()                                                          
                                                        ListaActualizarVideoJuegos4.append(ListaVideoJuegos[9])
                                                        ListaActualizarVideoJuegos4.append(ListaVideoJuegos[10])
                                                        ListaActualizarVideoJuegos4.append(nuevoPrecio)
                                                        print(f"Precio actualizado éxitosamente...\nVideojuego {ListaActualizarVideoJuegos4[9]} {ListaActualizarVideoJuegos4[10]} {ListaActualizarVideoJuegos4[11]}")
                                                        control4 = 1
                                                        ControlVueltas4 += 1
                                                        break
                                                    elif UsuarioQuiereActualizarEl == "4": # ACTUALIZAR PRECIO DEL VIDEOJUEGO
                                                        break
                                                    else:
                                                        print("Lo siento, lo que ha introducido no está en las opciones.")
                                                        continue
                                                
#==================================================================================ACTUALIZACION VIDEOJUEGO 5==================================================================================================================================== #
                                        elif eleccionVideojuegoActualizar == 5:
                                            if ControlVueltas5 >= 1:
                                                print("\nOJO: DEBES GUARDAR LA ACTUALIZACIÓN ANTES DE VOLVER ACTUALIZAR EL MISMO VIDEOJUEGO.")
                                                continue
                                            else:
                                                print(f"El videojuego seleccionado es (sin actualizar): {ListaActualizarVideoJuegos5[12]} {ListaActualizarVideoJuegos5[13]} {ListaActualizarVideoJuegos5[14]}")
                                                print("¿Seguro que quieres actualizar este videojuego?\n '1' para Sí y '0' para No.")
                                                respuestaSioNo = int(input("> "))
                                            while respuestaSioNo:
                                                if respuestaSioNo:
                                                    print("|1.-| Nombre\n|2.-| Tipo\n|3.-| Precio\n|4.-| Dejar actualizar")
                                                    UsuarioQuiereActualizarEl = input(f"¿Qué quiere actualizar del videojuego {eleccionVideojuegoActualizar}?\n> ")
                                                    if UsuarioQuiereActualizarEl == "1": # ACTUALIZAR NOMBRE DEL VIDEOJUEGO
                                                        print(f"Ha seleccionado el videojuego {eleccionVideojuegoActualizar}, para actualizar el nombre.\n")
                                                        nuevoNombre = input("Ingrese el nuevo nombre: ")
                                                        ListaActualizarVideoJuegos5.clear()
                                                        ListaActualizarVideoJuegos5.append(nuevoNombre)
                                                        ListaActualizarVideoJuegos5.append(ListaVideoJuegos[7])
                                                        ListaActualizarVideoJuegos5.append(ListaVideoJuegos[8])
                                                        print(f"Nombre actualizado éxitosamente...\Videojuego: {ListaActualizarVideoJuegos5[12]} {ListaActualizarVideoJuegos5[13]} {ListaActualizarVideoJuegos5[14]}")
                                                        control5 = 1
                                                        ControlVueltas5 += 1
                                                        break
                                                    elif UsuarioQuiereActualizarEl == "2": # ACTUALIZAR TIPO DEL VIDEOJUEGO
                                                        print(f"Ha seleccionado el videojuego {eleccionVideojuegoActualizar}, para actualizar el nombre.\n")
                                                        nuevoTipo = input("Ingrese el nuevo tipo: ")
                                                        ListaActualizarVideoJuegos5.clear()
                                                        ListaActualizarVideoJuegos5.append(ListaVideoJuegos[6])
                                                        ListaActualizarVideoJuegos5.append(nuevoTipo)
                                                        ListaActualizarVideoJuegos5.append(ListaVideoJuegos[8])
                                                        print(f"Tipo actualizado éxitosamente...\nVideojuego {ListaActualizarVideoJuegos5[12]} {ListaActualizarVideoJuegos5[13]} {ListaActualizarVideoJuegos5[14]}")
                                                        control5 = 1
                                                        ControlVueltas5 += 1
                                                        break
                                                    elif UsuarioQuiereActualizarEl == "3": # ACTUALIZAR PRECIO DEL VIDEOJUEGO
                                                        while True:
                                                            try:
                                                                print(f"Ha seleccionado el videojuego {eleccionVideojuegoActualizar}, para actualizar el precio.\n")
                                                                nuevoPrecio = int(input("Ingrese el nuevo precio: "))
                                                                break
                                                            except ValueError:
                                                                print("No aceptamos data basura.")
                                                                continue
                                                        ListaActualizarVideoJuegos5.clear()                                                          
                                                        ListaActualizarVideoJuegos5.append(ListaVideoJuegos[6])
                                                        ListaActualizarVideoJuegos5.append(ListaVideoJuegos[7])
                                                        ListaActualizarVideoJuegos5.append(nuevoPrecio)
                                                        print(f"Precio actualizado éxitosamente...\nVideojuego {ListaActualizarVideoJuegos5[12]} {ListaActualizarVideoJuegos5[13]} {ListaActualizarVideoJuegos5[14]}")
                                                        control5 = 1
                                                        ControlVueltas5 += 1
                                                        break
                                                    elif UsuarioQuiereActualizarEl == "4": # ACTUALIZAR PRECIO DEL VIDEOJUEGO
                                                        break
                                                    else:
                                                        print("Lo siento, lo que ha introducido no está en las opciones.")
                                                        continue
                                        elif eleccionVideojuegoActualizar == 6:
                                            Leer(4,control1, control2, control3, control4, control5)
                                            break 
                                    break                      
# ================================================================= Eliminar VIDEOJUEGO =================================================================== #
                    else:
                        print("¿Quieres primero leer la data para saber cuál vas a eliminar? \nPresiona '1' para Sí y presiona '0' para No")
                        while True:
                            eleccionData = int(input("> "))
                            if eleccionData:
                                LeerVideoJuegos()
                            else:
                                if len(ListaVideoJuegos) == 0:
                                    print("Lo siento, pero no hay data creada. Vuelve a intentarlo después de crearla con el Menú CRUD opción 1.\n")
                                    break
                                else:
                                    ListaEliminarAuxiliarVideoJuegos = ListaVideoJuegos.copy()
                                    while True:
                                        while True:
                                            try:
                                                print("\nPara dejar de eliminar y guardar todas las eliminaciones, presionar: '6'")
                                                print("Haz seleeccionado eliminar.\n\n¿Qué videojuego desea eliminar?")
                                                eliminarOpcion = int(input("> "))
                                                break
                                            except ValueError:
                                                print("No aceptamos data basura. Vuelva intentarlo.\n")
                                                continue
                                        # ============================== VIDEOJUEGO ELIMINAR 1 ============================== # 
                                        while True:
                                            try:
                                                if eliminarOpcion == 1:
                                                    print(f"Haz seleccionado el videojuego: {ListaEliminarAuxiliarVideoJuegos[0]} {ListaEliminarAuxiliarVideoJuegos[1]} {ListaEliminarAuxiliarVideoJuegos[2]}")
                                                    print("¿Estás seguro de que quieres eliminar este videojuego?\nPresiona '1' para Sí y presiona '0' para No.")
                                                    eliminarVideoJuegoSIoNo = int(input("> "))
                                                    if eliminarVideoJuegoSIoNo:
                                                        EliminarVentas(eliminarOpcion)
                                                    else:
                                                        print("De acuerdo, el videojuego no se ha eliminado. Saliendo...")
                                                    break
                                                else: break
                                            except ValueError:
                                                print("Lo siento, haz introducido algo que no es un dígito.")
                                                continue
                                            
                                        # ============================== VIDEOJUEGO ELIMINAR 2 ============================== # 
                                        while True:
                                            try:
                                                if eliminarOpcion == 2:
                                                    print(f"Haz seleccionado el videojuego: {ListaEliminarAuxiliarVideoJuegos[3]} {ListaEliminarAuxiliarVideoJuegos[4]} {ListaEliminarAuxiliarVideoJuegos[5]}")
                                                    print("¿Estás seguro de que quieres eliminar este videojuego?\nPresiona '1' para Sí y presiona '0' para No.")
                                                    eliminarVideoJuegoSIoNo = int(input("> "))
                                                    if eliminarVideoJuegoSIoNo:
                                                        EliminarVentas(eliminarOpcion)
                                                    else:
                                                        print("De acuerdo, el videojuego no se ha eliminado. Saliendo...")
                                                    break
                                                else: break
                                            except ValueError:
                                                print("Lo siento, haz introducido algo que no es un dígito.")
                                                continue
                                        # ============================== VIDEOJUEGO ELIMINAR 3 ============================== # 
                                        while True:
                                            try:
                                                if eliminarOpcion == 3:
                                                    print(f"Haz seleccionado el videojuego: {ListaEliminarAuxiliarVideoJuegos[6]} {ListaEliminarAuxiliarVideoJuegos[7]} {ListaEliminarAuxiliarVideoJuegos[8]}")
                                                    print("¿Estás seguro de que quieres eliminar este videojuego?\nPresiona '1' para Sí y presiona '0' para No.\n")
                                                    eliminarVideoJuegoSIoNo = int(input("> "))
                                                    if eliminarVideoJuegoSIoNo:
                                                        EliminarVentas(eliminarOpcion)
                                                    else:
                                                        print("De acuerdo, el videojuego no se ha eliminado. Saliendo...")
                                                    break
                                                else: break
                                            except ValueError:
                                                print("Lo siento, haz introducido algo que no es un dígito.")
                                                continue
                                        # ============================== VIDEOJUEGO ELIMINAR 4 ============================== # 
                                        while True:
                                            try:
                                                if eliminarOpcion == 4:
                                                    print(f"Haz seleccionado el videojuego: {ListaEliminarAuxiliarVideoJuegos[9]} {ListaEliminarAuxiliarVideoJuegos[10]} {ListaEliminarAuxiliarVideoJuegos[11]}")
                                                    print("¿Estás seguro de que quieres eliminar este videojuego?\nPresiona '1' para Sí y presiona '0' para No.\n")
                                                    eliminarVideoJuegoSIoNo = int(input("> "))
                                                    if eliminarVideoJuegoSIoNo:
                                                        EliminarVentas(eliminarOpcion)
                                                    else:
                                                        print("De acuerdo, el videojuego no se ha eliminado. Saliendo...")
                                                    break
                                                else: break
                                            except ValueError:
                                                print("Lo siento, haz introducido algo que no es un dígito.")
                                                continue
                                        # ============================== VIDEOJUEGO ELIMINAR 5 ============================== # 
                                        while True:
                                            try:
                                                if eliminarOpcion == 5:
                                                    print(f"Haz seleccionado el videojuego: {ListaEliminarAuxiliarVideoJuegos[12]} {ListaEliminarAuxiliarVideoJuegos[13]} {ListaEliminarAuxiliarVideoJuegos[14]}")
                                                    print("¿Estás seguro de que quieres eliminar este videojuego?\nPresiona '1' para Sí y presiona '0' para No.\n")
                                                    eliminarVideoJuegoSIoNo = int(input("> "))
                                                    if eliminarVideoJuegoSIoNo:
                                                        EliminarVentas(eliminarOpcion)
                                                    else:
                                                        print("De acuerdo, el videojuego no se ha eliminado. Saliendo...")
                                                    break
                                                else: break
                                            except ValueError:
                                                print("Lo siento, haz introducido algo que no es un dígito.")
                                                continue
                                        if eliminarOpcion == 6: # SALIR DE ELIMINAR
                                            break
                                        continue
                                    
                            if eliminarOpcion == 6: # SALIR DE ELIMINAR
                                break
                    elegirMenu()
                else:
                    print(f"Lo siento, el '{eleccionCRUD}' no se encuentra en el menú. \n")
                    continue
                    
# --------------------------------------------------------------- CLIENTES MENU 2 ---------------------------------------------------------------- #
            elif x == 2 and y == 1: # CONFIGURACION MENU 2 EN CLIENTES
                eleccionAdicional = int(input("¿Qué desea hacer?\n> "))
                if eleccionAdicional == 0:
                    print(f"Lo siento, el '{eleccionAdicional}' no se encuentra en el menú. \n")   
                elif eleccionAdicional >= 1 and eleccionAdicional <= 2:
# ================================================================= CARGA-EXPORTACION CSV =================================================================== #
                    if eleccionAdicional == 1:
                        while True:
                            try:
                                if len(ListaClientes) == 0:
                                    print("\nLo siento, no existe ninguna data para clientes, por favor crearla en el menú 1 CRUD, opción 1.\n")
                                else:
                                    print("¿Deseas cargar en un archivo csv la data de clientes para luego exportarla?\nPresiona '1' para Sí y presiona '0' para No.")
                                    elecionSIoNo = int(input("> "))
                                break
                            except ValueError:
                                print("No aceptamos data basura. No ingresaste un dígito, vuelve a intentarlo.\n")
                                continue
                        if elecionSIoNo:
                            archivoCargaExportacion = open("Carga_Exportacion_Clientes.csv", "a")
                            if len(ListaVentas) == 5:
                                archivoCargaExportacion.write("Cedula,Nombre,Apellido,Metodo de pago\n"+ListaClientes[0]+","+ListaClientes[1]+","+ListaClientes[2]+","+ListaClientes[3])
                            if len(ListaClientes) == 10:
                                archivoCargaExportacion.write("Cedula,Nombre,Apellido,Metodo de pago\n"+ListaClientes[0]+","+ListaClientes[1]+","+ListaClientes[2]+","+ListaClientes[3]+"\n"+ListaClientes[4]+","+ListaClientes[5]+","+ListaClientes[6]+","+ListaClientes[7])
                            elif len(ListaClientes) == 15:
                                archivoCargaExportacion.write("Cedula,Nombre,Apellido,Metodo de pago\n"+ListaClientes[0]+","+ListaClientes[1]+","+ListaClientes[2]+","+ListaClientes[3]+"\n"+ListaClientes[4]+","+ListaClientes[5]+","+ListaClientes[6]+","+ListaClientes[7]+"\n"+ListaClientes[8]+","+ListaClientes[9]+","+ListaClientes[10]+","+ListaClientes[11])
                            elif len(ListaClientes) == 20:
                                archivoCargaExportacion.write("Cedula,Nombre,Apellido,Metodo de pago\n"+ListaClientes[0]+","+ListaClientes[1]+","+ListaClientes[2]+","+ListaClientes[3]+"\n"+ListaClientes[4]+","+ListaClientes[5]+","+ListaClientes[6]+","+ListaClientes[7]+"\n"+ListaClientes[8]+","+ListaClientes[9]+","+ListaClientes[10]+","+ListaClientes[11]+"\n"+ListaClientes[12]+","+ListaClientes[13]+","+ListaClientes[14]+","+ListaClientes[15])
                            elif len(ListaClientes) == 25:
                                archivoCargaExportacion.write("Cedula,Nombre,Apellido,Metodo de pago\n"+ListaClientes[0]+","+ListaClientes[1]+","+ListaClientes[2]+","+ListaClientes[3]+"\n"+ListaClientes[4]+","+ListaClientes[5]+","+ListaClientes[6]+","+ListaClientes[7]+"\n"+ListaClientes[8]+","+ListaClientes[9]+","+ListaClientes[10]+","+ListaClientes[11]+"\n"+ListaClientes[12]+","+ListaClientes[13]+","+ListaClientes[14]+","+ListaClientes[15]+"\n"+ListaClientes[16]+","+ListaClientes[17]+","+ListaClientes[18]+","+ListaClientes[19])
                            
                        else:
                            archivoCargaExportacion.close()
                            print("\nCerrando... No se creó el archivo de Carga_Exportacion_Clientes.csv\n")
                            break
# ================================================================= CSV VENTAS MAYOR A RD$500.00 =================================================================== #
                    else:
                        pass
                    break
                else:
                    print(f"Lo siento, el '{eleccionAdicional}' no se encuentra en el menú. \n")
                    continue
                
# --------------------------------------------------------------- Ventas MENU 2 ---------------------------------------------------------------- #
            elif x == 2 and y == 2: # CONFIGURACION MENU 2 EN Ventas
                eleccionAdicional = int(input("¿Qué desea hacer?\n> "))
                if eleccionAdicional == 0:
                    print(f"Lo siento, el '{eleccionAdicional}' no se encuentra en el menú. \n")   
                elif eleccionAdicional >= 1 and eleccionAdicional <= 2:
# ================================================================= CARGA-EXPORTACION CSV =================================================================== #
                    if eleccionAdicional == 1:
                        while True:
                            try:
                                if len(ListaVentas) == 0:
                                    print("\nLo siento, no existe ninguna data para ventas, por favor crearla en el menú 1 CRUD, opción 1.\n")
                                else:
                                    print("¿Deseas cargar en un archivo csv la data de Ventas para luego exportarla?\nPresiona '1' para Sí y presiona '0' para No.")
                                    elecionSIoNo = int(input("> "))
                                break
                            except ValueError:
                                print("No aceptamos data basura. No ingresaste un dígito, vuelve a intentarlo.\n")
                                continue
                        if elecionSIoNo:
                            archivoCargaExportacion = open("Carga_Exportacion_Ventas.csv", "a")
                            if len(ListaVentas) == 5:
                                archivoCargaExportacion.write("No. Venta,Nombre,Cedula,Precio,Tipo\n"+ListaVentas[0]+","+ListaVentas[1]+","+ListaVentas[2]+","+ListaVentas[3]+","+ListaVentas[4])
                            if len(ListaVentas) == 10:
                                archivoCargaExportacion.write("No. Venta,Nombre,Cedula,Precio,Tipo\n"+ListaVentas[0]+","+ListaVentas[1]+","+ListaVentas[2]+","+ListaVentas[3]+","+ListaVentas[4]+"\n"+ListaVentas[5]+","+ListaVentas[6]+","+ListaVentas[7]+","+ListaVentas[8]+","+ListaVentas[9])
                            elif len(ListaVentas) == 15:
                                archivoCargaExportacion.write("No. Venta,Nombre,Cedula,Precio,Tipo\n"+ListaVentas[0]+","+ListaVentas[1]+","+ListaVentas[2]+","+ListaVentas[3]+","+ListaVentas[4]+"\n"+ListaVentas[5]+","+ListaVentas[6]+","+ListaVentas[7]+","+ListaVentas[8]+","+ListaVentas[9]+"\n"+ListaVentas[10]+","+ListaVentas[11]+","+ListaVentas[12]+","+ListaVentas[13]+","+ListaVentas[14])
                            elif len(ListaVentas) == 20:
                                archivoCargaExportacion.write("No. Venta,Nombre,Cedula,Precio,Tipo\n"+ListaVentas[0]+","+ListaVentas[1]+","+ListaVentas[2]+","+ListaVentas[3]+","+ListaVentas[4]+"\n"+ListaVentas[5]+","+ListaVentas[6]+","+ListaVentas[7]+","+ListaVentas[8]+","+ListaVentas[9]+"\n"+ListaVentas[10]+","+ListaVentas[11]+","+ListaVentas[12]+","+ListaVentas[13]+","+ListaVentas[14]+"\n"+ListaVentas[15]+","+ListaVentas[16]+","+ListaVentas[17]+","+ListaVentas[18]+","+ListaVentas[19])
                            elif len(ListaVentas) == 25:
                                archivoCargaExportacion.write("No. Venta,Nombre,Cedula,Precio,Tipo\n"+ListaVentas[0]+","+ListaVentas[1]+","+ListaVentas[2]+","+ListaVentas[3]+","+ListaVentas[4]+"\n"+ListaVentas[5]+","+ListaVentas[6]+","+ListaVentas[7]+","+ListaVentas[8]+","+ListaVentas[9]+"\n"+ListaVentas[10]+","+ListaVentas[11]+","+ListaVentas[12]+","+ListaVentas[13]+","+ListaVentas[14]+"\n"+ListaVentas[15]+","+ListaVentas[16]+","+ListaVentas[17]+","+ListaVentas[18]+","+ListaVentas[19]+"\n"+ListaVentas[20]+","+ListaVentas[21]+","+ListaVentas[22]+","+ListaVentas[23]+","+ListaVentas[24])
                                
                        else:
                            print("\nCerrando... No se creó el archivo de Carga_Exportacion_Ventas.csv\n")
                            break
# ================================================================= CSV VENTAS MAYOR A RD$500.00 =================================================================== #
                    else:
                        pass
                    break
                else:
                    print(f"Lo siento, el '{eleccionAdicional}' no se encuentra en el menú. \n")
                    continue
                
# --------------------------------------------------------------- VIDEOJUEGOS MENU 2 ---------------------------------------------------------------- #
            elif x == 2 and y == 3: # CONFIGURACION MENU 2 EN VIDEOJUEGOS
                eleccionAdicional = int(input("¿Qué desea hacer?\n> "))
                if eleccionAdicional == 0:
                    print(f"Lo siento, el '{eleccionAdicional}' no se encuentra en el menú. \n")   
                elif eleccionAdicional >= 1 and eleccionAdicional <= 2:
# ================================================================= CARGA-EXPORTACION CSV =================================================================== #
                    if eleccionAdicional == 1:
                        while True:
                            try:
                                if len(ListaVideoJuegos) == 0:
                                    print("\nLo siento, no existe ninguna data para ventas, por favor crearla en el menú 1 CRUD, opción 1.\n")
                                else:
                                    print("¿Deseas cargar en un archivo csv la data de VideoJuegos para luego exportarla?\nPresiona '1' para Sí y presiona '0' para No.")
                                    elecionSIoNo = int(input("> "))
                                break
                            except ValueError:
                                print("No aceptamos data basura. No ingresaste un dígito, vuelve a intentarlo.\n")
                                continue
                        if elecionSIoNo:
                            archivoCargaExportacion = open("Carga_Exportacion_Videojuegos.csv", "a")
                            if len(ListaVentas) == 3:
                                archivoCargaExportacion.write("Nombre,Tipo,Precio\n"+ListaVideoJuegos[0]+","+ListaVideoJuegos[1]+","+ListaVideoJuegos[2])
                            if len(ListaVideoJuegos) == 6:
                                archivoCargaExportacion.write("Nombre,Tipo,Precio\n"+ListaVideoJuegos[0]+","+ListaVideoJuegos[1]+","+ListaVideoJuegos[2]+"\n"+ListaVideoJuegos[3]+","+ListaVideoJuegos[4]+","+ListaVideoJuegos[5])
                            elif len(ListaVideoJuegos) == 9:
                                archivoCargaExportacion.write("Nombre,Tipo,Precio\n"+ListaVideoJuegos[0]+","+ListaVideoJuegos[1]+","+ListaVideoJuegos[2]+"\n"+ListaVideoJuegos[3]+","+ListaVideoJuegos[4]+","+ListaVideoJuegos[5]+"\n"+ListaVideoJuegos[6]+","+ListaVideoJuegos[7]+","+ListaVideoJuegos[8])
                            elif len(ListaVideoJuegos) == 12:
                                archivoCargaExportacion.write("Nombre,Tipo,Precio\n"+ListaVideoJuegos[0]+","+ListaVideoJuegos[1]+","+ListaVideoJuegos[2]+"\n"+ListaVideoJuegos[3]+","+ListaVideoJuegos[4]+","+ListaVideoJuegos[5]+"\n"+ListaVideoJuegos[6]+","+ListaVideoJuegos[7]+","+ListaVideoJuegos[8]+"\n"+ListaVideoJuegos[9]+","+ListaVideoJuegos[10]+","+ListaVideoJuegos[11])
                            elif len(ListaVideoJuegos) == 15:
                                archivoCargaExportacion.write("Nombre,Tipo,Precio\n"+ListaVideoJuegos[0]+","+ListaVideoJuegos[1]+","+ListaVideoJuegos[2]+"\n"+ListaVideoJuegos[3]+","+ListaVideoJuegos[4]+","+ListaVideoJuegos[5]+"\n"+ListaVideoJuegos[6]+","+ListaVideoJuegos[7]+","+ListaVideoJuegos[8]+"\n"+ListaVideoJuegos[9]+","+ListaVideoJuegos[10]+","+ListaVideoJuegos[11]+"\n"+ListaVideoJuegos[12]+","+ListaVideoJuegos[13]+","+ListaVideoJuegos[14])
                            
                        else:
                            archivoCargaExportacion.close()
                            print("\nCerrando... No se creó el archivo de Carga_Exportacion_VideoJuegos.csv\n")
                            break
# ================================================================= CSV VENTAS MAYOR A RD$500.00 =================================================================== #
                    else:
                        pass
                    break
                else:
                    print(f"Lo siento, el '{eleccionAdicional}' no se encuentra en el menú. \n")
                    continue
            elegirMenu()
        
            
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
                print("Haz seleccionado 'Ventas'...")
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

#TODO HACER EL SEGUNDO MENU DE LOS 3 MODELOS.