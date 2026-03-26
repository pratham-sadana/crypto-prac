key = input("Enter key: ")
text = input("Enter text: ")

key = key.replace('j', 'i')
text = text.replace('j', 'i').replace(' ', '')

text = ''.join(filter(str.isalpha, text))

alpha = "abcdefghiklmnopqrstuvwxyz"
matrix = ""

for ch in key + alpha:
    if ch not in matrix:
        matrix += ch

def pos(c):
    i = matrix.index(c)
    return i//5, i%5

res = ""

for i in range(0, len(text), 2):
    a = text[i]
    b = text[i+1] if i+1 < len(text) else 'x'

    r1, c1 = pos(a)
    r2, c2 = pos(b)

    if r1 == r2: # same row
        res += matrix[r1 * 5 + (c1 + 1) % 5]
        res += matrix[r2 * 5 + (c2 + 1) % 5]
    elif c1 == c2: # same column
        res += matrix[((r1 + 1) % 5) * 5 + c1]
        res += matrix[((r2 + 1) % 5) * 5 + c2]
    else: # rectangle
        res += matrix[r1 * 5 + c2]
        res += matrix[r2 * 5 + c1]

print("Encrypted:", res)
