# https://leetcode.com/problems/number-of-provinces/

'''
    Algorithm: UnionFind for connected components
    - Use the union find data structure to find connected components
    Time: O(N^2)
    Space: O(N)
    Find: Determine which subset a particular element is in. This can be used for determining if two elements are in the same subset.
    Union: Join two subsets into a single subset.
'''
class Solution:
    
    class Node:
        def __init__(self, value):
            self.rep = self
            self.value = value
            self.size = 1

    # returns a node's representative
    def find(self, node):
        if node.rep != node:
            node.rep = self.find(node.rep)
        return node.rep

    # merges(aka union) two sets
    def merge(self, a, b):
        repB = self.find(b)
        repA = self.find(a)
        if repA.size > repB.size:
            repA.size += repB.size
            repB.rep = repA
        else:
            repB.size += repA.size
            repA.rep = repB

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        rowSize, colSize = len(isConnected), len(isConnected[0])
        # create set nodes
        nodeLs = [self.Node(i) for i in range(rowSize)]
        for row in range(rowSize):
            for col in range(colSize):
                # skip nodes connected to themselves
                if row == col:
                    continue
                # skip nodes that aren't connected
                if isConnected[row][col] == 0:
                    continue
                # connect nodes that aren't already connected
                if self.find(nodeLs[row]).value != self.find(nodeLs[col]).value:
                    a = nodeLs[row]
                    b = nodeLs[col]                    
                    self.merge(nodeLs[row], nodeLs[col])
        
        # count the number of distinct sets
        count = 0
        for node in nodeLs:
            if self.find(node) == node:
                count += 1
        return count
                
'''
    Algorithm: Connected Components in Undirected Graph
    - Use DFS to find the number of connected components
    - Count the number of times DFS is triggered
    Time: O(N^2)
    Space: O(N)
'''
class Solution:
    def dfs(self, graph, node, visited, n):
        for i in range(n):
            if graph[node][i] == 1 and i not in visited:
                visited.add(i)
                self.dfs(graph, i, visited, n)
    
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        n = len(isConnected)
        count = 0
        for node in range(n):
            if node not in visited:
                self.dfs(isConnected, node, visited, n)
                count += 1
        return count
                