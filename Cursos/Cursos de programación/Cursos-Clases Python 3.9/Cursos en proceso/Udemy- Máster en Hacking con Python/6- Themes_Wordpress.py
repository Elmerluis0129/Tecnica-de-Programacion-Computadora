#!/usr/bin/env python
#_*_ coding: utf8 _*_

import requests
from bs4 import BeautifulSoup #Sirve para embellecer las respuestas de nuestro programa.


def main():
	agent = {'User-Agent':'Chrome'}
	peticion = requests.get(url = 'https://es.wikipedia.org/wiki/Wikipedia:Portada', headers = agent)
	soup = BeautifulSoup(peticion.text, 'html5lib')
	for enlace in soup.find_all('link'):
		if "/manifest?pwa=webhp" in enlace.get('href'):
			the = enlace.get('href')
			the = the.split('/') #Aquí parceamos la url para que nos muestre únicamente el tema y los divida con un '/'.
			if 'pwa=webhp' in the:
				pos = the.index('pwa=webhp') #Aquí index sirve para buscar un elemento en especifico, en este caso dentro de the.
				theme = the[pos]
				print(theme)
		else:
			print("No pude entrar")



if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print("Saliendo...")
		exit()
