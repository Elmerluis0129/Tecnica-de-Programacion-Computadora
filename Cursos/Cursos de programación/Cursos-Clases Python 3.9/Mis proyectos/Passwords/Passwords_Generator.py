import random


def main():
    minus = "abcdefghijklmnopqrstuvwxyz"
    mayus = minus.upper()
    numeros = "0123456789"
    simbolos = "!@&*():,.?+~-=#$%"

    base = minus+mayus+numeros+simbolos
    longi = 20
    
    for _ in range(10):
        muestra = random.sample(base, longi) #Aquí ponemos a que al azar escoja x cantidad de letras, en el primer parametro se le indica de dónde las escogerá, y en el segundo, cuántas escogerá!
        password = "".join(muestra) #Aqui unimos todo lo que escogio al azar
        print(f"*----------------------------------------------------------------------------*\nPassword: {password}\n") 

    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nSaliendo...")
        exit()