
#
# Complete the 'pairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

import datetime

from random import randint
import itertools

def pairs(k, arr):
    # Write your code here
    combinations = []
    
    # for i in range(len(arr)):
    #     for v in arr[i+1:]:
    #         if abs(arr[i] - v) == k:
    #             combinations.append([arr[i], v])

    # for combination in itertools.combinations(arr,2):
    #     if abs(combination[0] - combination[1]) == k:
    #         combinations.append(combination[0] - combination[1])

    # for item in arr:
    #     pairs_ = list(filter(lambda x: abs(x - item) == k, arr))
    #     for pair in pairs_:
    #         pair_ = sorted([item, pair])
    #         if pair_ not in combinations:
    #             combinations.append(pair_)

    map_= {item:True for item in arr} # map all distinct numbers into a dict

    for number in arr:
        # look for each number + k and number - k and add to combinations if it exists in map, then delete number from map
        # we can delete number because [number, number2] == [number2, number]
        # for example 16: 
        #   16 + 13 = 29 which is in map, [16,29] is added,. later in the for when number=29, 29-13=16 which is not in the map, [29,16] is not added
        #   same as 16 - 13 = 3 is in map, [16,3] is added, later number=3, 3+13=16 not in map, [3,16] is not added
        if number + k in map_:
            combinations.append([number, number + k])
        if number - k in map_:
            combinations.append([number, number - k])
        del map_[number]

    print(combinations)
                
    return len(combinations)

arr = [16, 10, 29, 3, 23]; k = 13 
# arr = [1,0,9,6,4,2,3];  k= 3
# arr = [1,3,5,8,6,4,2]; k = 2

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