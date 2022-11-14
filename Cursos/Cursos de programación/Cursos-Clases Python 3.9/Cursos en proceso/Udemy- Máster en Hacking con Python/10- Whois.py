#!/usr/bin/env python
#_*_ coding: utf8 _*_

import requests
from bs4 import BeautifulSoup

def main():
	a = requests.get("https://who.is/whois/reldsec.org")
	sp = BeautifulSoup(a.text, 'html5lib')
	for x in sp.find_all("pre"):
		print(x.get_text()) #get_text() Esta adentro de la funciones de beautifulsoup, con el estamos accediendo a todo el contenido que tenga ese elemento recorrido en la etiqueta.


if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print("Saliendo")
		exit()