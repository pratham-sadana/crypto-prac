key = int(input('Key: '))
text =  input('text: ')

function = lambda s, k: ''.join(
    chr ((ord(c) - 65 + k ) % 26 + 65) if c.isupper() else
    chr ((ord(c) - 97 + k ) % 26 + 97) if c.islower() else 
    c for c in s
)

ciphertext = function (text,key)
d_text = function (ciphertext,-key)

print("Encrypted: ",ciphertext)
print("Decrypted: ",d_text)
