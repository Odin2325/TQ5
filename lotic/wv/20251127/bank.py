class Bankkonto:
    def __init__ (self, kontonummer):
        self._kontonummer = kontonummer
        self._kontostand = 0

    def einzahlen(self, betrag):
        if betrag < 0:
            return False
        self._kontostand += betrag
        return True

    def auszahlen(self, betrag):
        if betrag > self._kontostand:
            return False
        if betrag < 0:
            return False
        self._kontostand -= betrag
        return True

    def get_kontostand(self):
        return self._kontostand

    def info(self):
        print(f'Konto mit der Kontonummer {self._kontonummer}, derzeitiger Kontostand: {self._kontostand}')

class Sparkonto(Bankkonto):
    def __init__ (self, kontonummer, zinssatz):
        super().__init__(kontonummer)
        self._zinssatz = zinssatz
    def zinsen_gutschreiben(self):
        self._kontostand = self._kontostand * (1 + self._zinssatz / 100)

class Girokonto(Bankkonto):
    def __init__ (self, kontonummer, ueberziehungsrahmen):
        super().__init__(kontonummer)
        self._ueberziehungsrahmen = ueberziehungsrahmen
    def auszahlen(self, betrag):
        if betrag < 0:
            return False
        if betrag > self._kontostand + self._ueberziehungsrahmen:
            return False
        self._kontostand -= betrag
        return True

sparkonto = Sparkonto(123456, 5)
sparkonto.einzahlen(100)
sparkonto.info()
sparkonto.zinsen_gutschreiben()
sparkonto.info()
print(sparkonto.get_kontostand())

girokonto = Girokonto(654321, 1000)
girokonto.einzahlen(100)
girokonto.auszahlen(1000)
girokonto.info()

'''
rich = 1000000000
counter = 0

while sparkonto.get_kontostand() < rich:
    sparkonto.zinsen_gutschreiben()
    sparkonto.info()
    counter += 1
    print(f'{counter} x zinsen erhalten')
'''



