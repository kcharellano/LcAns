'''
    https://leetcode.com/problems/longest-substring-without-repeating-characters/
'''

'''
    Algorithm:
        - Starting at each index, expand right until repeated character is found
        - Reset subStrSet and count for every iteration
        - Optimization: Using a set to check if a letter is already in substring --> O(1)
    Time: O(N^2)
    Space: O(N)
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        maxSubStr = 0
        for start in range(length):
            count = 0
            subStrSet = set()
            for cursor in range(start, length):
                if s[cursor] in subStrSet:
                    break
                else:
                    count += 1   
                    subStrSet.add(s[cursor])
            maxSubStr = max(count, maxSubStr)
        return maxSubStr

'''
    Algorithm:
        - expand right until repeated character is found
        - When repeated character is found pop first character from substring and continue step 1
    Time: O(N)
    Space: O(N)
'''
from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        length = len(s)
        count = 0
        maxSubStr = 1
        subStr = deque()
        leftOff = 0
        subStrSet = set()
        while leftOff < length-1:
            for cursor in range(leftOff, length):
                if s[cursor] in subStrSet:
                    leftOff = cursor
                    break
                else:
                    count += 1
                    subStr.append(s[cursor])
                    subStrSet.add(s[cursor])
            maxSubStr = max(count, maxSubStr)
            
            count -= 1
            letter = subStr.popleft()
            subStrSet.remove(letter)
        return maxSubStr
