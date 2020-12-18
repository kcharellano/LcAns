'''
    Left and right product list approach.
    Time: O(N)
    Space: O(N)
'''
from collections import deque
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numsLength = len(nums)
        # construct left product array
        leftArr = [1]
        for i in range(1, numsLength):
            leftArr.append(nums[i-1] * leftArr[i-1])
        
        # construct right product array
        rightArr = deque([1])
        for i in range(1, numsLength):
            rightArr.appendleft(rightArr[-i] * nums[-i])

        # fill array output
        return [leftArr[i] * rightArr[i] for i in range(numsLength)]
