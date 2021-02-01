
'''
    Algorithm: Memoization
    - Look at DP version explanation
    Time: O(N)
    Space: 
'''
class Solution:
    def solve(self, cache, nums, i):
        if i < 0:
            return 0
        if i in cache:
            return cache[i]
        else:
            cache[i] = max(self.solve(cache, nums, i-1), nums[i] + self.solve(cache, nums, i-2))
        return cache[i]
        
    def rob(self, nums: List[int]) -> int:
        return self.solve({}, nums, len(nums)-1)