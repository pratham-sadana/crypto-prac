key = int(input('Enter key: '))
txt = input('Message: ')

rows = [''] * key

i = 0
step = 1

for c in txt:
    rows[i] += c
    if i == 0:
        step = 1
    elif i == key - 1:
        step = -1
    i += step

cipher = ''.join(rows)

print('Ciphertext:', cipher)

#decrypt

res = [''] * len(txt)
pattern = []
i, step = 0, 1
for _ in txt:
    pattern.append(i)
    if i == 0:
        step = 1
    elif i == key - 1:
        step = -1
    i += step
pos = 0
rows = [''] * key
for r in range(key):
    count = pattern.count(r)
    rows[r] = cipher[pos:pos+count]
    pos += count
idx = [0] * key
for i in range(len(txt)):
    r = pattern[i]
    res[i] = rows[r][idx[r]]
    idx[r] += 1
d = ''.join(res)
print("Decrypted:", d)