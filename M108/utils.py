# def print_matrix(arr_2d):
#     for arr in arr_2d:
#         for el in arr:
#             print()
#
#     return arr_2d_rez


# def print_matrix(arr_2d):
#     arr_2d_rez = []
#     i = 0
#     j = 0
#     for arr in arr_2d:
#         for el in arr:
#             arr_2d_rez
#             j = j + 1
#         i = i + 1
#     return arr_2d_rez
arr_2d = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]


def print_matrix(arr_2d):
    for j in range(3):
        for i in range(3):
            print(arr_2d[i][j], end=" ")
        print()
    return arr_2d


print_matrix(arr_2d)
