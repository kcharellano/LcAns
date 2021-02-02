# https://leetcode.com/problems/maximum-subarray/submissions/

'''
    Algorithm: Dynamic Programming
    - rsum maintains the optimal subarray sum to a given point
        - at every step rsum makes a decides whether
        - to consider only the current index or consider the best possible rsum before that index + current index
    Time: O(N)
    Space: O(1)
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum, rsum = nums[0], nums[0]
        for i in range(1, len(nums)):
            rsum = max(nums[i], rsum + nums[i])
            maxSum = max(maxSum, rsum)
        return maxSum