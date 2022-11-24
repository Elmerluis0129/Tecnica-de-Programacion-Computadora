#!/usr/bin/env python
#_*_ coding: utf8 _*_

import os #Libreía de Python que nos permite interactuar directamente y utilizar funciones dependientes del sistema operativo

print("\nRuta actual: \n" ,os.getcwd()) #Sirve para mostrar en pantalla tu ruta actual
os.chdir("C:/Users/elmer/Desktop/Elmer") #Sirve para cambiar de tu ruta actual a otra ruta que introduzcas (cd)

print("\nEjecutando cambio de ruta... \nSu ruta ha cambiado con éxito \n\nRuta actual: \n" ,os.getcwd(), "\n\nEnlistando el contenido de la ruta: ")
print(os.listdir(os.getcwd())) #Sirve para en listar todo lo que contenga dicha ruta (dir)

os.mkdir("pruebacurso") # Sirve para crear carpetas / directorios (mkdir)
print("\nCarpeta creada (pruebacurso3): \n" ,os.listdir(os.getcwd()))

os.rmdir("pruebacurso") # Sirve para eliminar carpetas / directorios (rmdir)
print("\nCarpeta eliminada (pruebacurso3): \n" ,os.listdir(os.getcwd()))

#os.rename("Sistemas Ope", "Sistemas Operativos") # Sirve para renombrar un archivo o carpeta
#print("\nCarpeta renombrada (Sistemas O / Sistemas Operativos): \n" ,os.listdir(os.getcwd()))

os.system("ping www.google.com") # Sirve para ejecutar comandos directa e indirectamente

