def maximum_durch_sortieren(liste):
    if not liste:
        return None
    liste.sort() 
    return liste[-1]

print(f"Test 1 (Normal): {maximum_durch_sortieren([1, 5, 3])}") 
print(f"Test 2 (Negativ): {maximum_durch_sortieren([-10, -5, -20])}")
print(f"Test 3 (Leer): {maximum_durch_sortieren([])}")
