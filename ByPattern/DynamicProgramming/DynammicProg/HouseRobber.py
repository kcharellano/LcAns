# https://leetcode.com/problems/house-robber/solution/

'''
    Algorithm: Look at comments
    Time: O(N) -- N = len(nums)
    Space: O(N)
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        numLen = len(nums)
        # edgecase: numsLen = 0, 1 or 2
        if numLen < 3:
            return max(nums) if numLen != 0 else 0
        dp = [0] * numLen
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, numLen):
            '''
            at house i, we could rob it or not rub it
            if we rob house i (current house), we know that
            our previously robbed house would be i - 2 since
            we can not rob adjacient house
            if we do not rob house i (current house), we know that
            our previously robbed house would be i - 1 since the same 
            reason above
        
            so the current accumulated sum at house i will be the max 
            of the two cases described above except if we rob, make sure
            we add the money in current house first before comparing
            so,
            if rob, the money will become: dp[i-2] + nums[i]
            if not rob, the money will besome: dp[i-1]
            dp[i]: robbed so far
            '''
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        return dp[numLen-1]
            