def dezimal_zu_binaer(n):
    if n < 0:
        raise ValueError("Nur nicht-negative Zahlen erlaubt")
    
    if n == 0:
        return "0"
    
    binaer = ""
    
    while n > 0:
        rest = n % 2          # Rest bei Division durch 2 (0 oder 1)
        binaer = str(rest) + binaer  # vorne anhängen (wichtig!)
        n = n // 2            # ganzzahlige Division
    
    return binaer

# Tests
print(dezimal_zu_binaer(13))   # Ausgabe: 1101
print(dezimal_zu_binaer(19))   # Ausgabe: 10011
print(dezimal_zu_binaer(0))    # Ausgabe: 0
print(dezimal_zu_binaer(1))    # Ausgabe: 1
print(dezimal_zu_binaer(255))  # Ausgabe: 11111111