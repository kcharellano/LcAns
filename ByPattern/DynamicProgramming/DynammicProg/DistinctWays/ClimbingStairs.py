# https://leetcode.com/problems/climbing-stairs
'''
    Algorithm: DP Distinct Ways
    - This problem is equivalent to the fibonacci sequence
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {1: 1, 2: 2}
        if n <= 2:
            return cache[n]
        for i in range(3, n+1):
            cache[i] = cache[i-1] + cache[i-2]
        return cache[n]