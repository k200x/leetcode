#coding:utf-8

a = [[1, 2, 0, 3, 4],
     [2, 3, 4, 5, 1],
     [1, 1, 5, 3, 0]]

print(a[1][2])

def get_max_22Matrix(M, row, col):
    maxsum = 0
    result_i = result_j = 0

    for i in range(0, len(M) - 1):
        for j in range(0, len(M[0]) - 1):
            tmp_sum = M[i][j] + M[i+1][j] + M[i][j+1] + M[i+1][j+1]
            if maxsum < tmp_sum:
                maxsum = tmp_sum
                result_i = i
                result_j = j

    result_matrix = [[0] * 2 for i in range(2)]
    result_matrix[0][0] = M[result_i][result_j]
    result_matrix[1][0] = M[result_i + 1][result_j]
    result_matrix[0][1] = M[result_i][result_j + 1]
    result_matrix[1][1] = M[result_i + 1][result_j + 1]

    print(result_matrix)

get_max_22Matrix(a, 3, 5)








