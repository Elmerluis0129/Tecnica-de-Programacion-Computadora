#!/usr/bin/env python
#_*_ coding: utf8 _*_

import requests #Sirve para enviar solicitudes HTTP, y poder extraer información de los sitios web y más.
from bs4 import BeautifulSoup #Sirve para embellecer las respuestas de nuestro programa.

def main():
	sitioWeb = "https://www.plesk.com/" #Sitio web al cual quiero conectarme.
	cabeza = {'User-Agent':'Chrome'} #Cabecera para conectarme al sitio web.
	peticion = requests.get(url=sitioWeb,headers = cabeza) #Aquí nos conectamos a la url y obtenemos como respuesta el codigo fuente de la url.
	sp = BeautifulSoup(peticion.text, 'html5lib') #Con esto embellecemos el código de tal manera que se vea bonito a la hora de ejecutarlo por consola. html5lib, es la líbreria que usamos para emebellecer con BeautifulSoup.
	for v in sp.find_all('meta'): #Sirve para encontrar todas las etiquetas 'meta', que es donde se almacena con lo que se hizo el sitio web, en este caso wordpress.
		if v.get('name') == 'generator': #Sirve para crear el contenido, y traer todo lo que  se encuentre en name y saber si eso que se encuentra ahí, es igual a generator o no.
			ver = v.get('content')
			print(ver)
		else:
			print("Lo siento, name no es igual a generator")
	

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print("Saliendo...")
		exit()