
def bfs(n, m, edges: list, s):
    # Write your code here
    WEIGHT = 6

    distances_dict = {}
    distances_array = []

    edges.sort(key= lambda x: (x[0], x[1]))
    print(edges)
   
    for i,edge in enumerate(edges):
        if edge[0] == s:            
            distances_dict[edge[1]] = WEIGHT 
            distances_array.append(6)  
        else:
            distance_sum = distances_dict[edge[0]] + WEIGHT
            distances_dict[edge[1]] = distance_sum
            distances_array.append(distance_sum)
    
    for i in range(n):
        if i+1 not in distances_dict.keys() and i+1 != s:
            distances_array.insert(i, -1)
            distances_dict[i+1] = -1
    # return distances_array
    return distances_dict

print(bfs(5, 3, [[1,3], [1,2], [3,4]], 1))
print()
print(bfs(4, 3, [[1,3], [1,2]], 1))
print()
print(bfs(3, 2, [[2,3]], 2))

print()
print(bfs(8, 7, [[2,7], [2,4], [2,3], [3,6], [3,5], [7,1]], 2))
# 1     number of queries

# 4 2   n m n=number of nodes m=number of edges

# 1 2   edge between nodes u,v -> 1,2

# 1 3   edge between nodes u,v -> 1,3

# 1     starting node