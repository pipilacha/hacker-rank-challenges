#!/bin/python3

import os

#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix):
    # Write your code here
    n = len(matrix) 
    
    summ = 0

    # n = 4
    # 119  114  42   112
    # 56   125  101  49
    # 15   78   56   43
    # 62   98   83   108

    
    for i in range(n // 2):
        for j in range(n // 2):
            summ += max(matrix[i][j], matrix[i][n-j-1], matrix[n-i-1][j], matrix[n-i-1][n-j-1])
            # max will be 119, 
            
    return summ

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()


# Sample Input

# STDIN           Function
# -----           --------
# 1               q = 1
# 2               n = 2
# 112 42 83 119   matrix = [[112, 42, 83, 119], [56, 125, 56, 49], \
# 56 125 56 49              [15, 78, 101, 43], [62, 98, 114, 108]]
# 15 78 101 43
# 62 98 114 108

# Sample Output

# 414


# input (stdin)

#     1

#     2

#     107 54 128 15

#     12 75 110 138

#     100 96 34 85

#     75 15 28 112

# Expected Output

#     488