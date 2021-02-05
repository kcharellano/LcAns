# https://leetcode.com/problems/longest-substring-without-repeating-character

'''
    Algorithm: Sliding Window
    - Expand window until substring is no longer unique
    - shrink window until substring becomes unique again
    Time: O(N)
    Space: O(N)
'''
from collections import defaultdict, deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lmap = defaultdict(int)
        window = deque()
        start = 0
        maxSize = 0
        for i in range(len(s)):
            letter = s[i]
            # add letter to window
            window.append(letter)
            lmap[letter] += 1
            # remove duplicates
            while lmap[letter] > 1:
                lmap[window.popleft()] -= 1
                start += 1
            maxSize = max(maxSize, i - start + 1)
        return maxSize
