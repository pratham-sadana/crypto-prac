import hmac
import hashlib

key = input('Enter Key: ').encode()
msg = input('Enter Message: ').encode()

hmacv = hmac.new(key,msg,hashlib.sha256).hexdigest()

print('HMAC Value: ',hmacv)
