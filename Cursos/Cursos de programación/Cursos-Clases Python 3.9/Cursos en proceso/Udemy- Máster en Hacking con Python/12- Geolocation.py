#!/usr/bin/env python
#_*_ coding: utf8 _*_

import urllib.request
import json

def main():
	url = "https://ipinfo.io/172.217.9.4/json"
	v = urllib.request.urlopen(url)
	j = json.loads(v.read())

	for dato in j:
		print(dato + ": " + j[dato])

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print("Saliendo...")
		exit()