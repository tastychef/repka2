import unittest
from utils2 import print_matrix


class Test1(unittest.TestCase):
    """test for print_matrix"""

    def setUp(self):
        self.arr_2d = [[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9]]
        self.arr_2d_1 = [[1, 4, 7],
                         [2, 5, 8],
                         [3, 6, 9]]

    def test_1(self):
        self.assertEqual(print_matrix(self.arr_2d), self.arr_2d_1)
# if __name__ == "__main__":


# class Test1(unittest.TestCase):
#     """test for print_matrix"""
#     def setUp(self):
#         self.arr_2d = [[1, 2, 3],
#                        [4, 5, 6],
#                        [7, 8, 9]]
#         self.arr_2d_1 = [[1, 4, 7],
#                          [2, 5, 8],
#                          [3, 6, 9]]
#
#     def test_t1(self):
#         self.assertEqual(print_matrix(self.arr_2d), self.arr_2d_1)
