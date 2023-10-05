a = [50, 50, 47, 47, 47, 46, 46, 46, 46, 45, 45, 45, 45, 45, 45, 44, 43, 43, 41, 40, 39, 38, 38, 37, 37, 35, 35, 34, 34]
b = [33, 33, 32, 32, 32, 32, 31, 31, 30, 29, 28, 28, 27, 27, 27, 26, 26, 25, 24, 24, 23, 23, 22, 22, 22, 22, 21, 20, 19, 17, 17, 17, 17, 16, 16, 16, 15, 15, 14, 13, 13, 13, 13, 12, 12, 11, 10, 10, 9, 9, 9, 8, 8, 7, 7, 6, 6, 5, 4, 4, 4, 4, 3, 3, 3, 2, 2, 1]

print(sum(a), sum(b))

a = [50, 50, 47, 47, 47, 46, 46, 46, 46, 45, 45, 45, 45, 45, 45, 44, 43, 43, 41, 40, 39, 38, 38, 37, 37, 35, 35, 34]
b = [34, 33, 33, 32, 32, 32, 32, 31, 31, 30, 29, 28, 28, 27, 27, 27, 26, 26, 25, 24, 24, 23, 23, 22, 22, 22, 22, 21, 20, 19, 17, 17, 17, 17, 16, 16, 16, 15, 15, 14, 13, 13, 13, 13, 12, 12, 11, 10, 10, 9, 9, 9, 8, 8, 7, 7, 6, 6, 5, 4, 4, 4, 4, 3, 3, 3, 2, 2, 1]

print(sum(a), sum(b))


# arr = a+b
# arr.sort(reverse=True)
    
#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'subsetA' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def subsetA(arr):
    arr.sort(reverse=True)
    
    sub_setsA = []
    sub_setsB = []
    
    for i in range(len(arr)):
        a = arr[:i+1]
        b = arr[i+1:]
        if sum(a) > sum(b) and len(b) > 0:
            if not any(item in b for item in a):
                sub_setsA.append(a)
                sub_setsB.append(b)
                
    print(sub_setsA[0], sub_setsB[0], sep="\n*")
    
    min_ = sub_setsA[0]
    for element in sub_setsA[1:]:
        # print("min", min_, len(min_))
        # print('element', element, len(element))
        if (sum(element) >= sum(min_)) and (len(element) < len(min_)):
            min_ = element
     
    return sorted(min_)

def subsetA(arr):
    arr.sort(reverse=True)
    
    A = None
    
    for i in range(len(arr)):
        a = arr[:i+1]
        b = arr[i+1:]
        #if sum(a) > sum(b) and len(b) > 0:
        if sum(a) > sum(b) and len(b) > 0:
            # if not any(item in b for item in a):  #if i check for intersections some test do not pass??
            #     if A is not None:
            #         if sum(a) > sum(a):
            #             A = a
            #         elif sum(a) == sum(A) and len(a) < len(A):
            #             A = a
            #     else:
            #         A = a
            # if A is not None:
            #     if sum(a) > sum(a):
            #         A = a
            #     elif sum(a) == sum(A) and len(a) < len(A):
            #         A = a
            # else:
            #     A = a
            A=a
            break
    
     
    return sorted(A)
        
    
    # 50, 50, 47, 47, 47, 46, 46, 46, 46, 45, 45, 45, 45, 45, 45, 44, 43, 43, 41, 40, 39, 38, 38, 37, 37, 35, 35, 34, 34
    # 50, 50, 47, 47, 47, 46, 46, 46, 46, 45, 45, 45, 45, 45, 45, 44, 43, 43, 41, 40, 39, 38, 38, 37, 37, 35, 35, 34, 34
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = subsetA(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


# Input (stdin)|
# 20
# 2
# 3
# 4
# 4
# 5
# 9
# 7
# 8
# 6
# 10
# 4
# 5
# 10
# 10
# 8
# 4
# 6
# 4
# 10
# 1


# Expected Output

#     8

#     8

#     9

#     10

#     10

#     10

#     10
