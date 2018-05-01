import unittest


def half(matrix, k=1):
    print_matrix(matrix)
    if matrix is []:
        return []

    if k is 1:
        next_num_elements = 1
        for row_num, row in enumerate(matrix):
            for i in len(row):
                if next_num_elements < i:
                    matrix[row_num][i] = ''
        next_num_elements += 1
    print_matrix(matrix)
    return matrix


def half_test():
    assert (half([], 0) == [])
    assert (half([], 1) == [])
    assert (half([[1, 2, 3, 4, 5], [6, 7, 8, 9, "spam"], [11, 12, 13, 14, 15], [16, "stam", 18, 19, 20]]) == [[1],[6,7],[11, 12, 13],[16, "stam", 18, 19]])


def print_matrix(matrix):
    for i in range(len(matrix), 1, -1):
        for j in range(len(matrix[i]), 1, -1):
            print(matrix[i][j])


half_test()


