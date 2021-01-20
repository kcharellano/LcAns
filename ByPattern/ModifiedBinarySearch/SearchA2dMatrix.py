# https://leetcode.com/problems/search-a-2d-matrix/

'''
    Algorithm:
        - Find row that target may reside in by using problem constraints
        - perform a binary search on that row to look for target
    Time: O(M + log(N)) M = # of rows, N = # of columns
    Space: O(1)
'''
import math
class Solution:
    def binSearch(self, left, right, nums, target):
        while left <= right:
            mid = math.floor((left + right) / 2)
            
            if target == nums[mid]:
                return True
            
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowSize = len(matrix)
        colSize = len(matrix[0])
        # find row that contains target
        for row in range(rowSize):
            if target <= matrix[row][colSize-1]:
                if target >= matrix[row][0]:
                    return self.binSearch(0, colSize-1, matrix[row], target)
                else:
                    return False
        return False
