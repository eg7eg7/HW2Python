import unittest


def half(matrix, k=1):
    return [
        row_list[row_index:len(row_list)]
        if k==0
        else row_list[0:row_index+1] if k==1
        else [] for row_index, row_list in enumerate(matrix)
    ]


class testHW(unittest.TestCase):

    def test_half(self):
        self.assertEqual(half([], 0), [])
        self.assertEqual(half([], 1), [])
        self.assertEqual(half([[1, 2, 3, 4, 5], [6, 7, 8, 9, "spam"], [11, 12, 13, 14, 15], [16, "stam", 18, 19, 20]]), [[1], [6, 7], [11, 12, 13], [16, "stam", 18, 19]])
        self.assertEqual(half([[1, 2, 3, 4, 5], [6, 7, 8, 9, "spam"], [11, 12, 13, 14, 15], [16, "stam", 18, 19, 20]], 0), [[1, 2, 3, 4, 5], [7,  8,  9, "spam"], [13, 14, 15], [19, 20]])
        self.assertEqual(half([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [6, 7, 8, 9, "spam"], [11, 12, 13, 14, 15], [16, "stam", 18, 19, 20]], 0), [[1, 2, 3, 4, 5], [2, 3, 4, 5], [8, 9, "spam"], [14, 15], [20]])


# helper function - free to use where needed to debug
def print_matrix(matrix):
    print('*****Printing matrix*****')
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print(' ')
    print('*****Printing matrix*****')


if __name__ == "__main__":
    unittest.main()
    print_matrix(half([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [6, 7, 8, 9, "spam"],
                       [11, 12, 13, 14, 15], [16, "stam", 18, 19, 20]]))



