'''
    Algorithm: Brute Force
    NOTE: Time limit exceeded
'''
from math import inf
class Solution:
    def explore(self, nums, m, split):
        if m == 1:
            split.append(nums)
            #print(split)
            maxSubarraySum = -inf
            for ls in split:
                rsum = 0
                for num in ls:
                    rsum += num
                maxSubarraySum = max(maxSubarraySum, rsum)
            self.gmin = min(self.gmin, maxSubarraySum)
            split.pop()
            return
        
        length = 1
        for i in range(len(nums)-m+1):
            # choose numbers
            split.append(nums[:length])
            
            # call subroutine
            self.explore(nums[length:], m-1, split)
            
            # backtrack
            split.pop()
            length += 1
            
    def splitArray(self, nums: List[int], m: int) -> int:
        self.gmin = inf
        self.explore(nums, m, [])
        return self.gmin
