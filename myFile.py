def half(matrix, k=1):
    return [
        []
    ]
    # TODO requirement - one lined body...

    return [
        row_list[row_index:len(row_list)]
        if k==0
        else row_list[0:row_index+1] if k==1
        else [] for row_index, row_list in enumerate(matrix)
    ]
    # # if k==0:
    # for row_index, row_list in enumerate(matrix):
    #         for col_index in range(row_index, len(row_list)):
    #             result_matrix = matrix[row_index][col_index]
    #
    # if k==0:
    #     for row_index, row_list in enumerate(matrix):
    #             result_matrix[row_index] = row_list[row_index:len(row_list)]
    #
    # if k==1:
    #     for row_index, row_list in enumerate(matrix):
    #         result_matrix[row_index] = row_list[0:row_index+1]


    if k==1:
        for row_index, row_list in enumerate(matrix):
            for col_index in range(0,  row_index+1):
                result_matrix[row_index] = matrix[row_index][col_index]

    if k is 0:
        for i, row in enumerate(matrix):
            for k in range(i):
                del matrix[i][0]

def print_matrix(matrix):
    print('*****Printing matrix*****')
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print(' ')
    print('*****Printing matrix*****')


if __name__ == "__main__":
    print_matrix(half([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [6, 7, 8, 9, "spam"],
                       [11, 12, 13, 14, 15], [16, "stam", 18, 19, 20]]))