def liste_umdrehen(zahlen):
    umgedreht = []
    for i in range(len(zahlen) - 1, -1, -1):  # von letztem Index bis 0 rückwärts
        umgedreht.append(zahlen[i])
    return umgedreht

# Test
liste = [1, 2, 3, 4, 5]
print(liste_umdrehen(liste))  # Ausgabe: [5, 4, 3, 2, 1]