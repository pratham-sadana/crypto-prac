import hashlib  

message = input('Enter Message: ')
encodedmessage = message.encode()

hashedmessage = hashlib.sha256(encodedmessage).hexdigest()

print('Message: ',message)
print('Encoded Message: ',encodedmessage)
print('Hashed Message: ', hashedmessage)

