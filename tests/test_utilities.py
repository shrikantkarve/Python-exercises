import unittest
from algorithms.sorting.qsort import qsort
from utils.Calculator import Calculator

class TestUtilities(unittest.TestCase):

    # Quicksort Tests
    def test_qsort_basic(self):
        arr = [10, 80, 90, 40, 50, 20, 50]
        qsort(arr, 0, len(arr)-1)
        self.assertEqual(arr, sorted([10, 80, 90, 40, 50, 20, 50]))

    def test_qsort_empty(self):
        arr = []
        qsort(arr, 0, len(arr)-1)
        self.assertEqual(arr, [])

    def test_qsort_sorted(self):
        arr = [1, 2, 3, 4, 5]
        qsort(arr, 0, len(arr)-1)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    # Calculator Tests
    def setUp(self):
        self.calc = Calculator()

    def test_calc_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_calc_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(5, 0), "Division by zero error")

    def test_calc_square_root(self):
        self.assertEqual(self.calc.square_root(16), 4)
        self.assertEqual(self.calc.square_root(-1), "Cannot calculate square root of a negative number")

if __name__ == '__main__':
    unittest.main()
