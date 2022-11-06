import sys, socket

objetivo = socket.gethostbyname(input("Ingresa la dirección ip a escanear\n> "))

print(f"Escaneado objetivo {objetivo}\n\nFavor ser paciente, el escaneo tarda unos minutos...\n")

try:
	for port in range(1,150):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		resultado = s.connect_ex((objetivo, port))
		if resultado == 0:
			print(f"> El puerto {port} está abierto")
		s.close()

except:
	print("\nSaliendo...")
	sys.exit(0)