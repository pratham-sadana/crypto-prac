plaintext= input("enter plaintext: ")
key = input('Enter key (same length): ')

ciphertext = ''
for p, k in zip(plaintext,key):
    ciphertext += chr(ord(p) ^ ord(k))

print('Encrpyted: ', ciphertext.encode().hex())

decr = ''

for c, k in zip(ciphertext,key):
    decr +=chr(ord(c) ^ ord(k) )

print('decrypted: ', decr)