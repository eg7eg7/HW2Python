import unittest


def half(matrix, k=1):
    # TODO requirement - one lined body...

    if k is 0:
        for i, row in enumerate(matrix):
            for k in range(i):
                del matrix[i][0]
    if k is 1:
        next_num_elements = 1
        for row_num in range(len(matrix)):
            for i in range(len(matrix[row_num])-1, 0, -1):
                if next_num_elements < i+1:
                    del matrix[row_num][i]
            next_num_elements += 1

    return matrix


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


