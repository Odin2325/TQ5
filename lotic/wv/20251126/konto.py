class Bankkonto:
    def __init__(self, kontoinhaber):
        self._kontoinhaber = kontoinhaber
        self._kontostand = 0

    def einzahlen(self, betrag):
        if betrag < 0:
            print('Ungültiger Betrag. Vorgang abgebrochen.')
            return False
        self._kontostand += betrag
        return True

    def abheben(self, betrag):
        if betrag < 0:
            print('Ungültiger Betrag. Vorgang abgebrochen.')
            return False
        if betrag > self._kontostand:
            print('Netter Versuch. Leider bist du zu Pleite um soviel Geld abzuheben.')
            return False
        self._kontostand -= betrag
        return True

    def __str__(self):
        return f'Kontoinhaber: {self._kontoinhaber}\nKontostand: {self._kontostand}'


konto1 = Bankkonto('Alice')
print(konto1)
konto1.einzahlen(100)
print(konto1)
konto1.abheben(30)
print(konto1)
konto1.abheben(200)
konto1.einzahlen(-10)
konto1.abheben(-10)
