# https://leetcode.com/problems/trapping-rain-water/

# Brute force approach using dynamic programming to shorten time
# Time: O(n)
class Solution:
    def trap(self, height: List[int]) -> int:
        prevMax = 0
        maxFromLeft = []
        for i in range(len(height)):
            maxFromLeft.append(max(prevMax, height[i]))
            if height[i] > prevMax:
                prevMax = height[i]
        
        prevMax = 0
        maxFromRight = []
        for i in reversed(range(len(height))):
            maxFromRight.insert(0, max(prevMax, height[i]))
            if height[i] > prevMax:
                prevMax = height[i]
        
        water = 0
        for index in range(len(height)):
            water += min(maxFromLeft[index], maxFromRight[index]) - height[index]
        return water
        