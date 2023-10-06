


#
# Complete the 'pairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

import datetime

def pairs(k, arr):
    # Write your code here
    # combinations = []    
    # for i in range(len(arr)):
    #     for v2 in arr[i+1:]:
    #         if abs(arr[i] - v2) == k:
    #             combinations.append([arr[i],v2])
    combinations = []
    arr.sort()
    
    for i in range(len(arr)-k):
        if abs(arr[i] - arr[i+k]):
            combinations.append([arr[i], arr[i+k]])
    # print(combinations)
    return len(combinations)

arr = [x for x in range(0,100000)]; k = 3
# arr = [1,0,9,6,4,2,3];  k= 3
arr = [1,3,5,8,6,4,2]; k = 2

start = datetime.datetime.now()
print(pairs(k, arr))
end = datetime.datetime.now()
diff = end -  datetime.timedelta(seconds=start.second, microseconds=start.microsecond)
print(start, end, 'Duration: '+f"{diff.second}.{diff.microsecond}")

# Input (stdin)|

#     5 2

#     1 5 3 4 2

# Your Output (stdout)

#     3

# Expected Output

#     3




# Input (stdin)|

#     10 1

#     363374326 364147530 61825163 1073065718 1281246024 1399469912 428047635 491595254 879792181 1069262793

# Your Output (stdout)

#     0

# Expected Output

#     0




# Input (stdin)
# |

#     7 2

#     1 3 5 8 6 4 2

# Your Output (stdout)

#     5

# Expected Output

#     5