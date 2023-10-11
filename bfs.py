
def bfs(n, m, edges: list, s):
    # Write your code here
    def uniques(lst):
        lasts = []
        for item in lst:
            if item in lasts or item[::-1] in lasts:
                continue
            yield item
            lasts.append(item)            

    WEIGHT = 6

    edges = list(uniques(edges))

    distances_dict = {}

    start = [s]
    traveled = [s]
    while len(start) > 0:
        next_start = []
        for s_ in start:
            for x in sorted(list(filter(lambda x: s_ in x, edges))):
                node = x[0] if x[0] != s_ else x[1]
                if node in traveled:
                    continue
                else:
                    if s_ == s:
                        distances_dict[node] = WEIGHT
                    else:
                        distances_dict[node] = distances_dict[s_] + WEIGHT
                    next_start.append(node)
                    traveled.append(node)
        start = next_start

    distances_array = []
    
    for i in range(n):
        if i+1 == s:
            continue
        value = distances_dict[i+1] if i+1 in distances_dict.keys() else -1 
        distances_array.insert(i, value)
    
    print(distances_dict)
    return distances_array            

print(bfs(5, 3, [[1,3], [1,2], [3,4]], 1))
print()
print(bfs(4, 3, [[1,3], [1,2]], 1))
# print()
# print(bfs(3, 2, [[2,3]], 2))

# print()
# print(bfs(8, 7, [[2,7], [2,4], [2,3], [3,6], [3,5], [7,1]], 2))
# 1     number of queries

# 4 2   n m n=number of nodes m=number of edges

# 1 2   edge between nodes u,v -> 1,2

# 1 3   edge between nodes u,v -> 1,3

# 1     starting node



# 10 6 [[3, 1], [10, 1], [10, 1], [3, 1], [1, 8], [5, 2]] 3
print()
print(bfs(10, 6, [[3, 1], [10, 1], [10, 1], [3, 1], [1, 8], [5, 2], [1,3]], 3))