# https://leetcode.com/problems/longest-substring-without-repeating-characters/

'''
    Algorithm: Sliding Window
    - Expand window until substring is no longer unique
    - if window contains repeated characters shift it right
    - Note: We don't need to shrink window becase a smaller size window will
    never be the answer.
    Time: O(N)
    Space: O(N)
'''
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = defaultdict(int)
        unique, left = 0, 0
        longest = 0
        for i, letter in enumerate(s):
            # update distinct letter count
            if window[letter] == 0:
                unique += 1
            # add letter to window
            window[letter] += 1
            # check for repeated letters
            if (i - left + 1) - unique > 0:
                # shift window
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    unique -= 1
                left += 1
            longest = max(longest, i-left+1)
        return longest
