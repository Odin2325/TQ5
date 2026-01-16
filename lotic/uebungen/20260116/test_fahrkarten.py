import unittest
from unittest import TestCase

from fahrkarten import grundpreis, zonen_zuschlag, rabatt, gesamtpreis

class TestGrundpreis(TestCase):
    def test_gueltiges_alter(self):
        with self.assertRaises(ValueError):
            grundpreis(5)
        with self.assertRaises(ValueError):
            grundpreis('5')
    def test_price(self):
        self.assertEqual(grundpreis(6), 1.5)
        self.assertEqual(grundpreis(18), 3.0)

class TestZonenZuschlag(TestCase):
    def test_gueltige_zone(self):
        with self.assertRaises(ValueError):
            zonen_zuschlag('1')
        with self.assertRaises(ValueError):
            zonen_zuschlag(0)
        with self.assertRaises(ValueError):
            zonen_zuschlag(4)
    def test_expected_values(self):
        self.assertEqual(zonen_zuschlag(1), 0.0)
        self.assertEqual(zonen_zuschlag(2), 1.0)
        self.assertEqual(zonen_zuschlag(3), 2.0)

class TestRabatt(TestCase):
    def test_invalid_count(self):
        with self.assertRaises(ValueError):
            rabatt(-1, 10)
    def test_correct_rabatt(self):
        self.assertAlmostEqual(rabatt(10, 10), 90)
        self.assertAlmostEqual(rabatt(3, 10), 30)

class TestGesamtpreis(TestCase):
    def test_invalid_age(self):
        with self.assertRaises(ValueError):
            gesamtpreis(5, 1, 4)
    def test_invalid_zone(self):
        with self.assertRaises(ValueError):
            gesamtpreis(8, -1, 4)
    def test_expected_values(self):
        self.assertAlmostEqual(gesamtpreis(7, 1, 1), (1.5 + 0) * 1  )

if __name__ == '__main__':
    unittest.main()
