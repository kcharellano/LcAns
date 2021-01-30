# https://leetcode.com/problems/minimum-genetic-mutation/submissions/

'''
    Algorithm: BFS Shortest Paths
    - treat each start, end and the sequences in word bank as nodes
    - The problem then turns into a shortest paths problem where start is the start node, 
    end is the end node and all the sequences in word bank are middle nodes
    - Implement a standard shortest paths BFS search
    Time: O(V+E) -- note that isMutation() is constant because every sequence is of size 8
    Space: O(V)
    NOTE: This code can't handle cycles becuase visited nodes arent tracked
'''
from collections import deque
class Solution:
    def isMutation(self, start, end):
        # returns true if start and end are one letter apart
        flag = True
        for i in range(8):
            if start[i] != end[i]:
                if flag:
                    flag = False
                else:
                    return False
        return False if flag == True else True
    
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        # edgecase: end is not a valid mutation
        if not end in bank:
            return -1
        
        # deque = (starting node, stepCount)
        queue = deque([(start, 0)])
        while queue:
            node, step = queue.popleft();
            
            if node == end:
                return step
            
            for sequence in bank:
                if self.isMutation(node, sequence):
                    queue.append((sequence, step+1))
        return -1
        