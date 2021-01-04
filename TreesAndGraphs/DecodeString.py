'''
    https://leetcode.com/problems/decode-string
'''

'''
    Algorithm: Decode string recursively
        - Use an outerloop to decode string while i < len
        - if a digit is found then decode the string inside brackets
    Time: O(maxK * n) -- k is a multiplier and n is the length of its respective string
    Space: unknown
'''


class Solution:
    # return number and index of the last digit
    def getNumber(self, s, startIdx):
        i = startIdx
        numBuilder = []
        while s[i].isdigit():
            numBuilder.append(s[i])
            i += 1
        return (int("".join(numBuilder)), i-1)
    
    # return substring and index of closing bracket
    def getSubstr(self, s, startIdx):
        i = startIdx + 1
        strBuilder = []
        while s[i] != ']':
            if s[i].isalpha():
                strBuilder.append(s[i])
                i += 1
            else:
                multx, didx = self.getNumber(s, i)
                substr, idx = self.getSubstr(s, didx+1)
                for i in range(multx):
                    strBuilder.append(substr)
                i = idx+1
        return ("".join(strBuilder), i)

    def decodeString(self, s: str) -> str:
        i = 0
        size = len(s)
        strBuilder = []
        # outer loop
        while i < size:
            if s[i].isalpha():
                strBuilder.append(s[i])
                i += 1
            else:
                multx, didx = self.getNumber(s, i)
                substr, idx = self.getSubstr(s, didx+1)
                for i in range(multx):
                    strBuilder.append(substr)
                i = idx+1
        return "".join(strBuilder)
