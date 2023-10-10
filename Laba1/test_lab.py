import unittest

from lab1_variant2 import find_unsorted_subarray


class TestLabs(unittest.TestCase):

    def test_find_unsorted_subarray(self):
        array1 = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
        array2 = [1, 2, 3, 4, 5, 6, 7, 9]
        array3 = [9, 8, 7, 6, 5, 4, 3]
        array4 = [2]
        self.assertEqual(find_unsorted_subarray(array1), (3, 9))
        self.assertEqual(find_unsorted_subarray(array2), (-1, -1))
        self.assertEqual(find_unsorted_subarray(array3), (0, 7))
        self.assertEqual(find_unsorted_subarray(array4), (-1, -1))


if __name__ == "__main__":
    unittest.main()
