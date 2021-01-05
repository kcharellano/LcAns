'''
    "Horziontal Scanning" -- Compare words and keep track of longest common prefix
    Time: O(S), S is the sum of all characters in all strings
    Space: O(L), L is the length of the longest word
'''
class Solution:
    # return the longest common prefix between two strings
    def _helper(self, s1, s2) -> str:
        lcp = []
        for i in range(min(len(s1), len(s2))):
            if s1[i] == s2[i]:
                lcp.append(s1[i])
            else:
                break
        return "".join(lcp)

    def longestCommonPrefix(self, strs: List[str]) -> str:
        # if strs is empty then no possible common prefix
        if strs == []:
            return ""
        
        # else iteratively compare each word
        lcp = strs[0]
        for i in range(1, len(strs)):
            lcp = self._helper(lcp, strs[i])
        return lcp;
"""
    "Vertical Scanning" -- compare letters of words by column
    Time: O(S), S is the sum of all characters in all strings
    Space: O(L), L is the length of the longest word
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # if strs is empty then no possible common prefix
        if strs == []:
            return ""
        
        # else vertical scan
        lcp = []
        # iterate through columns in range of the length of the smallest
        # word in the list to avoid index out of bounds errors
        for col in range(len(min(strs, key=len))):
            # append letter from first word from col
            lcp.append(strs[0][col])
            for wordIndex in range(1, len(strs)):
                # if any other word in the list doesn't match current lcp col
                # then pop it off and return lcp
                if lcp[col] != strs[wordIndex][col]:
                    lcp.pop()
                    return "".join(lcp)
        # if able to get through all letters then return lcp as string
        return "".join(lcp)

