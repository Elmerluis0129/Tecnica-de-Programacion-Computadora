import socket as skt

nombre = skt.gethostname()
ip = skt.gethostbyname(nombre)

print(f"El nombre de tu ordenador es: {nombre}\nTu dirección ip pública es: {ip}")