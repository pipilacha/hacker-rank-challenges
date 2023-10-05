# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

K,M = iter(map(int, input().split()))

sqr = lambda x: x**2
S = lambda X: sum([sqr(x) for x in X])%M

# lists = {k:max([v for v in list(map(int, input().split()))]) for k in range(K) }
#lists = [max([v for v in list(map(int, input().split()))]) for k in range(K)]

lists =[[v for v in list(map(int, input().split()[1:]))] for k in range(K) ] 

# maxx_S = 0
# for comb in product(*lists):
#     result = S(comb)
#     maxx_S = result if result > maxx_S else maxx_S
# print(maxx_S)  

# first we find which combination gives the max result >max(product(*lists), key=S)<
# then we apply the formula to that result >S(max result)<
print(S(max(product(*lists), key=S)))

# # Sample input
# 6 767
# 2 488512261 423332742
# 2 625040505 443232774
# 1 4553600
# 4 92134264 617699202 124100179 337650738
# 2 778493847 932097163
# 5 489894997 496724555 693361712 935903331 518538304
# # Sample output
# 766