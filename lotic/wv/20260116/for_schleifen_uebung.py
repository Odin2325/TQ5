meine_liste = [5, 7, 9, 10, 11, 36, 2342]

#print(len(meine_liste))

# for schleife mit Range die der länge der Liste entspricht.
for zähler in range (len(meine_liste)):
    print(f'Das {zähler} Element meiner Liste hat den Wert {meine_liste[zähler]}')

# for schleife ohne Range. Geht über jedes Element einer Liste
for element in meine_liste:
    print(element)
