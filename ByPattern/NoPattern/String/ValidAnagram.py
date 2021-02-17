# https://leetcode.com/problems/valid-anagram/submissions/
from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letterCount = defaultdict(int)
        for l in s:
            letterCount[l] += 1
        for l in t:
            letterCount[l] -= 1
        for v in letterCount.values():
            if v != 0:
                return False
        return True
