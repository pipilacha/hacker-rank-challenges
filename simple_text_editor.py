Q = int(input("Enter the number of operations: "))
# Q = int(input())

S = ''
states_stack = []
for _ in range(Q):
    operation = input("Enter the operation and value: ").split()
    # operation = input().split()
    # print(operation)
    
    if operation[0] == '1':  # append substring to the end of the string
        states_stack.append(S)
        S += operation[1]
        
    elif operation[0] == '2':  # delete the last k chars off the string
        states_stack.append(S)
        S = S[:-int(operation[1])]
        
    elif operation[0] == '3':  # print the Kth char of the string
        print(S[int(operation[1])-1])
        
    elif operation[0] == '4':  # Undo the last (not previously undone) operation of type 1 or 2, reverting the state it was in prior to that operation.
        S = states_stack.pop()

list.re
# Input (stdin)

#     8

#     1 abc

#     3 3

#     2 3

#     1 xy

#     3 2

#     4

#     4

#     3 1

# Expected Output

#     c

#     y

#     a





# Input (stdin)

#     10

#     1 ewcgpjfh

#     1 igqsbqyp

#     1 qsdliigcj

#     4

#     3 15

#     1 iilmgp

#     2 8

#     4

#     2 18

#     1 scwhors

# Expected Output

#     y