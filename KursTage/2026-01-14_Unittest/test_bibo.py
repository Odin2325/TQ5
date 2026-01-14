import unittest
from bibo import Bibliothek, Medium, Buch, Dvd


class TestMedium(unittest.TestCase):

    def test_medium_info(self):
        m = Medium("Testtitel", 2020)
        self.assertEqual(m.info(), "Medium: Testtitel (2020)")


class TestBuch(unittest.TestCase):

    def test_buch_attribute(self):
        b = Buch("Python", 2021, "Guido", 350)
        self.assertEqual(b.titel, "Python")
        self.assertEqual(b.autor, "Guido")
        self.assertEqual(b.seitenzahl, 350)
        self.assertEqual(b.erscheinungsjahr, 2021)

    def test_buch_info(self):
        b = Buch("Python", 2021, "Guido", 350)
        expected = (
            "Medium: Python (2021), Typ Buch, Autor: Guido, Seiten: 350"
        )
        self.assertEqual(b.info(), expected)


class TestDvd(unittest.TestCase):

    def test_dvd_attribute(self):
        d = Dvd("Matrix", 1999, 136, "Wachowski")
        self.assertEqual(d.titel, "Matrix")
        self.assertEqual(d.erscheinungsjahr, 1999)
        self.assertEqual(d.spielzeit, 136)
        self.assertEqual(d.regisseur, "Wachowski")

    def test_dvd_info(self):
        d = Dvd("Matrix", 1999, 136, "Wachowski")
        expected = (
            "Medium: Matrix (1999), Typ DVD, Spielzeit: 136 Min, Regisseur: Wachowski"
        )
        self.assertEqual(d.info(), expected)


class TestBibliothek(unittest.TestCase):

    def setUp(self):
        self.bib = Bibliothek()
        self.buch = Buch("Python", 2021, "Guido", 300)
        self.dvd = Dvd("Matrix", 1999, 136, "Wachowski")

    def test_hinzufuegen(self):
        self.bib.hinzufuegen(self.buch)
        self.assertIn(self.buch, self.bib.medien)

    def test_entfernen(self):
        self.bib.hinzufuegen(self.buch)
        self.bib.entfernen(self.buch)
        self.assertNotIn(self.buch, self.bib.medien)

    def test_entfernen_nicht_vorhanden(self):
        # Sollte keinen Fehler werfen
        self.bib.entfernen(self.buch)
        self.assertEqual(len(self.bib.medien), 0)

    def test_seiten_nur_buecher(self):
        self.bib.hinzufuegen(self.buch)
        self.bib.hinzufuegen(self.dvd)
        self.assertEqual(self.bib.seiten(), 300)

    def test_auflisten_print(self):
        pass


if __name__ == "__main__":
    unittest.main()
