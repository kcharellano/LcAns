'''
    https://leetcode.com/problems/letter-combinations-of-a-phone-number/
'''
'''
    Algorithm: Backtracking
        - Create a mapping of digits to their letters on phone keys
        - Perform basic backtracking
    Time: unkown but either O(N * 4^N) or O(3^N * 4^M)
    Space: unkown but either O(N * 4^N) or O(3^N * 4^M) bc it stores that many solutions
'''
class Solution:
    def explore(self, digits, digitMap, rcomb, comb):
        if digits == "":
            comb.append("".join(rcomb))
            return
        
        for letter in digitMap[digits[0]]:
            # choose a letter
            rcomb.append(letter)
            # call subroutine
            self.explore(digits[1:], digitMap, rcomb, comb)
            # backtrack
            rcomb.pop()
    
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        
        comb = []
        # create digit to letter maps
        digitMap = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']            
        }
        self.explore(digits, digitMap, [], comb)
        return comb