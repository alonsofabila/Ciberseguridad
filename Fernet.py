#cifrado Fernet

#importamos fernet
from cryptography.fernet import Fernet

#Generamos la clave
clave = Fernet.generate_key()

#creamos la instancia de fernet
f = Fernet(clave)

#encriptamos el mensaje
token =  f.encrypt(b'Mensaje Secreto')

#mensaje cifrado
print(token)

#descifrar
des = f.decrypt(token)

#descifrado
print(des)