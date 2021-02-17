
'''
    Algorithm: 01 Knapsack
    - The solution is the same as house robber one except with one modification
    - If our houses are [a, b, c, d]
    then we run our algorithm on [a,b,c] and [b,c,d]. Since if 
    our robber robs house A then they cannot rob house D and vice versa. 
    Then we take the max of the two scenarious.
    Time: O(N)
    Space: O(N)
'''

class Solution:
    def solve(self, nums, numLen):
        dp = [0] * numLen
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for idx in range(2, numLen):
            dp[idx] = max(nums[idx] + dp[idx-2], dp[idx-1])
        return dp[-1]
            
    def rob(self, nums: List[int]) -> int:
        numLen = len(nums)
        if numLen < 3:
            return max(nums)
        a = self.solve(nums[1:], numLen-1)
        b = self.solve(nums[:-1], numLen-1)
        return max(a,b)