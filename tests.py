import unittest
from utils import print_matrix


class TestT1(unittest.TestCase):
    def setUp(self):
        self.arr_2d = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
        self.arr_2d_1 = [[1, 4, 7],
          [2, 5, 8],
          [3, 6, 9]]

    def test_t1(self):
        self.assertEqual(print_matrix(self.arr_2d), self.arr_2d_1)