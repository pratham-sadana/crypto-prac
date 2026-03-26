key = input('key: ')
txt = input("text: ")

n = len(key)
rows = []
for i in range(0,len(txt),n):
    rows.append(txt[i:i+n])

order = sorted(range(n), key= lambda i: key[i])

ct = ''
for i in order:
    for r in rows:
        if i <  len(r):
            ct +=   r[i]

print('ciphertxt: ',ct)

col_len = len(txt) // n
extra = len(txt) % n

cols = {}
pos = 0

for idx, i in enumerate(order):
    l = col_len + (1 if idx < extra else 0)
    cols[i] = ct[pos:pos+l]
    pos += l

num_rows = (len(txt) + n - 1) // n
res = ''
for i in range(num_rows):
    for j in range(n):
        if i < len(cols[j]):
            res += cols[j][i]

print("Decrypted:", res)
