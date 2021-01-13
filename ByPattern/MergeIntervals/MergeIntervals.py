'''
    https://leetcode.com/problems/merge-intervals
'''

'''
    Algorithm: linear scan
        - sort intervals by their start time
        - loop through intervals in order and merge intervals 
        by keeping track of the current max of the last interval added
        to the answer list.
    Time: O(nlogn) -- b/c we need to sort the list first
    Space: O(N) -- b/c we create a new list to store answer
'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort intervals by their start time
        intervals.sort(key=lambda x: x[0])

        ans = [intervals[0]]
        ansIndex = 0
        end = ans[0][1]
        for i in range(1, len(intervals)):
            # merge overlapping intervals
            if intervals[i][0] <= end:
                end = max(end, intervals[i][1])
                ans[ansIndex][1] = end
            else:
                # append new interval to answer list
                end = intervals[i][1]
                ans.append(intervals[i])
                ansIndex += 1
        return ans
