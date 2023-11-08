import itertools

def check_if_valid(main: list, sub:list):

    permutations = itertools.permutations(sub)
    
    for comb in permutations:
        concat = [y for x in comb for y in x]
        print(comb, concat)
        if concat == main:
            return 'valid'

    return 'invalid'


main = [15,88,63]
print(check_if_valid(main,[[88],[63],[15]]))

print()
print(check_if_valid(main,[[88,63,15]]))

print()
print(check_if_valid(main,[[15,88,63]]))

print()
print(check_if_valid(main,[[88, 63],[15]]))