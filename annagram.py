def ist_anagramm(wort1, wort2):
    # Groß-/Kleinschreibung ignorieren und Leerzeichen entfernen
    wort1 = wort1.lower().replace(" ", "")
    wort2 = wort2.lower().replace(" ", "")
    
    # Buchstaben sortieren und vergleichen
    return sorted(wort1) == sorted(wort2)

# Tests
print(ist_anagramm("listen", "silent"))      # True
print(ist_anagramm("hello", "world"))        # False
print(ist_anagramm("Dormitory", "Dirty room"))  # True (Leerzeichen werden ignoriert)
print(ist_anagramm("Astronomer", "Moon starer")) # True