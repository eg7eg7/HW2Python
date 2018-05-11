import unittest
from itertools import *
from proj import *


class TestHW(unittest.TestCase):

    def test_half(self):
        self.assertEqual(half([], 0), [])
        self.assertEqual(half([], 1), [])
        self.assertEqual(half([[1, 2, 3, 4, 5], [6, 7, 8, 9, "spam"], [11, 12, 13, 14, 15], [16, "stam", 18, 19, 20]]),
                         [[1], [6, 7], [11, 12, 13], [16, "stam", 18, 19]])
        self.assertEqual(
            half([[1, 2, 3, 4, 5], [6, 7, 8, 9, "spam"], [11, 12, 13, 14, 15], [16, "stam", 18, 19, 20]], 0),
            [[1, 2, 3, 4, 5], [7, 8, 9, "spam"], [13, 14, 15], [19, 20]])
        self.assertEqual(half(
            [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [6, 7, 8, 9, "spam"], [11, 12, 13, 14, 15], [16, "stam", 18, 19, 20]],
            0), [[1, 2, 3, 4, 5], [2, 3, 4, 5], [8, 9, "spam"], [14, 15], [20]])

    def test_decrypt(self):
        self.assertEqual(decrypt("vrorqjdqgwkdqnviruwkhilvk"), "solongandthanksforthefish")
        self.assertEqual(decrypt("vsdp "), "spam ")
        self.assertEqual(decrypt("a"), "x")
        self.assertEqual(decrypt("a", 1), "z")
        self.assertEqual(decrypt("a", 26), "a")
        self.assertEqual(decrypt("a", 52), "a")
        self.assertEqual(decrypt("a", 0), "a")

    def test_merge(self):
        g = divisable_by(4, 21)
        my_merge_iter = merge(g, [2, 3, 7, 10, 11])
        self.assertEqual(next(my_merge_iter), 0)
        self.assertEqual(next(my_merge_iter), 2)
        self.assertEqual(list(islice(my_merge_iter, 9)), [3, 4, 7, 8, 10, 11, 12, 16, 20])

        g = divisable_by(3, 35)
        my_merge_iter = merge(g, [2, 5, 8, 10])
        self.assertEqual(list(islice(my_merge_iter, 8)), [0, 2, 3, 5, 6, 8, 9, 10])

    def test_rank(self):
        file_name = 'winners_test.txt'
        self.assertEqual(list(islice(rank(file_name, 'total'), 3)), ["\"USA\":2521", "\"Great-Britain\":847", "\"Israel\":9"])
        self.assertEqual(list(islice(rank(file_name, 'weighted'), 3)), ["\"USA\":5359", "\"Great-Britain\":1668", "\"Israel\":12"])
        self.assertEqual(list(islice(rank(file_name, 'gold'), 3)), ["\"USA\":1022", "\"Great-Britain\":263", "\"Israel\":1"])
        self.assertEqual(list(islice(rank(file_name, 'silver'), 3)), ["\"USA\":794", "\"Great-Britain\":295", "\"Israel\":1"])
        self.assertEqual(list(islice(rank(file_name, 'arad'), 3)), ["\"USA\":705", "\"Great-Britain\":289", "\"Israel\":7"])
        self.assertEqual(list(islice(rank(file_name, 'svsd'), 3)), ["\"Israel\":-1", "\"USA\":-1", "\"Great-Britain\":-1"])


if __name__ == "__main__":
    unittest.main(exit=False)