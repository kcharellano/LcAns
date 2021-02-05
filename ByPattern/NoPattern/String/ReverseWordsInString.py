# https://leetcode.com/problems/reverse-words-in-a-string

'''
    Algorithm: In place reverse
    - split string
    - swap words in place
    Time: O(N)
    Space: O(1)
'''
from collections import deque
class Solution:
    def reverseWords(self, s: str) -> str:
        ls = s.split()
        left, right = 0, len(ls) - 1
        while left < right:
            ls[left], ls[right] = ls[right], ls[left]
            left += 1
            right -= 1
        return " ".join(ls)

'''
    Algorithm: reverse words
    - split string
    - iterate over words and append them at head to mimic reverse
    Time: O(N)
    Sapce: O(N)
'''
from collections import deque
class Solution:
    def reverseWords(self, s: str) -> str:
        ls = s.split()
        left, right = 0, len(ls) - 1
        while left < right:
            ls[left], ls[right] = ls[right], ls[left]
            left += 1
            right -= 1
        return " ".join(ls)
        