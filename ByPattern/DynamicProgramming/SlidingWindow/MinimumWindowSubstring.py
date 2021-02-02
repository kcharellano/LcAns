#https://leetcode.com/problems/minimum-window-substring

'''
    Algorithm: Sliding Window -- dynamic variation
        - Keep a set of the original target characters
        - keep a set of remaining characters needed to make window valid
        - Store target letter counts inside the window using a dict
        - expand window inside outer string until remaining characters is empty
            - then shrink window until remaining characters is not empty
    Time: O(max(len(s), len(t)))
    Space: O(max(len(s), len(t)))
'''

from math import inf
from collections import defaultdict

class Solution:
    '''
    adds letter to window and adds letter to remaining
    if letter count > 0
    '''
    def addLetter(self, window, letter, remaining):
        window[letter] += 1
        if window[letter] > 0 and not letter in remaining:
            remaining.add(letter)
    
    '''
    removes letter from window and removes letter from remaining
    if lettercount <= 0
    '''
    def removeLetter(self, window, letter, remaining):
        window[letter] -= 1
        if window[letter] <= 0 and letter in remaining:
            remaining.remove(letter)
    
    def minWindow(self, s: str, t: str) -> str:
        # letters in s
        targetChars = set(t)
        # remaining letters needed to make window valid
        remaining = set(t)
        # important target character count in the current window
        window = defaultdict(int)
        for l in t:
            window[l] += 1
        
        start = 0
        end = 0
        left = 0
        minLength = inf
        for i in range(len(s)):
            if s[i] in targetChars:
                self.removeLetter(window, s[i], remaining)
            while not remaining:
                # update answer range
                if (i - left) < minLength:
                    minLength = min(minLength, i - start)
                    end = i + 1
                    start = left
                # add letter to window 
                if s[left] in targetChars:
                    self.addLetter(window, s[left], remaining)
                left += 1
                
        return s[start:end] if minLength != inf else ""
            
                
        