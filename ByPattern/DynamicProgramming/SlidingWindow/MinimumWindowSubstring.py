#https://leetcode.com/problems/minimum-window-substring

'''
    Algorithm: Sliding Window -- dynamic variation
        - Keep a set of the original target characters (tchars)
        - keep a set of remaining characters needed to make window valid(missing)
        - Store target letter counts inside the window using a dict
        - expand window until it contains all characters in t
        - shrink window while it contains all charactesrs in t
    Time: O(max(len(s), len(t)))
    Space: O(max(len(s), len(t)))
'''

from collections import defaultdict
from math import inf
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # constant used to process only important chars
        tchars = set(t)
        # contains letters that the window is missing
        missing = set(t)
        # maintains missing t-letter counts inside window
        # -- a negative value means we have more than necessary
        # -- a positive value means the window is missing x many letters
        # -- a zero count means just enough letters
        window = defaultdict(int)
        left = 0
        start, end = 0, inf
        for letter in t:
            window[letter] += 1
        # only process letters in tchars
        for i, letter in enumerate(s):
            # if letter is a tchar then update window
            if letter in tchars:
                window[letter] -= 1
                if window[letter] == 0:
                    missing.remove(letter)
            while not missing:
                # update min sub range
                if i - left < end - start:
                    end, start = i, left
                # if left points to a tchar then update window
                if s[left] in tchars:
                    window[s[left]] += 1
                    if window[s[left]] > 0:
                        missing.add(s[left])
                left += 1
        return s[start:end+1] if end != inf else ""