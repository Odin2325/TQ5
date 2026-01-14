import unittest
from shop import Produkt, Lebensmittel, Elektronik, Kleidung, Warenkorb

class TestShop(unittest.TestCase):

    def test_produkt_initialisierung(self):
        p = Produkt("Test", 10.0)
        self.assertEqual(p.name, "Test")
        self.assertEqual(p.preis, 10.0)
        self.assertEqual(p.info(), "Produkt Test für 10.0 €")

    def test_lebensmittel_info(self):
        l = Lebensmittel("Apfel", 1.5, "2025-12-31")
        self.assertIn("haltbar bis 2025-12-31", l.info())
        self.assertEqual(l.preis, 1.5)

    def test_elektronik_garantie(self):
        e = Elektronik("Laptop", 999, 2)
        self.assertEqual(e.garantie_dauer, 2)
        self.assertIn("Garantie von 2 Jahren", e.info())

    def test_kleidung_eigenschaften(self):
        k = Kleidung("T-Shirt", 19.99, "L", "Blau")
        self.assertEqual(k.groesse, "L")
        self.assertEqual(k.farbe, "Blau")
        self.assertIn("Größe L", k.info())
        self.assertIn("Farbe Blau", k.info())

    def test_warenkorb_gesamtpreis(self):
        w = Warenkorb([]) 
        w.hinzufuegen(Produkt("A", 10))
        w.hinzufuegen(Produkt("B", 20.5))
        self.assertEqual(w.gesamtpreis(), 30.5)

    def test_warenkorb_leeren(self):
        w = Warenkorb([])
        self.assertEqual(w.gesamtpreis(), 0)
        self.assertEqual(w.auflisten(), "")

    def test_warenkorb_auflisten(self):
        w = Warenkorb([])
        p1 = Produkt("Brot", 2)
        w.hinzufuegen(p1)
        self.assertIn("Brot", w.auflisten())
# ersetzt man Brot zb durch Apfel beim Self wird ein Fehlerausgegeben da es kein Apfel gibt
if __name__ == '__main__':
    unittest.main()