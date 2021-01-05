'''
'''

'''
    Algorithm: Brute Force
        - Find the maximum area of every bar to the left and right of it
    Time: O(N^2)
    Space: O(1)
'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maximumArea = 0
        listLen = len(height)
        for index in range(listLen):
            # check areas to the left of index
            for cursor in reversed(range(0, index)):
                minHeight = min(height[cursor], height[index])
                distance = index - cursor
                maximumArea = max(maximumArea, minHeight * distance)
            # check areas to the right of index
            for cursor in range(index+1, listLen):
                minHeight = min(height[index], height[cursor])
                distance = cursor - index
                maxiumArea = max(maximumArea, minHeight*distance)
        return maximumArea
'''
    Algorithm:
        - Two Pointers
        - both pointers start at opposite ends of the height list
        - check their area against maximumArea
        - move the pointer whose height is smaller
    Time: O(N)
    Space: O(1)
'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maximumArea = 0
        left = 0
        right = len(height) - 1
        while left < right:
            maximumArea = max(maximumArea, min(height[left], height[right]) * (right - left))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return maximumArea
