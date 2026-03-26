# n = p*q
# phi(n) = (p-1)*(q-1)
# choose e, i.e gcd(e,phi(n)) = 1
# encryption: c = (m ** e) % n
# d*e % n = 1
# decryption: m = (c**d) % n 
def gcd(a,b):
    while b:
        a,b = b, a % b
    return a

def finde(pn):
    e=2
    while gcd(e,pn) !=1:
        e+=1
    return e

def modinv(e,pn):
    for i in range(1,pn):
        if (i*e) % pn == 1:
            return i

p = int(input('Enter prime p: '))
q = int(input('Enter prime q: '))

n = p * q
pn = (p-1) * (q-1)

e = finde(pn)
d = modinv(e,pn)
print('Public key:', e )
print('Private key:', d )

m = int(input('Enter message to encrypt: '))
puk = int(input('Enter Public key: '))
c = (m ** e) % n
print('Encryted: ', c)

em = int(input('For Decrypting, Enter the Encrypted Message: '))
pxk = int(input('Enter Private key: '))
dm = (c ** d) % n

print('Decrpted Message: ',dm)
