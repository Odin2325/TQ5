import unittest
from unittest import TestCase

from notenverwaltung import ist_gueltige_note, durchschnitt, beste_note, note_zu_text

class TestIstGueltigeNote(TestCase):
    # 1 test für gültige Noten (1, 3, 6)
    def test_gueltig(self):
        self.assertTrue(ist_gueltige_note(1))
        self.assertTrue(ist_gueltige_note(3))
        self.assertTrue(ist_gueltige_note(6))

    # 1 test für ungültige Noten (0, 7, -1)
    def test_ungueltig(self):
        self.assertFalse(ist_gueltige_note(0))
        self.assertFalse(ist_gueltige_note(7))
        self.assertFalse(ist_gueltige_note(-1))

    # 1 test für ungültige Typen (2.5, "2", None)
    def test_ungueltig_type(self):
        self.assertFalse(ist_gueltige_note(2.5))
        self.assertFalse(ist_gueltige_note('2'))
        self.assertFalse(ist_gueltige_note(None))


class TestDurchschnitt(TestCase):
    # 1 test für durchschnitt mehrerer noten z.B. [2, 3, 4]
    def test_multiple(self):
        self.assertAlmostEqual(durchschnitt([2, 3, 4]), (2+3+4)/3)
    # 1 test für durchschnitt einzelner note z.B. [1]
    def test_single(self):
        self.assertEqual(durchschnitt([1]), 1)
    # 1 test für Leere Liste []
    def test_empty(self):
        with self.assertRaises(ValueError):
            durchschnitt([])
    # 1 test für ungültige Note in Liste z.B. [2, 3, 7]
    def test_invalid(self):
        with self.assertRaises(ValueError):
            durchschnitt([2, 3, 7])

class TestBesteNote(TestCase):
    # 1 test für beste Note z.B. [2, 3, 5]
    def test_sorted(self):
        self.assertEqual(beste_note([2, 3, 5]), 2)
    # 1 test für beste Note in unsortierter Liste z.B. [6, 1, 4, 2]
    def test_unsorted(self):
        self.assertEqual(beste_note([6, 1, 4, 2]), 1)
    # 1 test für leere Liste []
    def test_empty(self):
        with self.assertRaises(ValueError):
            beste_note([])

class TestNoteZuText(TestCase):

    # 1 test für alle Noten 1 -> "sehr gut", usw

    def test_allvalid(self):
        self.assertEqual(note_zu_text(1), 'sehr gut')
        self.assertEqual(note_zu_text(2), 'gut')
        self.assertEqual(note_zu_text(3), 'befriedigend')
        self.assertEqual(note_zu_text(4), 'ausreichend')
        self.assertEqual(note_zu_text(5), 'mangelhaft')
        self.assertEqual(note_zu_text(6), 'ungenügend')
    # 1 test für ungültige Noten, z.B. 0, 7
    def test_invalid(self):
        with self.assertRaises(ValueError):
            note_zu_text(0)
        with self.assertRaises(ValueError):
            note_zu_text(7)

if __name__ == '__main__':
    unittest.main()
