"""
Formato de fechas. Solicitar una fecha por teclado (día, mes y año), y retornarla en el siguiente formato de ejemplo: Sábado 29 de octubre del 2022.
Elmer Saint-Hilare 21-1354
""" 
def fecha():
    # ==== Importaciones ==== #
    """
    Aquí importo date de datetime como dt. Ya que más adelante lo estaré necesitando.
    """
    from datetime import date as dt
    # == Fin Importaciones == #
    
    # ===== Variables generales ===== #
    """
    Aquí es donde almaceno en las variables lo que es el día, mes y año según lo introducido por el usuario.
    """
    d = int(input("\nDía: \n> "))
    m = int(input("Mes: \n> "))
    a = int(input("Año: \n> "))
    # === Fin Variables generales === #
    
    # ========================================== Control de días y meses ========================================== #
    """
    Aquí es donde controlo que días tienen n meses y qué meses tienen n días, para así evitar un error si el usuario coloca un mes con más días de los establecidos.
    """
    
    while True:
    
    # ---------------------------- Meses con 28 días ---------------------------- #
        if m == 2 and d > 28:
            print("\nLo siento, febrero solo tiene 28 días a menos que sea un año viciesto.\nVuelve a intentarlo.")
            d = int(input("\nDía: \n> "))
            continue
    # -------------------------- Fin Meses con 28 días -------------------------- #
    
    # ---------------------------- Meses con 30 días ---------------------------- #
        elif m == 4 and d > 30:
            print("\nLo siento, abril solo tiene 30 días.\nVuelve a intentarlo.")
            d = int(input("\nDía: \n> "))
            continue
        elif m == 6 and d > 30:
            print("\nLo siento, junio solo tiene 30 días.\nVuelve a intentarlo.")
            d = int(input("\nDía: \n> "))
            continue
        elif m == 9 and d > 30:
            print("\nLo siento, Septiembre solo tiene 30 días.\nVuelve a intentarlo.")
            d = int(input("\nDía: \n> "))
            continue
        elif m == 11 and d > 30:
            print("\nLo siento, noviembre solo tiene 30 días.\nVuelve a intentarlo.")
            d = int(input("\nDía: \n> "))
            continue 
    # -------------------------- Fin Meses con 30 días -------------------------- #
        
    # ---------------------------- Meses con 31 días ---------------------------- #
        elif m == 1 and d > 31:
            print("\nLo siento, enero solo tiene 31 días.\nVuelve a intentarlo.")
            d = int(input("\nDía: \n> "))
            continue
        elif m == 3 and d > 31:
            print("\nLo siento, marzo solo tiene 31 días.\nVuelve a intentarlo.")
            d = int(input("\nDía: \n> "))
            continue
        elif m == 5 and d > 31:
            print("\nLo siento, mayo solo tiene 31 días.\nVuelve a intentarlo.")
            d = int(input("\nDía: \n> "))
            continue
        elif m == 7 and d > 31:
            print("\nLo siento, julio solo tiene 31 días.\nVuelve a intentarlo.")
            d = int(input("\nDía: \n> "))
            continue
        elif m == 8 and d > 31:
            print("\nLo siento, agosto solo tiene 31 días.\nVuelve a intentarlo.")
            d = int(input("\nDía: \n> "))
            continue
        elif m == 10 and d > 31:
            print("\nLo siento, octubre solo tiene 31 días.\nVuelve a intentarlo.")
            d = int(input("\nDía: \n> "))
            continue
        elif m == 12 and d > 31:
            print("\nLo siento, diciembre solo tiene 31 días.\nVuelve a intentarlo.")
            d = int(input("\nDía: \n> "))
            continue    
        else: 
            Fechactual = dt(a, m, d) # Aquí le doy el formato de fecha y lo guardo en la variable.
            break
    # -------------------------- Fin Meses con 31 días -------------------------- #
    # ======================================== Fin Control de días y meses ======================================== #
          
    
    
    
    
    # ================= Funciones ================= #
    """
    Aquí tengo mis funciones donde especifico cual es el día de la semana y cuál es el mes según el número que me mande la función.
    """
    # -------------- Función 1 -------------- #
    """
    Aquí es dónde especifico los días de la semana.
    """
    def diaDeLaSemana(): 
        diactual = dt(a, m, d).weekday()
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
    # ------------ Fin Función 1 ------------ #  
    
    # -------------- Función 2 -------------- # 
    """
    Aquí es donde especifico los meses del año.
    """   
    def mesDelAño(): 
        mesAño = dt(a, m, d).month
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
    # ------------ Fin Función 2 ------------ #  
    # =============== Fin Funciones =============== #
    
    # =============== Llamada Funciones =============== #
    """
    Aquí le hago el llamado a mis funciones.
    """
    diaDeLaSemana()
    mesDelAño()
    # ============= Fin Llamada Funciones ============= #
    
    # ===== Impresión por pantalla ===== #
    """
    Aquí ya imprimo mi resultado.
    """
    print("Su fecha actual es:\n"+
    "*---------------------------------*"
    ,"\n|",diasemana,Fechactual.day, "de", mes, "del", Fechactual.year,
    "|\n*---------------------------------*")
    # === Fin Impresión por pantalla === #
    
    print("\n¡Programa 2 finalizado con éxito!")