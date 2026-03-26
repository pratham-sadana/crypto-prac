from cryptography.fernet import Fernet
import hashlib
import base64

k = input("enter key: ").encode()

key = base64.urlsafe_b64encode(hashlib.sha256(k).digest())

f = Fernet(key)

message = input("Enter plaintext: ").encode()

ciphertext = f.encrypt(message).decode()
plaintext = f.decrypt(ciphertext).decode()

print('Encrpyted: ',ciphertext)
print("Decrypted: ",plaintext)
