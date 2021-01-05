'''
    DP solution
    Time: O(n^2)
    Space: O(len(nums))
'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # create dp table
        length = len(nums)
        dp = [1] * (length)
        end = 0
        globalMax = 1
        while end < length:
            for i in range(0, end):
                if nums[i] < nums[end]:
                    dp[end] = max(dp[end], dp[i]+1)
            globalMax = max(globalMax, dp[end])
            end += 1
        return globalMax
            