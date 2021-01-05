'''
    Two pointers solution
    Time: O(N)
    Space: O(1)
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left = 0
        right = len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True