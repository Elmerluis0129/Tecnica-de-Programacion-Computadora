#!/usr/bin/env python
#_*_ coding: utf8 _*_

import os #Libreía de Python que nos permite interactuar directamente y utilizar funciones dependientes del sistema operativo
import subprocess #Sirve para interactuar con procesos dentro del sistema operativo. 

a = open(os.devnull, 'w') # Papelera sin fondo, aqui se abre en modo escritura
p = subprocess.call(['ping','1.1.1.1'], stdout = a, stderr =subprocess.STDOUT) #Con call, hacemos que subprocess llame al sistema y ejecute lo que este adentro. Con stdout, es la salida que muestra cuando el comando se ejecuta correctamente. Con stderr, es la salida que da cuando da error la linea de comando.
if p == 0:
	print("\nEl comando se ejecutó correctamente")
else:
	print("\nFalló la ejecución del comando")