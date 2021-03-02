from collections import deque
'''
    Algorithm: Two Pointer Solution
'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sLen, tLen = len(s), len(t)
        sPtr, tPtr = 0, 0
        while sPtr < sLen and tPtr < tLen:
            if s[sPtr] == t[tPtr]:
                sPtr += 1
                tPtr += 1
            else:
                tPtr += 1
        return sPtr == sLen