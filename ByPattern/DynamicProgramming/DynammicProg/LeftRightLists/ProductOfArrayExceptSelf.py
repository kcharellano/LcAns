# https://leetcode.com/problems/product-of-array-except-self

'''
    Algorithm: leftArr and rightArr
    - Create a left-based "prefix product"
    - Create a right-based "prefix product"
    - ans[i] = leftArr[i-1] * rightArr[i+1]
        - "everything to the left and everything to the right
    Time: O(N)
    Space: O(N) 
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        leftArr = [1] * length
        rightArr = [1] * length
        
        # fill leftArr
        leftArr[0] = nums[0]
        for i in range(1, length):
            leftArr[i] = leftArr[i-1] * nums[i]
        
        # fill rightArr
        rightArr[-1] = nums[-1]
        for i in range(2, length+1):
            rightArr[-i] = rightArr[-(i-1)] * nums[-i]
        
        ans = [1] * length
        ans[0] = rightArr[1]
        ans[-1] = leftArr[-2]
        for i in range(1,length-1):
            ans[i] = leftArr[i-1] * rightArr[i+1]
        return ans


# slightly cleaner solution
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        leftArr = [1] * (length+1)
        rightArr = [1] * (length+1)
        
        # fill leftArr
        for i in range(1, length+1):
            leftArr[i] = leftArr[i-1] * nums[i-1]
        
        # fill rightArr
        for i in range(2, length+2):
            rightArr[-i] = rightArr[-(i-1)] * nums[-(i-1)]

        ans = [1] * length
        for i in range(length):
            ans[i] = leftArr[i] * rightArr[i+1]
        return ans
