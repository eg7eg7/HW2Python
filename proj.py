import unittest


def half(matrix, k=1):
    # TODO requirement - one lined body...
    print_matrix(matrix)
    if matrix is []:
        return []

    if k is 1:
        next_num_elements = 1
        for row_num in range(len(matrix)):
            list_mat = matrix[row_num]
            print(list_mat, "list")
            k=0
            for i in range(len(list_mat)):
                if next_num_elements < i:
                    del matrix[row_num][i-k]
                    k+=1
        next_num_elements += 1
    print_matrix(matrix)
    return matrix


def half_test():
    #assert (half([], 0) == [])
    #assert (half([], 1) == [])
    assert (half([[1, 2, 3, 4, 5], [6, 7, 8, 9, "spam"], [11, 12, 13, 14, 15], [16, "stam", 18, 19, 20]]) == [[1],[6,7],[11, 12, 13],[16, "stam", 18, 19]])


def print_matrix(matrix):
    print('*****')
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print(' ')
    print('*****')


half_test()


