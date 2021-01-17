# https://leetcode.com/problems/subarray-sum-equals-k
'''
    Algorithm: come back later
    NOTE: Remember to add this pattern
'''
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, rsum = 0, 0
        cache = defaultdict(int)
        cache[0] = 1
        for i in range(len(nums)):
            rsum += nums[i]
            if rsum - k in cache:
                count += cache[rsum-k]
            cache[rsum] += 1 #unsure why this needs to be here
        return count
        