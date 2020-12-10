'''
Greedy approach
Time: O(N)
Space: O(1)
'''
from math import inf
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        rsum = nums[0]
        maxSum = nums[0]
        for i in range(1, len(nums)):
            rsum = max(nums[i], rsum + nums[i])
            maxSum = max(rsum, maxSum)
        return maxSum