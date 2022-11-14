from cryptography.fernet import Fernet as FN

password_to_encrypted = "Pamela y yo estamos mangando"

#Genera una clave en formato de secuencias de bytes
#Encriptamamos la contraseña proporcionada
key = FN.generate_key()
object_encrypted = FN(key)
password_encrypted = object_encrypted.encrypt(str.encode(password_to_encrypted))
print("Password encrypted:\n>", password_encrypted)


#Aqui desencriptamos las claves!!
passwords_decrypted_bytes = object_encrypted.decrypt(password_encrypted)
passwords_decrypted = passwords_decrypted_bytes.decode()
print("Password decrypted:\n>", passwords_decrypted)