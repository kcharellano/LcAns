# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/submissions/


'''
    Algorithm: HashMap to check for letter differences
    - create letter counts for string s and string t
    - remove letters they have in common
    - remaining size of either(they will be the same) is the answer
    Time: O(len(s))
    Space: O(len(s))
'''
from collections import defaultdict
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        tMap, sMap = defaultdict(int), defaultdict(int)
        # lettercount for s and t
        for letter in s:
            sMap[letter] += 1
        for letter in t:
            tMap[letter] += 1
        # count difference
        diffCount = 0
        for key, val in tMap.items():
            diff = val - sMap[key]
            if diff > 0:
                diffCount += diff
        return diffCount
