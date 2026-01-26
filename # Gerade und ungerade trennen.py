# Gerade und ungerade trennen

# Aufgabe: Lies Zahlen ein und erstelle zwei Listen: gerade und ungerade. Gib beide Listen aus.
# Beispiel: Input: "1 2 3 4" → Output: "Gerade: [2,4], Ungerade: [1,3]"

eingabe = input('Zahlen eingeben (durch Leerzeichen getrennt)')

gerade = []
ungerade = []

for wert in eingabe.split():
    try:
        zahl = int(wert)
        if zahl % 2 == 0:
            gerade.append(zahl)
        else:
            ungerade.append(zahl)
    except ValueError:
        print(f"'{wert}' ist keine Zahl und wird ignoriert.")

print('Gerade Zahlen:', gerade)
print('Ungerade Zahlen:', ungerade)