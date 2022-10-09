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
ListaCosto = []
ListaCantidadProducto = []
ListaITBS = ["manzana", "pera", "huevos", "pan", "salami", "chinola", "mandarina", "aguacate", "refresco", "leche", "mantequilla"]
ListaCalcularITBS = []
cantidadProductosComprados = int(input("Ingrese la cantidad de productos comprados: "))
x = 0


#Aqui lo uso para pedir los datos
while cantidadProductosComprados != x:
    if nombreUsuario == 0:
        nombreUsuario = str(input("Nombre Usuario: ")) #Aqui pide el nombre
        continue
    
    nombreProducto = input("Nombre Producto: ") #Aqui pido el nombre del producto
    nombreProducto = nombreProducto.lower()
    if cantidadProductosComprados != x: 
        cantidadProducto = str(input("Cantidad Producto: ")) # Aqui pide la cantidad del producto
        ListaCantidadProducto.append(cantidadProducto) # Aqui agrega el cantidad del producto
        precioProducto = int(input("Precio Producto: ")) # Aqui pide el precio del producto
        ListaValor.append(precioProducto) # Aqui agrega el precio del producto.
    if nombreProducto in ListaITBS:
        calcularITBS = (precioProducto / 1.18) * 0.18
        ListaCalcularITBS.append(calcularITBS)
    else:
        ListaCalcularITBS.append(0.00)
        calcularITBS = 0.00
        
    precioCompraProducto = int(cantidadProducto) * int(precioProducto)
    ListaCosto.append(precioCompraProducto)
    ListaCompra.append(nombreProducto)# Aqui para agregar el producto a la lista
    x = x + 1 # Aqui mi contador.
    

CalcularPrecioTodo = precioCompraProducto + calcularITBS
it = ListaCalcularITBS[0]
precioTotal = precioCompraProducto + CalcularPrecioTodo
  
  
print("""
*------------------------------*
|FACTURA DE CONSUMO ELECTRONICA| 
*------------------------------*\n\n"""
"Usuario:", nombreUsuario)

        #Encabezado de la factura
