#!/usr/bin/env python
#_*_ coding: utf8 _*_

import socket

s = socket.socket() #Aqui convertimos a s en un objeto, y estamos accediendo a la clase socket del modulo socket
try:
	s.connect(("dlptest.com", 21))
	banner = s.recv(1024) # Aqui igualamos el resultado que venga de reset a la variable de banner, con una longitud de 1024 bytes en el bufet
	print(banner)
except:
	print("Ocurrió un error en la conexión")	