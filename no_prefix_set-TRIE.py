#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'noPrefix' function below.
#
# The function accepts STRING_ARRAY words as parameter.
#

def noPrefix(words):
    # Write your code here
    class TrieNode:
        def __init__(self, data=None):
            self.children = [None for _ in range(26)] # initialize all in none, a-z
            self.word_count = 0 # to check if a word ends a that node
            self.data = data # to store the char in that node
            
    class Trie:
        def __init__(self):
            self.root = TrieNode() # create a root node which data is null
            
        def insert(self, word):
            '''
            Insert a word in to the trie
            '''
            current_node = self.root 
            for c in word:
                if current_node.children[ord(c)-ord('a')] is None: # if children[char] is None we create it and move to the new node
                    new_node = TrieNode(c)
                    current_node.children[ord(c)-ord('a')] = new_node
                current_node = current_node.children[ord(c)-ord('a')]
            current_node.word_count += 1
            
        def search_prefix(self, word):
            '''
            Return True if a match is found else False
            '''
            current_node = self.root
            for c in word:
                if current_node.word_count > 0:
                    # if there is that ends at that node that means there is a prefix for this word in the trie
                    return True
                if current_node.children[ord(c)-ord('a')] is None: # if any of the children is none it means it not in the trie
                    return False
                current_node = current_node.children[ord(c)-ord('a')]
            return True # true if it matched the word
    
    trie = Trie()
    for word in words:
        if trie.search_prefix(word):
            print('BAD SET')
            print(word)
            break
        trie.insert(word)
    else:
        print('GOOD SET')
                
                    
                    
        

if __name__ == '__main__':
    n = int(input().strip())

    words = []

    for _ in range(n):
        words_item = input()
        words.append(words_item)

    noPrefix(words)


# nput (stdin)

#     7

#     aab

#     defgab

#     abcde

#     aabcde

#     cedaaa

#     bbbbbbbbbb

#     jabjjjad

# Your Output (stdout)

#     BAD SET

#     aabcde

# Expected Output

#     BAD SET

#     aabcde





# Input (stdin)

#     4

#     aab

#     aac

#     aacghgh

#     aabghgh

# Your Output (stdout)

#     BAD SET

#     aacghgh

# Expected Output

#     BAD SET

#     aacghgh