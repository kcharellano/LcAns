'''
    https://leetcode.com/problems/reverse-integer
'''
'''
    Algorithm: pop/push
        - pop the rightmost integer off number
        - add it as a reverse number
        - check bounds
'''
class Solution:
    def reverse(self, x: int) -> int:
        posMax = 2**31 - 1
        negMax = -(2**31)
        reverse = 0
        negFlag = -1 if x < 0 else 1
        while x != 0:
            # get rightmost integer on x
            pop = (negFlag*x) % 10
            
            # delete rightmost integer on x
            x = int(x / 10)
            
            # store reverse number on a temp and check bounds
            temp = reverse * 10 + (negFlag*pop)
            if temp > posMax or temp < negMax:
                return 0
            # if reverse number doesn't violate bounds continue
            reverse = temp
        return reverse
