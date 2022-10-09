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
ListaValor = []
ListaCantidadProducto = []
ListaITBS = ["Manzana", "Pera", "Huevos"]
ListaCalcularITBS = []
cantidadProductosComprados = int(input("Ingrese la cantidad de productos comprados: "))
x = 0


#Aqui lo uso para pedir los datos
while cantidadProductosComprados != x:
    if nombreUsuario == 0:
        nombreUsuario = str(input("Nombre Usuario: ")) #Aqui pide el nombre
        continue
    
    nombreProducto = input("Nombre Producto: ") #Aqui pido el nombre del producto
    
    if cantidadProductosComprados != x: 
        cantidadProducto = str(input("Cantidad Producto: ")) # Aqui pide la cantidad del producto
        ListaCantidadProducto.append(cantidadProducto) # Aqui agrega el cantidad del producto
        precioProducto = int(input("Precio Producto: ")) # Aqui pide el precio del producto
        ListaValor.append(precioProducto) # Aqui agrega el precio del producto.
    if nombreProducto in ListaITBS:
        calcularITBS = (precioProducto / 1.18) * 0.18
        ListaCalcularITBS.append(calcularITBS)
    else:
        calcularITBS = 0.00
        
        
    x = x + 1 # Aqui mi contador.
    ListaCompra.append(nombreProducto)# Aqui para agregar el producto a la lista
    # Aqui para saber cuales llevan itbis
    
precioCompraProducto = int(cantidadProducto) * int(precioProducto)
# CalcularPrecioTodo = precioCompraProducto + CalcularITBI



    
    
print("""
*------------------------------*
|FACTURA DE CONSUMO ELECTRONICA| 
*------------------------------*\n\n"""
"Usuario:", nombreUsuario)

        #Encabezado de la factura
print("""
*------------------------------------------------------------------------*
|      Descripcion       | Cantidad Producto |   ITBIS   |       VALOR   | 
*------------------------------------------------------------------------*
""")
a = 0
for e in ListaCompra:
    n = ListaCantidadProducto[a]
    i = ListaCalcularITBS[a]
    v = ListaValor[a]
    if len(ListaCompra[a]) >= 5 and len(ListaCantidadProducto[a]) <= 7:
        print("\t",e, "\t\t", n, "\t\t", round(i, 2), "\t\t", v)
    elif len(ListaCompra[a]) >= 2 and len(ListaCantidadProducto[a]) <= 4:
        print("\t",e, "\t\t\t", n, "\t\t", round(i, 2), "\t\t", float(v))
    a = a + 1
    
#TODO TRATAR DE RESOLVER LO DEL ITBIS PARA QUE AGREGUE AL QUE NO TIENE COMO 0.00
    

#Agradecimiento por usar el programa.
print("""
*----------------------------------------------------------------------------*
| ¡Muchas gracias por utilizar mi programa! / By: Elmer Saint-Hilare 21-1354 |
*----------------------------------------------------------------------------*
""")#Decorando el agradecimiento.
#FIN