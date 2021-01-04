'''
    Convert letter to number with base-26
    Time: O(N)
    Space: O(1)
'''

from string import ascii_uppercase

class Solution:
    def titleToNumber(self, s: str) -> int:
        # Create mapping of letter to value
        letterMap = {}
        for val, letter in enumerate(ascii_uppercase, 1):
            letterMap[letter] = val
        # calculate value
        rsum = 0
        power = 0
        for letter in reversed(s):
            rsum += letterMap[letter] * (26 ** power)
            power += 1
        return rsum