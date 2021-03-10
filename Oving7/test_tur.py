import unittest
from unittest import TestCase
from tur import Tur, Posisjon


class TestTur(TestCase):

    def test_correct_sluttidspunkt(self):
        self.tur = Tur("Test", 2, 5)
        self.assertTrue(self.tur.starttidspunkt < self.tur.sluttidspunkt)
        with self.assertRaises(ValueError):
            Tur("Test", 5, 2)

    def test_add_posisjon(self):
        self.tur = Tur("Test", 2, 5)
        position = Posisjon(2, 5, 3)
        self.tur.add_posisjon(position)
        self.assertTrue(self.tur.posisjoner[-1] == position)

    def test_add_posisjon_koordinater(self):
        self.tur = Tur("Test", 2, 5)
        self.tur.add_posisjon_koordinater(2, 5, 3)
        self.assertTrue(self.tur.posisjoner[-1] == Posisjon(2, 5, 3))

        self.tur = Tur("Test", 2, 3)
        self.tur.add_posisjon_koordinater(2, 3, 2)
        self.tur.add_posisjon_koordinater(20, 5, 20)
        self.tur.add_posisjon_koordinater(18, 13, 22)
        self.tur.add_posisjon_koordinater(2, 3, 2)

        self.assertTrue(self.tur.hoydemeter() == 40)
        self.assertTrue(self.tur.er_rundtur())

        self.tur = Tur("Test", 2, 3)
        self.tur.add_posisjon_koordinater(5, 3, 10)
        self.tur.add_posisjon_koordinater(15, 5, 18)
        self.tur.add_posisjon_koordinater(12, 15, 12)

        self.assertTrue(self.tur.hoydemeter() == 14)
        self.assertFalse(self.tur.er_rundtur())

    def test_hoydemeter(self):
        self.tur = Tur("Test", 2, 5)
        self.tur.add_posisjon_koordinater(2, 5, 3)
        self.tur.add_posisjon_koordinater(4, 6, 5)
        self.assertTrue(self.tur.hoydemeter() == 2)
        self.tur.add_posisjon_koordinater(5, 3, 10)
        self.assertTrue(self.tur.hoydemeter() == 7)

        self.tur = Tur("Test", 2, 5)
        self.tur.add_posisjon_koordinater(2, 5, 3)
        self.tur.add_posisjon_koordinater(4, 6, 5)
        self.tur.add_posisjon_koordinater(4, 6, 8)
        self.tur.add_posisjon_koordinater(2, 5, 3)
        self.assertTrue(self.tur.hoydemeter() == 10)

    def test_er_rundtur(self):
        self.tur = Tur("Test", 2, 5)
        self.tur.add_posisjon_koordinater(2, 5, 3)
        self.tur.add_posisjon_koordinater(4, 6, 5)
        self.tur.add_posisjon_koordinater(2, 5, 3)
        self.assertTrue(self.tur.er_rundtur())
        self.tur.add_posisjon_koordinater(4, 6, 5)
        self.assertFalse(self.tur.er_rundtur())


if __name__ == "__main__":
    unittest.main()
