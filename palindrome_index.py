def palindromeIndex(s):
    # Write your code here
    print("\n"+s)
    index = -1
    for i in range(len(s)//2):
        if s[i] != s[-1-i]:
            print(s[:-1-i]+s[-1-i +1:])
            if s[:i]+s[i+1:] == (s[:i]+s[i+1:])[::-1]:
                index = i
            else: #if diff is at -1??
                if i > 0:
                    if s[:-1-i]+s[-1-i+1:] == (s[:-1-i]+s[-1-i+1:])[::-1]:
                        index = len(s) -1 -i
                else:
                    if s[:-1-i] == (s[:-1-i])[::-1]:
                        index = len(s) -1 -i
            break
    return index

# def palindromeIndex2(s):
#     for i in range(int(len(s)/2)):
#         if s[i]!=s[len(s)-1-i]:
#             print('them',i if ((s[:i]+s[i+1:])==(s[:i]+s[i+1:])[::-1]) else len(s)-1-i)
#             break
        



print('me',palindromeIndex('hgygsvlfcwnswtuhmyaljkqlqjjqlqkjlaymhutwsnwcwflvsgygh')) # expected 44
# palindromeIndex2('hgygsvlfcwnswtuhmyaljkqlqjjqlqkjlaymhutwsnwcwflvsgygh')
print(palindromeIndex('aaab'))
print(palindromeIndex('baa'))
print(palindromeIndex('aaa'))
# Input (stdin)
# |

#     3

#     aaab

#     baa

#     aaa

# Your Output (stdout)

#     3

#     0

#     -1

# Expected Output

#     3

#     0

#     -1