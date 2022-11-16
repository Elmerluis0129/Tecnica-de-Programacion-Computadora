"""
Escribir un programa que lea los archivos .csv adjuntos, y modifique el archivo "cedulas_clientes.csv" de modo que se tengan los datos de cada cliente de acuerdo a su ID. Al mismo tiempo, la fecha de nacimiento debe tener el formato dd/mm/yyyyy (día/mes/año).

Elmer Saint-Hilare 21-1354
"""

# ==== Lista general ==== #
lista1 = []
# == Fin Lista general == #

# ==== Lectura de archivos ==== #
"""
Aquí abro el archivo, luego lo leo y por ultimo lo cierro.

Lo mismo hago con el segundo archivo file2
"""
file = open("clientes.csv", 'r')
linea = file.read().splitlines()
file.close()

file2 = open("cedulas_clientes.csv", 'r')
linea2 = file2.read().splitlines()
file2.close()
# == Fin Lectura de archivos == #

# ======== Editando cedulas_clientes ======== #
"""
Aquí abro el archivo cedulas_clientes y lo edito escribiendo los headers.
y de último lo cierro.
"""
file2 = open("cedulas_clientes.csv", 'a')
encabezado = linea[0].split(',')
encabezado2 = linea2[0].split(',')
file2.write(encabezado2[0]+','+encabezado[0]+','"Cliente"+','+encabezado[3])
file2.close()
# ====== Fin Editando cedulas_clientes ====== #


# ============ Funciones ============ #
# ------------ Función 1 ------------ #
"""
Aquí una vez leido el archivo cliente, agrego cada cliente a una lista ya creada anteriormente, aqui me agrega, nombre, apellido y fecha del cada cliente por separado todo.

las condicionales son para ir controlando que cliente me agrega por cada iteracion. con ayuda de mi contadores y acumulador.
"""
def PasarDataALista():
    x = 0
    
    for i in range(1, len(linea)):
        usuario = linea[i].split(',')
        if x == 0:
            lista1.append(usuario[1])
            lista1.append(usuario[2])
            lista1.append(usuario[3])
            x = 1
            
        elif x == 1:
            lista1.append(usuario[1])
            lista1.append(usuario[2])
            lista1.append(usuario[3])
            x = 2
            
        elif x == 2:
            lista1.append(usuario[1])
            lista1.append(usuario[2])
            lista1.append(usuario[3])
            x = 3
        elif x == 3:
            lista1.append(usuario[1])
            lista1.append(usuario[2])
            lista1.append(usuario[3])
            x = 4
        elif x == 4:
            lista1.append(usuario[1])
            lista1.append(usuario[2])
            lista1.append(usuario[3])
            x = 12  
# ---------- Fin Función 1 ---------- #

# ------------  Función 2 ------------ #
"""
Aquí divido todo, para tener acceso al dia, año y mes de cada fecha de cada cliente.

En el bucle for es donde abro el archivo cedulas_clientes como escritura sin borrar, leo el segundo archivo, segun el numero de iteración, lo separo por comma.
y luego con las condicionales verifico que usuario voy agregar, si es el 04, o el 05 o cualquiera de ellos.

Agrego los usuarios llegando a ellos segun su posicion en que quedaron en la lista creada anteriormente, al igual que su informaciones.
"""
def PasarData ():
    
    fecha1 = linea[1].split("/")
    fecha2 = linea[2].split("/")
    fecha3 = linea[3].split("/")
    fecha4 = linea[4].split("/")
    fecha5 = linea[5].split("/")
    
    mes1 = fecha1[0].split(",")
    mes2 = fecha2[0].split(",")
    mes3 = fecha3[0].split(",")
    mes4 = fecha4[0].split(",")
    mes5 = fecha5[0].split(",")
        
        
    for i in range(1, len(linea)):
        file2 = open("cedulas_clientes.csv", 'a')
        dato = linea2[i].split(',')   
        if dato[1] == '1004':
            file2.write("\n"+dato[0]+','+dato[1]+','+lista1[9]+' '+lista1[10]+','+'{}'.format(fecha4[1]+"/"+mes4[3]+"/"+fecha4[2]))
        elif dato[1] == '1001':             
            file2.write("\n"+dato[0]+','+dato[1]+','+lista1[0]+' '+lista1[1]+','+'{}'.format(fecha1[1]+"/"+mes1[3]+"/"+fecha1[2]))
        elif dato[1] == '1003':             
            file2.write("\n"+dato[0]+','+dato[1]+','+lista1[6]+' '+lista1[7]+','+'{}'.format(fecha3[1]+"/"+mes3[3]+"/"+fecha3[2]))
        elif dato[1] == '1002':             
            file2.write("\n"+dato[0]+','+dato[1]+','+lista1[3]+' '+lista1[4]+','+'{}'.format(fecha2[1]+"/"+mes2[3]+"/"+fecha2[2]))
        else:          
            file2.write("\n"+dato[0]+','+dato[1]+','+lista1[12]+' '+lista1[13]+','+'{}'.format(fecha5[1]+"/"+mes5[3]+"/"+fecha5[2]))
# ---------- Fin Función 2 ---------- #
# ========== Fin Funciones ========== #

# ========== Llamando Funciones ========== #
PasarDataALista()
PasarData()
# ======== Fin Llamando Funciones ======== #