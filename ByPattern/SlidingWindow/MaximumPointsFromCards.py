# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards

'''
    Algorithm: Sliding Window Variation
    - form a prefix sum starting from left up to k
    - form a prefix sum starting from right up to k
    - Compare every possibilty of combinations between choosing left and right
    and choose the maximum sum combination
    Time: O(K)
    Space: O(K)
'''

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        rsum = 0
        leftSum = [0]
        for i in range(k):
            rsum += cardPoints[i]
            leftSum.append(rsum)
        rsum = 0
        rightSum = [0]
        for i in range(1, k+1):
            rsum += cardPoints[-i]
            rightSum.append(rsum)
        
        maxPoints = -1
        leftPtr = 0
        rightPtr = k
        for i in range(k+1):
            maxPoints = max(maxPoints, leftSum[leftPtr] + rightSum[rightPtr])
            leftPtr += 1
            rightPtr -= 1
        return maxPoints
