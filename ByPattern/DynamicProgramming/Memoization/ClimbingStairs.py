# https://leetcode.com/problems/climbing-stairs
'''
    Algorithm: Memo Distinct Ways
    - This problem is equivalent to the fibonacci sequence
    - 
'''
class Solution:
    def fib(self, cache, n):
        if n in cache:
            return cache[n]
        cache[n] = self.fib(cache, n-1) + self.fib(cache, n-2)
        return cache[n]
        
    def climbStairs(self, n: int) -> int:
        return self.fib({1: 1, 2: 2}, n)