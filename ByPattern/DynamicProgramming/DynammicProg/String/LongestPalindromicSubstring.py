# https://leetcode.com/problems/longest-palindromic-substring
'''
    Algorithm: 2D DP
    - Form a 2D array where dp[i,j] == true if substring from i to j is a palindrome
    - A subtring from k to l is a palindrome if dp[k+1, l-1] == true and s[k] == s[l]
    Time: O(N^2)
    Space: O(N^2)
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        dp = [[1 for i in range(size)] for j in range(size)]
        maxSize = 1
        left, right = 0, 0
        for row in range(1, size):
            for col in range(size-row):
                start, end = col, col+row
                if s[start] == s[end]:
                    if end - start == 1:
                        dp[row][col] = 2
                    else:
                        dp[row][col] = 2 + dp[row-1][col+1]
                else:
                    dp[row][col] = max(dp[row-1][col], dp[row-1][col+1])
                # update max
                if dp[row][col] > maxSize:
                    maxSize = dp[row][col]
                    left, right = start, end
        return s[left:right+1]
