import operator

def person_lister(f):
    def inner(people):
        #Sort the list in ascending order and return None.
        # The sort is in-place (i.e. the list itself is modified) and stable (i.e. the order of two equal elements is maintained).
        # If a key function is given, apply it once to each list item and sort them, ascending or descending, according to their function values.
        # The reverse flag can be set to sort in descending order.

        get_age = operator.itemgetter(2) # sort the list by the second field using itemgetter from the operator module:
        people.sort(key=lambda x: int(get_age())) 

        people.sort(key=lambda x: int(x[2])) 
        print(people)
        return [f(person) for person in people]
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')

