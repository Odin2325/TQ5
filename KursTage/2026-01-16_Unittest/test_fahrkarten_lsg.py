from unittest import TestCase

from fahrkarten_lsg import grundpreis, zonen_zuschlag, rabatt, gesamtpreis


class TestGrundpreis(TestCase):

    def test_negatives_alter(self):
        with self.assertRaises(ValueError):
            grundpreis(-1)

    def test_kind_unter_6_alter_0(self):
        with self.assertRaises(ValueError):
            grundpreis(0)

    def test_kind_6_jahre(self):
        self.assertEqual(grundpreis(6), 1.5)

    def test_kind_17_jahre(self):
        self.assertEqual(grundpreis(17), 1.5)

    def test_erwachsener_18_jahre(self):
        self.assertEqual(grundpreis(18), 3.0)

    def test_erwachsener(self):
        self.assertEqual(grundpreis(30), 3.0)

    def test_negatives_alter(self):
        with self.assertRaises(ValueError):
            grundpreis(-1)


class TestZonenZuschlag(TestCase):

    def test_zone_1(self):
        self.assertEqual(zonen_zuschlag(1), 0.0)

    def test_zone_2(self):
        self.assertEqual(zonen_zuschlag(2), 1.0)

    def test_zone_3(self):
        self.assertEqual(zonen_zuschlag(3), 2.0)

    def test_zone_0_ungueltig(self):
        with self.assertRaises(ValueError):
            zonen_zuschlag(0)

    def test_zone_4_ungueltig(self):
        with self.assertRaises(ValueError):
            zonen_zuschlag(4)


class TestRabatt(TestCase):

    def test_kein_rabatt_ein_ticket(self):
        self.assertEqual(rabatt(1, 10.0), 10.0)

    def test_kein_rabatt_drei_tickets(self):
        self.assertEqual(rabatt(3, 30.0), 30.0)

    def test_rabatt_vier_tickets(self):
        self.assertEqual(rabatt(4, 40.0), 36.0)

    def test_rabatt_fuenf_tickets(self):
        self.assertEqual(rabatt(5, 50.0), 45.0)

    def test_negative_ticketanzahl(self):
        with self.assertRaises(ValueError):
            rabatt(-1, 10.0)


class TestGesamtpreis(TestCase):

    def test_erwachsener_zone1_ein_ticket(self):
        self.assertEqual(gesamtpreis(30, 1), 3.0)

    def test_kind_zone2_ein_ticket(self):
        self.assertEqual(gesamtpreis(10, 2), 2.5)

    def test_kind_unter_6_zone3(self):
        with self.assertRaises(ValueError):
            gesamtpreis(3, 3)

    def test_erwachsener_zone1_zwei_tickets(self):
        self.assertEqual(gesamtpreis(30, 1, ticket_anzahl=2), 6.0)

    def test_erwachsener_zone2_vier_tickets_mit_rabatt(self):
        self.assertAlmostEqual(
            gesamtpreis(30, 2, ticket_anzahl=4),
            14.4
        )
