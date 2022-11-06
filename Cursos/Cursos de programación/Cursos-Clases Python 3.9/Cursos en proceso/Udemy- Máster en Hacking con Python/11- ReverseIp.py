#!/usr/bin/env python
#_*_ coding: utf8 _*_

import requests
from bs4 import BeautifulSoup


def main():
	agent = {'User-Agent':'Chrome'}
	a = requests.get("https://viewdns.info/reverseip/?host=www.cloudflare.com&t=1", headers = agent)
	b = BeautifulSoup(a.text, 'html5lib')
	c = b.find(id = "null")
	d = c.find(border ="1")
	for x in d.find_all("tr"):
		print(x)

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print("Saliendo")	
		exit()
		
#No funciona