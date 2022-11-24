#!/usr/bin/env python
#_*_ coding: utf8 _*_

import requests

def main():
	word = "cloudflare"
	url = requests.get("https://www.udemy.com") #Aquí hacemos una petición al servidor o página web
	cabeceras = dict(url.headers) #Aquí convertimos en diccionario las respuesta de la petición
	for c in cabeceras:
		if cabeceras[c].lower():
			print("\n¡¡CloudFlare está protegiendo esta página web!!")
			break
		else:
			print("\n¡¡CloudFlare no está protegiendo esta página web!!")


if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print("Saliendo")
		exit()