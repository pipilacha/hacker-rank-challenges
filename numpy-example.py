import numpy

# my_array = numpy.array([ [1, 2], [3, 4] ])

# print("mean")
# print( numpy.mean(my_array, axis = 0)  )      #Output : [ 2.  3.]
# print( numpy.mean(my_array, axis = 1)  )     #Output : [ 1.5  3.5]
# print( numpy.mean(my_array, axis = None) )    #Output : 2.5
# print( numpy.mean(my_array)               )   #Output : 2.5


# print("\nvariance")
# print( numpy.var(my_array, axis = 0)  )      #Output : [ 2.  3.]
# print( numpy.var(my_array, axis = 1)  )     #Output : [ 1.5  3.5]
# print( numpy.var(my_array, axis = None) )    #Output : 2.5
# print( numpy.var(my_array)               )   #Output : 2.5


# print("\narimethic standard variation - std")
# print( numpy.std(my_array, axis = 0)  )      #Output : [ 2.  3.]
# print( numpy.std(my_array, axis = 1)  )     #Output : [ 1.5  3.5]
# print( numpy.std(my_array, axis = None) )    #Output : 2.5
# print( numpy.std(my_array)               )   #Output : 2.5


# N,M = list(map(int, input().split()))

# # _2D_array = []
# # for _ in range(N):
# #     _2D_array.append(list(map(int, input().split())))

# _2D_array = numpy.array([input().split() for _ in range(N)], int)
    
# # mean along axis 1
# print(numpy.mean(_2D_array, axis=1))

# # variance along axis 0
# print(numpy.var(_2D_array, axis=0))

# # standarsd deviation along axis None
# print(round(numpy.std(_2D_array), 11))









# A = numpy.array([ 1, 2 ])
# B = numpy.array([ 3, 4 ])
# print(f"dot product of {A} and {B}") # dot product is also the inner product
# print(numpy.dot(A,B))
# print(f"cross product of {A} and {B}")
# print(numpy.cross(A,B))

# Task
# You are given two arrays
# and . Both have dimensions of X.
# Your task is to compute their matrix product.

# Sample Input
# 2
# 1 2
# 3 4
# 1 2
# 3 4

# Sample Output
# [[ 7 10]
#  [15 22]]


# import numpy

# N = int(input())
# A = numpy.array([input().split() for _ in range(N)], int)
# B = numpy.array([input().split() for _ in range(N)], int)

# print(numpy.matmul(A,B))
# numpy.matmul(A,B)









A = numpy.array([0, 1])
B = numpy.array([3, 4])
print(f"inner prodcut of arrays {A} and {B}") # or dot product
print(numpy.inner(A, B))    #Output : 4
print(f"outer prodcut of arrays {A} and {B}") # or tensor product
print(numpy.outer(A, B))    #Output : [[0 0]
                            #          [3 4]]

import numpy


A = numpy.array(input().split(), int)
B = numpy.array(input().split(), int)

print(numpy.inner(A,B))
print(numpy.outer(A,B))

