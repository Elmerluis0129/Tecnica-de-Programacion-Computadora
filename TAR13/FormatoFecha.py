from datetime import *



d = int(input("Día: \n> "))
m = int(input("Mes: \n> "))
a = int(input("Año: \n> "))

fechactual = datetime.datetime.strftime("%d-%m-%Y")
print(fechactual)



