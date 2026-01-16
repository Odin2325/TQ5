from unittest import TestCase

from notenverwaltung_lsg import ist_gueltige_note, durchschnitt, beste_note, note_zu_text


class TestIstGueltigeNote(TestCase):

    def test_gueltige_noten(self):
        self.assertTrue(ist_gueltige_note(1))
        self.assertTrue(ist_gueltige_note(3))
        self.assertTrue(ist_gueltige_note(6))

    def test_ungueltige_noten_zahlen(self):
        self.assertFalse(ist_gueltige_note(0))
        self.assertFalse(ist_gueltige_note(7))
        self.assertFalse(ist_gueltige_note(-1))

    def test_ungueltige_typen(self):
        self.assertFalse(ist_gueltige_note(2.5))
        self.assertFalse(ist_gueltige_note("2"))
        self.assertFalse(ist_gueltige_note(None))


class TestDurchschnitt(TestCase):

    def test_durchschnitt_mehrere_noten(self):
        self.assertAlmostEqual(durchschnitt([2, 3, 4]), 3.0)

    def test_durchschnitt_eine_note(self):
        self.assertEqual(durchschnitt([1]), 1.0)

    def test_leere_liste(self):
        with self.assertRaises(ValueError):
            durchschnitt([])

    def test_ungueltige_note_in_liste(self):
        with self.assertRaises(ValueError):
            durchschnitt([2, 3, 7])


class TestBesteNote(TestCase):

    def test_beste_note_normal(self):
        self.assertEqual(beste_note([2, 3, 5]), 2)

    def test_beste_note_unsortiert(self):
        self.assertEqual(beste_note([6, 1, 4, 2]), 1)

    def test_leere_liste(self):
        with self.assertRaises(ValueError):
            beste_note([])


class TestNoteZuText(TestCase):

    def test_alle_noten(self):
        self.assertEqual(note_zu_text(1), "sehr gut")
        self.assertEqual(note_zu_text(2), "gut")
        self.assertEqual(note_zu_text(3), "befriedigend")
        self.assertEqual(note_zu_text(4), "ausreichend")
        self.assertEqual(note_zu_text(5), "mangelhaft")
        self.assertEqual(note_zu_text(6), "ungenügend")

    def test_ungueltige_note(self):
        with self.assertRaises(ValueError):
            note_zu_text(0)

        with self.assertRaises(ValueError):
            note_zu_text(7)