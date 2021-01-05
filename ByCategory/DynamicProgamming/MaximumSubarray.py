'''
    https://leetcode.com/problems/maximum-subarray/
'''

'''
    Algorithm:
        - rsum updates itself to be:
            - reset to the next element
            - itself plus the next element
        - maxSum keeps track of maximum rsum seen so far
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        rsum = nums[0]
        maxSum = nums[0]
        for i in range(1, len(nums)):
            rsum = max(nums[i], rsum + nums[i])
            maxSum = max(rsum, maxSum)
        return maxSum