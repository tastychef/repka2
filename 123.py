arr_2d = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
def print_matrix(arr_2d):
    for arr in arr_2d:
          print(arr)
print_matrix(arr_2d)

def print_matrix(arr_2d):
    for arr in arr_2d:
        for el in arr:
            print(el, end = ' ')
        print()
print_matrix(arr_2d)




# def print_matrix (arr_2d):
#     for i in range (len(arr_2d)):
#         for j in range(len(arr_2d[i])):
#             print(arr_2d[i][j]), eng = ''
#         print()
