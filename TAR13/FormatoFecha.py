# Elmer Saint-Hilare 21-1354

from datetime import date

d = int(input("\nDía: \n> "))
m = int(input("Mes: \n> "))
a = int(input("Año: \n> "))

Fechactual = date(a, m, d)

def diaDeLaSemana(): 
    diactual = date(a, m, d).weekday()
    global diasemana
    diasemana = None
    if diactual == 0:
        diasemana = "Lunes,"
    elif diactual == 1:
        diasemana = "Martes,"
    elif diactual == 2:
        diasemana = "Miercoles,"
    elif diactual == 3:
        diasemana = "Jueves,"
    elif diactual == 4:
        diasemana = "Viernes,"
    elif diactual == 5:
        diasemana = "Sábado,"
    else:
        diasemana = "Domingo,"
        
def mesDelAño(): 
    mesAño = date(a, m, d).month
    global mes
    mes = None
    if mesAño == 1:
        mes = "Enero"
    elif mesAño == 2:
        mes = "Febrero"
    elif mesAño == 3:
        mes = "Marzo"
    elif mesAño == 4:
        mes = "Abril"
    elif mesAño == 5:
        mes = "Mayo"
    elif mesAño == 6:
        mes = "Junio"
    elif mesAño == 7:
        mes = "Julio"
    elif mesAño == 8:
        mes = "Agosto"
    elif mesAño == 9:
        mes = "Septiembre"
    elif mesAño == 10:
        mes = "Octubre"
    elif mesAño ==11:
        mes = "Noviembre"
    elif mesAño == 12:
        mes = "Diciembre"
        
diaDeLaSemana()
mesDelAño()
print("Su fecha actual es:\n"+
"*---------------------------------*"
,"\n|",diasemana,Fechactual.day, "de", mes, "del", Fechactual.year,
"|\n*---------------------------------*")