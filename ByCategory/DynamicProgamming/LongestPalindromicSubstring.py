
'''
    Algortitm: DP
        - use a dp table to determine if substrings are palindromic or not
        - if a palindrom is found on a new row then store it
    Time: O(N^2)
    Space: O(N^2)
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == "":
            return ""
        # create and initialize first row table
        sLen = len(s)
        dp = [[False for i in range(sLen)] for j in range(sLen)]        
        
        # initialize first row
        for i in range(sLen):
            dp[0][i] = True
        maxSubStr = s[0]
        
        # initialize second row
        for i in range(sLen - 1):
            if s[i] == s[i+1]:
                dp[1][i] = True
                maxSubStr = s[i:i+2]
        
        for row in range(2, sLen):
            foundFlag = False
            for col in range(sLen-row):
                # first check
                if s[col] == s[col+row]:
                    # second check
                    if dp[row-2][col+1] == True:
                        dp[row][col] = True
                        if not foundFlag:
                            maxSubStr = s[col:col+row+1]
                            foudFlag = True
                        continue
                
                # otherwise
                dp[row][col] = False
        
        return maxSubStr
