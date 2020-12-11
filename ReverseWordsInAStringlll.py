'''
    Split string into words and reverse every word individually
    Time: O(N)
    Space: O(W)
'''
class Solution:
    # reverse a single word and return as a string
    def reverseWord(self, w: str) -> str:
        ls = list(w)
        left = 0
        right = len(w) - 1
        while left < right:
            # swap left with right
            ls[left], ls[right] = ls[right], ls[left]
            # incr/decr index cursors
            left += 1
            right -= 1
        return "".join(ls)

    def reverseWords(self, s: str) -> str:
        # split string based on spaces
        ans = s.split(' ')
        # loop through words and reverse them
        for i in range(len(ans)):
            ans[i] = self.reverseWord(ans[i])
        return " ".join(ans)
