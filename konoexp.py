class NegativerBetragError(Exception):
    """Bei Negativ Betrag."""
    pass
class UnzureichendesGuthabenError(Exception):
    """Kontostand reicht nicht aus ."""
    pass
class Bankkonto:
    def __init__(self, kontoinhaber):
        self._kontoinhaber = kontoinhaber
        self._kontostand = 0

    def einzahlen(self, betrag):
        if betrag < 0:
            raise NegativerBetragError("Es kann kein negativer Betrag eingezahlt werden!")
        self._kontostand += betrag

    def abheben(self, betrag):
        if betrag < 0:
            raise NegativerBetragError("Es kann kein negativer Betrag abgehoben werden!")

        if betrag > self._kontostand:
            raise UnzureichendesGuthabenError("Nicht genügend Guthaben vorhanden!")

        self._kontostand -= betrag

    def __str__(self):
        return f"Inhaber: {self._kontoinhaber}, Kontostand: {self._kontostand}€"
# Testlauf
konto1 = Bankkonto("Rübezahl")

print(konto1)

# Einzahlen
try:
    konto1.einzahlen(100)
except Exception as e:
    print("Fehler:", e)
print(konto1)

# Abheben korrekt
try:
    konto1.abheben(30)
except Exception as e:
    print("Fehler:", e)
print(konto1)

try:
    konto1.abheben(200)
except Exception as e:
    print("Fehler:", e)
print(konto1)

try:
    konto1.einzahlen(-10)
except Exception as e:
    print("Fehler:", e)
try:
    konto1.abheben(-10)
except Exception as e:
    print("Fehler:", e)
