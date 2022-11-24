#A way to do it.
f=open("abc.txt", "w") #Sirve para abrir o crear archivos, en este caso, para crear un documento de texto, con e:\\ram\\ antes del nombre, puedes cambiar la ubicación
n=int(input("How many lines: "))
for i in range(n):
    s=input("Enter string: ")
    f.write(s+"\n")#Aquí, sirve para escribir en el/los archivo/s
f.close()#Para cerrar el/los archivo/s

#An another way.
f=open("abc.txt", "w") #Sirve para abrir o crear archivos, en este caso, para crear un documento de texto, con e:\\ram\\ antes del nombre, puedes cambiar la ubicación
n=int(input("How many lines: "))
L=[]
for i in range(n):
    s=input("Enter string: ")
    L.append(s+"\n")
    
f.writelines(L)#Aquí, sirve para escribir en el/los archivo/s
f.close()#Para cerrar el/los archivo/s
