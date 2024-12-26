#Program No 12
#python program to implement symmetric encryption using python library

from cryptography.fernet import Fernet
key=Fernet.generate_key()
f=Fernet(key)
token=f.encrypt(b"Welcome to AIMCA Lab")
print(token)
d=f.decrypt(token)
print(d)


