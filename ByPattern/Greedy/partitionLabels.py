
# https://leetcode.com/problems/partition-labels/
from collections import defaultdict
'''
    Algorithm: Greedy
    - Get the intervals for each letter where that letter only occurs in that interval
    - Loop through intervals in the order seen and merge intervals
    - The number of intervals left is the max number of intervals that fulfill condition
'''
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        # key = letter, val = [start, end]
        intervals = defaultdict(list)
        # order of intervals seen
        order = []
        for i, letter in enumerate(S):
            if letter not in intervals:
                order.append(letter)
                intervals[letter].extend([i, i])
            else:
                intervals[letter][1] = i
        # merge intervals
        ls = [intervals[order[0]]]
        ptr = 0
        for i in range(1, len(order)):
            A, B = ls[ptr], intervals[order[i]]
            if A[0] <= B[0] and B[0] <= A[1]:
                # merge A and B
                A[1] = max(A[1], B[1])
            else:
                # add B as new interval
                ls.append(B)
                ptr += 1
        
        return [A[1] - A[0] + 1 for A in ls]