# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
'''
    Algorithm: Count Intitial DFS Triggers
    - Build adjacency list from graph using edges
    - Count DFS triggers
    Time: O(N)
    Space: O(N)
'''
from collections import defaultdict

class Solution:
    def dfs(self, node, graph, visited):
        # visit node
        visited.add(node)
        
        # explore neighbors
        for adj in graph[node]:
            if adj not in visited:
                self.dfs(adj, graph, visited)
    
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # build adjcency list graph from edges
        graph = defaultdict(lambda: [])
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        # perform DFS on unvisited nodes and count times DFS is triggered
        visited = set()
        count = 0
        for node in range(n):
            if node not in visited:
                self.dfs(node, graph, visited)
                count += 1
        return count