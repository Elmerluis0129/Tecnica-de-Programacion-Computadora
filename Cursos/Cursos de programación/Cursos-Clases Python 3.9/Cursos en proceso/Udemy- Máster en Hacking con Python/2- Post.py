#!/usr/bin/env python
#_*_ coding: utf8 _*_

import requests #Libreía de python que sirve para trabajar con peticiones HTTP
import argparse #Librería de python que sirve para analizar sintácticamente las opciones, argumentos y sub-comandos de la línea de comandos
from os import path #Librería de python (os), importamos path, que sirve para verificar la existencia de archivos

parser = argparse.ArgumentParser() #Aquí convertimos la variable parser en un objeto de esa clase
parser.add_argument('-f', '--file', help = "Indica el archivo a subir") #Aquí añadimos argumentos a nuestro parser
parser = parser.parse_args() #Aquí le damos a entender al programa que ya hemos terminado de agregale argumentos a nuestra variable (parser)


def main():
	if parser.file:
		if path.exists(parser.file): #Aquí le pedimos al programa que verifique si hay un archivo
			archivo = open(parser.file, 'rb') #Abrír el archivo en caso de que exista uno, de forma binaria (rb)
			headers = {'User-Agent':'Chrome'}
			peticion = requests.post(url = "https://justbeamit.com/", files = {'uploaded_file':archivo})
			if parser.file in peticion.text:
				print(peticion.text)
				print("Archivo subido con éxito")
			else:
				print("\nFalló la subida del archivo")
		else:
			print("No existe el archivo")
	else:
		print("Necesito un archivo para subir")

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt: #Controlamos las salidas con try y except
		print("Saliendo...")
		exit()