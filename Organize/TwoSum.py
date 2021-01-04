

'''
single pass solution
Time: O(N)
Space: O(N)
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        for i in range(len(nums)):
            addend2 = target - nums[i]
            if addend2 in numMap:
                # we found our answer
                return [i, numMap[addend2]]
            else:
                # add addend2 to table
                numMap[addend2] = i
            