# https://leetcode.com/problems/longest-repeating-character-replacement/

'''
    Algorithm: Dynamic Sliding Window(no shrinking)
        - Keep track of max reapeated character count
        and window size(i - start + 1)
        - if the window size - max repeated character count is ever greater
        than k(the max number of letter differences) then right shift window
        - upates maxWindowLength after every iteration
    Time: O(N*W) -- W = size of window, N = size of S
    Space: O(W)
'''
class Solution:
    def addLetter(self, letter, hmap):
        if letter in hmap:
            hmap[letter] += 1
        else:
            hmap[letter] = 1
    
    def characterReplacement(self, s: str, k: int) -> int:
        window = {}
        maxRepeatedCount = 0
        start = 0
        size = len(s)
        maxWindowLength = 0
        for i in range(size):
            self.addLetter(s[i], window)
            maxRepeatedCount = max(maxRepeatedCount, max(window.values()))
            # if there are more than k differences in window
            # NOTE: i - start + 1 is the window length
            if (i - start + 1) - maxRepeatedCount > k:
                # shift window to the right
                window[s[start]] -= 1
                start += 1
            maxWindowLength = max(maxWindowLength, i - start + 1)
        return maxWindowLength