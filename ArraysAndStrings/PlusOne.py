'''
    Algorithm: Elementary math
    Time: O(N)
    Space: O(1)
'''
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits)
        flag = False
        for i in range(1, length+1):
            if digits[-i] > 8 and i == length:
                flag = True
                digits[-i] = 0
            elif digits[-i] > 8:
                digits[-i] = 0
            else:
                digits[-i] += 1
                break
        # edgecase
        if flag:
            digits.insert(0, 1)
        return digits