print("""
*-----------------------------------------------------------------------------------------*
|      Descripcion       | Cantidad Producto |   ITBIS   |      Valor    |      Costo     |
*-----------------------------------------------------------------------------------------*
""")
a = 0
for e in ListaCompra:
    n = ListaCantidadProducto[a]
    i = ListaCalcularITBS[a]
    v = ListaValor[a]
    if len(ListaCalcularITBS) == 2:
        it = ListaCalcularITBS[0] + ListaCalcularITBS[1]
        vl = ListaValor[0] + ListaValor[1]
        cs = ListaCosto[0] + ListaCosto[1]
    elif len(ListaCalcularITBS) == 3:
        it = ListaCalcularITBS[0] + ListaCalcularITBS[1] + ListaCalcularITBS[2]
        vl = ListaValor[0] + ListaValor[1] + ListaValor[2]
        cs = ListaCosto[0] + ListaCosto[1] + ListaCosto[2]
    elif len(ListaCalcularITBS) == 4:
        it = ListaCalcularITBS[0] + ListaCalcularITBS[1] + ListaCalcularITBS[2] + ListaCalcularITBS[3]
        vl = ListaValor[0] + ListaValor[1] + ListaValor[2] + ListaValor[3]
        cs = ListaCosto[0] + ListaCosto[1] + ListaCosto[2] + ListaCosto[3]
    elif len(ListaCalcularITBS) == 5:
        it = ListaCalcularITBS[0] + ListaCalcularITBS[1] + ListaCalcularITBS[2] + ListaCalcularITBS[3] + ListaCalcularITBS[4]
        vl = ListaValor[0] + ListaValor[1] + ListaValor[2] + ListaValor[3] + ListaValor[4]
        cs = ListaCosto[0] + ListaCosto[1] + ListaCosto[2] + ListaCosto[3] + ListaCosto[4]
    elif len(ListaCalcularITBS) == 6:
        it = ListaCalcularITBS[0] + ListaCalcularITBS[1] + ListaCalcularITBS[2] + ListaCalcularITBS[3] + ListaCalcularITBS[4] + ListaCalcularITBS[5]
        vl = ListaValor[0] + ListaValor[1] + ListaValor[2] + ListaValor[3] + ListaValor[4] + ListaValor[5]
        cs = ListaCosto[0] + ListaCosto[1] + ListaCosto[2] + ListaCosto[3] + ListaCosto[4] + ListaCosto[5]
    elif len(ListaCalcularITBS) == 7:
        it = ListaCalcularITBS[0] + ListaCalcularITBS[1] + ListaCalcularITBS[2] + ListaCalcularITBS[3] + ListaCalcularITBS[4] + ListaCalcularITBS[5] + ListaCalcularITBS[6]
        vl = ListaValor[0] + ListaValor[1] + ListaValor[2] + ListaValor[3] + ListaValor[4] + ListaValor[5] + ListaValor[6]
        cs = ListaCosto[0] + ListaCosto[1] + ListaCosto[2] + ListaCosto[3] + ListaCosto[4] + ListaCosto[5] + ListaCosto[6]
    elif len(ListaCalcularITBS) == 8:
        it = ListaCalcularITBS[0] + ListaCalcularITBS[1] + ListaCalcularITBS[2] + ListaCalcularITBS[3] + ListaCalcularITBS[4] + ListaCalcularITBS[5] + ListaCalcularITBS[6] + ListaCalcularITBS[7]
        vl = ListaValor[0] + ListaValor[1] + ListaValor[2] + ListaValor[3] + ListaValor[4] + ListaValor[5] + ListaValor[6] + ListaValor[7]
        cs = ListaCosto[0] + ListaCosto[1] + ListaCosto[2] + ListaCosto[3] + ListaCosto[4] + ListaCosto[5] + ListaCosto[6] + ListaCosto[7]
    elif len(ListaCalcularITBS) == 9:
        it = ListaCalcularITBS[0] + ListaCalcularITBS[1] + ListaCalcularITBS[2] + ListaCalcularITBS[3] + ListaCalcularITBS[4] + ListaCalcularITBS[5] + ListaCalcularITBS[6] + ListaCalcularITBS[7] + ListaCalcularITBS[8]
        vl = ListaValor[0] + ListaValor[1] + ListaValor[2] + ListaValor[3] + ListaValor[4] + ListaValor[5] + ListaValor[6] + ListaValor[7] + ListaValor[8]
        cs = ListaCosto[0] + ListaCosto[1] + ListaCosto[2] + ListaCosto[3] + ListaCosto[4] + ListaCosto[5] + ListaCosto[6] + ListaCosto[7] + ListaCosto[8]
    elif len(ListaCalcularITBS) == 10:
        it = ListaCalcularITBS[0] + ListaCalcularITBS[1] + ListaCalcularITBS[2] + ListaCalcularITBS[3] + ListaCalcularITBS[4] + ListaCalcularITBS[5] + ListaCalcularITBS[6] + ListaCalcularITBS[7] + ListaCalcularITBS[8] + ListaCalcularITBS[9]
        vl = ListaValor[0] + ListaValor[1] + ListaValor[2] + ListaValor[3] + ListaValor[4] + ListaValor[5] + ListaValor[6] + ListaValor[7] + ListaValor[8] + ListaValor[9]
        cs = ListaCosto[0] + ListaCosto[1] + ListaCosto[2] + ListaCosto[3] + ListaCosto[4] + ListaCosto[5] + ListaCosto[6] + ListaCosto[7]  + ListaCosto[8] + ListaCosto[9]
    else:
        it = ListaCalcularITBS[a]
        vl = ListaValor[a]
        cs = ListaCosto[a]
        
    if len(ListaCompra[a]) >= 7 and len(ListaCantidadProducto[a]) <= 10:
        print("\t",e, "\t\t", n, "\t\t", round(i, 2), "\t\t", float(v), "\t\t", float(cs))
    elif len(ListaCompra[a]) >= 5 and len(ListaCantidadProducto[a]) <= 6:
        print("\t",e, "\t\t\t", n, "\t\t", round(i, 2), "\t\t", float(v), "\t\t", float(cs))
    elif len(ListaCompra[a]) >= 2 and len(ListaCantidadProducto[a]) <= 4:
        print("\t",e, "\t\t\t", n, "\t\t", round(i, 2), "\t\t", float(v), "\t\t", float(cs))
        
    a = a + 1

print("*-----------------------------------------------------------------------------------------*")
print("""\tSubtotal:\t\t\t\t""", round(it, 2), "\t\t", float(vl))
print("""\tTotal:""", round(CalcularPrecioTodo, 2))

#TODO ARREGLAR LO COSTO Y QUE TOTAL SEA LA SUMA DE COSTO.
    
#Agradecimiento por usar el programa.
print("""
*----------------------------------------------------------------------------*
| ¡Muchas gracias por utilizar mi programa! / By: Elmer Saint-Hilare 21-1354 |
*----------------------------------------------------------------------------*
""", )#Decorando el agradecimiento.
#FIN