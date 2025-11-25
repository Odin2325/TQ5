#Bubblesort

meine_liste = [78, 18, 11, 6, 3, 24, 22, 4]

for i in range(len(meine_liste)):
    for j in range(len(meine_liste)-i):
        if j+1 >= len(meine_liste):
            continue
        temp = meine_liste[j]
        if meine_liste[j] > meine_liste[j+1]:
            meine_liste[j] = meine_liste[j+1]
            meine_liste[j+1] = temp
print('Sortierte Liste')
print(meine_liste)

print(f'Das kleinste Element in der Liste ist {meine_liste[0]}')