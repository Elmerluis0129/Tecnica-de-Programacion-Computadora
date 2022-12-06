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
Se deben controlar las excepciones (data basura) haciendo uso de try-except.

Elmer Saint-Hilare 21-1354
"""
def MenuPrincipal():
    print(
"""
   Menú CRUD
---------------
1. Listar
2. Crear
3. Leer
4. Actualizar
5. Eliminar
""")

MenuPrincipal()



    