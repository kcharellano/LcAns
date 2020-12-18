'''
    DP solution
    Time: O(N^2), N is the length of nums
    Space: O(N^2)
'''
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:        
        n = len(nums)
        count = 0
        # create table
        table = [[0 for j in range(n)] for i in range(n)]
        
        # initialize first row
        for i in range(n):
            table[0][i] = nums[i]
            if nums[i] == k:
                count += 1
        
        # fill table
        for row in range(1, n):
            for col in range(n-row):
                table[row][col] = table[row-1][col] + nums[row+col]
                if table[row][col] == k:
                    count += 1
        return count
