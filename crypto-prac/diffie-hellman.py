p = int(input('Enter Prime p: '))
g = int(input('Enter Base g: '))

a = int(input("Enter A Private Key (a): "))
b = int(input("Enter B Private Key (b): "))

A = (g ** a) % p
B = (g ** b) % p 

print("A's public key: ",A)
print("B's public key: ",B)

sA = (B ** a) % p
sB = (A ** b) % p 

print("A's shared key: ", sA)
print("B's shared key: ", sB)
