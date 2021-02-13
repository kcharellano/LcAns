'''
    Algorithm: Dynamic Sliding Window
        - expand window right while rsum < target
        - once rsum becomes greater or equal to target begin shrinking in order
        to find minimal subrange
    Time: O(N)
    Space: O(1)
'''
from math import inf
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        rsum, left = 0, 0
        minSize = inf
        for i, num in enumerate(nums):
            rsum += num
            while rsum >= target:
                #(i-left+1) = size of window
                minSize = min(minSize, i-left+1) 
                rsum -= nums[left]
                left += 1
        return minSize if minSize != inf else 0
