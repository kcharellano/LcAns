# https://leetcode.com/problems/critical-connections-in-a-network/

# Explanation: Look at LC solution tab
# Time: O(V + E)
# Space: O(E)
from collections import defaultdict
class Solution:
    def dfs(self, node, graph, edgeSet, rank, discoveryRank):
        # A node with a rank has already been visited by DFS
        if node in rank:
            return rank[node]
        
        rank[node] = discoveryRank
        # Will store start of cycle if there is one
        # If no cycle, it will store the rank of the next node
        minRank = discoveryRank + 1
        for adj in graph[node]:
            # skip parent
            if adj in rank and rank[adj] == discoveryRank - 1:
                continue
            
            # recurse on the neighbor
            recursiveRank = self.dfs(adj, graph, edgeSet, rank, discoveryRank+1)
            
            # check if edge needs to be removed
            if recursiveRank <= discoveryRank:
                edgeSet.remove((min(node, adj), max(node,adj)))
                
            # update minrank
            minRank = min(minRank, recursiveRank)
        
        return minRank

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # build adjacency list graph from connections
        graph = defaultdict(lambda: [])
        # will store critical edges
        edgeSet = set()
        for edge in connections:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            edgeSet.add((min(edge), max(edge)))
        rank = {}
        # call dfs
        self.dfs(0, graph, edgeSet, rank, 0)
        
        return list(edgeSet)
