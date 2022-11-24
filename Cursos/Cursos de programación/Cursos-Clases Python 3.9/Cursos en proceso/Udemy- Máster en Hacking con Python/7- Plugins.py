#!/usr/bin/env python
#_*_ coding: utf8 _*_

import requests
from os import path # Librería de python (os), importamos path, que sirve para verificar la existencia de archivos
from progress.bar import Bar # 


def main():
	if path.exists("wp_plugins.txt"):
		w = open("wp_plugins.txt", "r")
		w = w.read().split('\n')
		lista = []
		url = "https://Hostinger.com"
		b = Bar("Espere...", max = len(w))

		for plugin in w:
			b.next()
			try:
				p = requests.get(url = url + "/" +plugin)
				if p.status_code == 200:
					final = url + "/" + plugin
					lista.append(final.split("/")[-2])
			except:
				pass
		b.finish()
		for plugin in lista:
			print(f"Plugin encontrado: {plugin}")

	else:
		print("No se encuentra la lista")

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print("Saliendo...")
		exit()