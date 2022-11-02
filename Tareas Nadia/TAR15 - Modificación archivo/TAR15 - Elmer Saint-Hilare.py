"""
Escribir un programa que lea los archivos .csv adjuntos, y modifique el archivo "cedulas_clientes.csv" de modo que se tengan los datos de cada cliente de acuerdo a su ID. Al mismo tiempo, la fecha de nacimiento debe tener el formato dd/mm/yyyyy (día/mes/año).

Elmer Saint-Hilare 21-1354
"""


file = open("clientes.csv", 'r')
linea = file.read().splitlines()

file2 = open("cedulas_clientes.csv", 'r')
linea2 = file2.read().splitlines()


for i in range(1, len(linea)):
    usuarios = linea[i].split(',')
    dato = linea2[i].split(',')
    file2 = open("cedulas_clientes.csv", 'a')
    file2.write("\n"+dato[0]+','+usuarios[0]+','+usuarios[1]+' '+usuarios[2]+','+usuarios[3])
    

    file.close()
    file2.close()
    
#TODO INVESTIGAR LA LIBRERIA QUE SIRVE PARA ARCHIVOS, NO ES PANDA