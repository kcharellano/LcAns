from math import inf
'''
    Algorithm: Greedy 
    - Sort arrows based on start position in ascending order
    - Loop over balloons
    - try to burst as many balloons as you can with one arrow by seeing how many balloons in a row
    can overlap. Keep updating the common span balloons x1 to xN share
    Time: O(NLogN)
    Space: O(1)
'''
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if points == []: return 0
        
        points.sort(key=lambda x: x[0])
        arrows = 1
        span = [-1, inf]
        # find the max ballons you can pop with a single arrow
        for pair in points:
            if pair[0] <= span[1]:
                span = [max(pair[0], span[0]), min(pair[1], span[1])]
            else:
                arrows += 1
                span = [pair[0], pair[1]]
        return arrows