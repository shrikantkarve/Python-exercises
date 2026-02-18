import unittest
import sys
import os

# Add the parent directory to sys.path to import the module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dynamic_programming.egg_drop import egg_drop


class TestEggDrop(unittest.TestCase):

    def test_one_egg_ten_floors(self):
        """1 egg, 10 floors -> must try each floor linearly = 10"""
        self.assertEqual(egg_drop(1, 10), 10)

    def test_two_eggs_six_floors(self):
        """2 eggs, 6 floors -> 3 trials"""
        self.assertEqual(egg_drop(2, 6), 3)

    def test_two_eggs_ten_floors(self):
        """2 eggs, 10 floors -> 4 trials"""
        self.assertEqual(egg_drop(2, 10), 4)

    def test_two_eggs_hundred_floors(self):
        """Classic interview question: 2 eggs, 100 floors -> 14"""
        self.assertEqual(egg_drop(2, 100), 14)

    def test_three_eggs_fourteen_floors(self):
        """3 eggs, 14 floors -> 4 trials"""
        self.assertEqual(egg_drop(3, 14), 4)

    def test_one_egg_one_floor(self):
        """Trivial: 1 egg, 1 floor -> 1"""
        self.assertEqual(egg_drop(1, 1), 1)

    def test_many_eggs_one_floor(self):
        """Many eggs but only 1 floor -> 1"""
        self.assertEqual(egg_drop(10, 1), 1)

    def test_zero_floors(self):
        """No floors -> 0 trials needed"""
        self.assertEqual(egg_drop(2, 0), 0)

    def test_two_eggs_one_floor(self):
        """2 eggs, 1 floor -> 1"""
        self.assertEqual(egg_drop(2, 1), 1)

    def test_three_eggs_twenty_five_floors(self):
        """3 eggs, 25 floors -> 5 trials"""
        self.assertEqual(egg_drop(3, 25), 5)


if __name__ == '__main__':
    unittest.main()
