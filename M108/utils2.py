from M108.data2 import arr_2d2


def print_matrix(s):
    for j in range(3):
        for i in range(3):
            print(arr_2d2[i][j], end=" ")
        print()
    return arr_2d2


print_matrix([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
