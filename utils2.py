from data2 import arr_2d


def print_matrix(self):
    for j in range(3):
        for i in range(3):
            print(arr_2d[i][j], end=" ")
        print()
    return arr_2d


print_matrix(arr_2d)
