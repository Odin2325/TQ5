binary = '1111110'
pos_val = 1
dez = 0

for i in range (len(binary)-1, -1, -1):
    if binary[i] == '1':
        dez += pos_val
    pos_val *= 2

print(dez)
