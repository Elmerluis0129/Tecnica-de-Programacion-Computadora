#!/usr/bin/env python
#_*_ coding: utf8 _*_

import requests #Libreía de python que sirve para trabajar con peticiones HTTP
import argparse #Librería de python que sirve para analizar sintácticamente las opciones, argumentos y sub-comandos de la línea de comandos


parser = argparse.ArgumentParser(description = "Detector de cabeceras") #Aquí añadimos argumentparser a argparse, con una descripción
parser.add_argument('-t', '--target', help = "Debes especificar el objetivo, ejemplo: -t (url página web)") #Aquí añadimos argumentos a nuestro parser
parser = parser.parse_args() #Aquí le decimos al programa que terminamos de poner argumentos a nuestra variable parser


def main():
	if parser.target:
		try:
			url = requests.get(url = parser.target) #Aquí le pedimos al programa que se conecte a la url que el usuario le brinde
			cabeceras = dict(url.headers)#Aquí convertimos la información solicitada a un diccionario
			for x in cabeceras: #Aquí recoremos el diccionario que hemos creado anteriormente
				print(x + " : " + cabeceras[x])#Aquí le damos un orden para su legibilidad
		except:
			print("No me pude conectar")
	else:
		print("No hay objetivo, consulta la ayuda con --help para más información.")
		

if __name__ == '__main__':
	main()