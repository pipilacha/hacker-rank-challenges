#!/bin/python3

import re

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
    
string = ''

for column in range(m):
    for message in matrix:
        string += message[column:column+1]
        
print(re.sub(r"(?<=\w)([!@#$%& ]+)(?=\w)"," ", string))
# look behind is word,[!@#$%& ] repeats one or more times ,look ahead is word

# Sample Input 0

# 7 3
# Tsi
# h%x
# i #
# sM 
# $a 
# #t%
# ir!

# Sample Output 0

# This is Matrix#  %!


# input (stdin)

#     4 8

#     #%$r%r$n

#     I%Mi$iTi

#     tiaxsprt

#     #st%ctiy

# Expected Output

#     #It is Matrix script Trinity