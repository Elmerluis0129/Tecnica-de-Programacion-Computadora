# Realice un programa que replique la impresión de una factura.
# Indicaciones:
# Omitir las categorías de productos.
# Capturar nombre del cliente y mostrarlo al inicio de la factura.
# A diferencia de como se muestra en la imagen, INCLUIR una columna para la CANTIDAD del producto.
# Hay productos que no llevan ITBIS, por lo que el programa debe de controlar esto, de modo que en la columna de ITBIS se tenga 0.00 si el producto no lleva, o el valor correspondiente si lleva.
# Fórmula para el cálculo del ITBIS: (precio / 1.18) * 0.18.
# Los valores deben presentarse con 2 posiciones decimales (tal como en la imagen).
# Se debe evitar capturar data basura.
# Elmer Saint-Hilare 21-1354.

print("""
*---------------------*
|Impresión de factura:| 
*---------------------*
\n
""")


nombreUsuario = 0
ListaCompra = []
ListaITBS = ["Manzana", "Pera", "Hueos"]
cantidadProductosComprados = int(input("Ingrese la cantidad de productos comprados: "))
x = 0


#Aqui lo uso para pedir los datos
while cantidadProductosComprados != x:
    if nombreUsuario == 0:
        nombreUsuario = str(input("Nombre Usuario: ")) #Aqui pide el nombre
        continue
    
    nombreProducto = input("Nombre Producto: ") #Aqui pido el nombre del producto
    
    if cantidadProductosComprados != x: 
        cantidadProducto = str(input("Cantidad Producto: ")) #Aqui pide la cantidad del producto
        precioProducto = int(input("Precio Producto: ")) #Aqui pide el precio del producto
    x = x + 1 #Aqui mi contador
    ListaCompra.append(nombreProducto) #Aqui para agregar el producto a la lista
    #Aqui para saber cuales llevan itbis
    if nombreProducto == ListaITBS[0] or nombreProducto == ListaITBS[1] or nombreProducto == ListaITBS[2]:
        precioTotal = float(cantidadProducto) * float(precioProducto)
        CalcularITBI = ((float(precioTotal) / 1.18) * 0.18) 
        for e in ListaCompra:
            print("""
*------------------------------*
|FACTURA DE CONSUMO ELECTRONICA| 
*------------------------------*""")

            #Encabezado de la factura
            print("""
*------------------------------------------------------------------------*
|      Descripcion       | Cantidad Producto |   ITBIS   |       VALOR   | 
*------------------------------------------------------------------------*
"""
"Usuario:", nombreUsuario)
            if len(e) > 4:
                print(e, "\t\t\t", float(cantidadProducto), "\t\t",round(CalcularITBI, 2), "\t\t",round(precioProducto, 2))
            else:
                print(e, "\t\t\t\t", float(cantidadProducto), "\t\t",round(CalcularITBI, 2), "\t\t",round(precioProducto, 2))
    else:
        CalcularITBI = 0.00
        print("""
*------------------------------*
|FACTURA DE CONSUMO ELECTRONICA| 
*------------------------------*""")

        #Encabezado de la factura
        print("""
*------------------------------------------------------------------------*
|      Descripcion       | Cantidad Producto |   ITBIS   |       VALOR   | 
*------------------------------------------------------------------------*
"""
"Usuario:", nombreUsuario)
        #Aqui lo uso para que me imprima la factura.
        for e in ListaCompra:
            if len(e) > 4:
                print(e, "\t\t\t", float(cantidadProducto), "\t\t",round(CalcularITBI, 2), "\t\t",round(precioProducto, 2))
            else:
                print(e, "\t\t\t\t", float(cantidadProducto), "\t\t",round(CalcularITBI, 2), "\t\t",round(precioProducto, 2))
    
    

precioTotal = int(cantidadProducto) * int(precioProducto)

#Nombre de la factura


        
CalcularPrecioTodo = precioTotal + CalcularITBI
print("Precio Total: ", round(CalcularPrecioTodo, 2))

#Agradecimiento por usar el programa.
print("""
*----------------------------------------------------------------------------*
| ¡Muchas gracias por utilizar mi programa! / By: Elmer Saint-Hilare 21-1354 |
*----------------------------------------------------------------------------*
""")#Decorando el agradecimiento.
#FIN