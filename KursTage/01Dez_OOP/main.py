from buch import Buch
from dvd import Dvd
from bibliothek import Bibliothek

def importiere_buecher(bibliothek, datei="buecher.txt"):
    with open(datei, encoding="utf-8") as file:
        inhalt = file.read()

    for zeile in inhalt.splitlines():
        teile = zeile.split(",")
        buecher = buecher(teile[0], int(teile[1]), teile[2], int(teile[3]))
        self.hinzufuegen(buecher)

# Bibliothek erstellen
bibo = Bibliothek()

# # Medien erstellen
# buch1 = Buch("Harry Potter", 1997, "J.K. Rowling", 336)
# dvd1 = Dvd("Inception", 2010, 148, "Christopher Nolan")

# # Zur Bibliothek hinzufuegen
# bibo.hinzufuegen(buch1)
# bibo.hinzufuegen(dvd1)

# Auflisten
bibo.auflisten()
