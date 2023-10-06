#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here
    def find_opposite(char):
        if char == '(':
            return ')'
        elif char == '{':
            return '}'
        elif char == '[':
            return ']'
    
    stack = []  # using array as stack
    # append to char to stack, if the next element is closing bracket pop stack. it is balanced if the stack is empty.
    
    for char in s:
        if len(stack) == 0: # first pass append first element
            stack.append(char)
        else:
            # print(char, stack[-1])
            if char == find_opposite(stack[-1]): # if char is the closing bracket of the head of the stack, pop stack
                stack.pop()
            else: # if no append to stack
                stack.append(char)
            
    return 'YES' if len(stack) == 0 else 'NO'



# Input (stdin)

#     3

#     {[()]}

#     {[(])}

#     {{[[(())]]}}

# Expected Output

#     YES

#     NO

#     YES



# Input (stdin)

#     2

#     {{([])}}

#     {{)[](}}

# Expected Output

#     YES

#     NO



# Input (stdin)

#     3

#     {(([])[])[]}

#     {(([])[])[]]}

#     {(([])[])[]}[]

# Expected Output

#     YES

#     NO

#     YES