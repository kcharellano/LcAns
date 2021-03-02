from collections import defaultdict

'''
    Algorithm: Optimized DFS
    - Detect cycles using DFS
    - Use a localSeen to detect cycle
    - Use a globalSeen to avoid duplicate work
    Time: O( V + E)
    Space: O(V + E), we have to build a graph
'''

class Solution:
    # globalSeen -- nodes processed in another dfs exploration
    # localSeen -- nodes visited in the current dfs exploration
    # returns true if dfs finds cycle
    def dfsCycle(self, graph, node, globalSeen, localSeen):
        if node in globalSeen:
            return False
        if node in localSeen:
            return True
        localSeen.add(node)
        for adj in graph[node]:
            if self.dfsCycle(graph, adj, globalSeen, localSeen):
                return True
        globalSeen.add(node)
        return False
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Form graph
        graph = defaultdict(lambda: [])
        for course, prereq in prerequisites:
            graph[prereq].append(course)
        # used for nodes visited in any dfs exploration
        # ignore visited nodes
        globalSeen = set()
        for i in range(numCourses):
            if graph[i] and self.dfsCycle(graph, i, globalSeen, set()):
                    return False
        return True

'''
    Same solution as above except using a single
    int array to describe node states instead of a globaLSeen set and
    a localSeen set
'''
from collections import defaultdict
class Solution:
    
    # returns true if dfs finds cycle
    def dfsCycle(self, graph, node, nodeStates):
        if nodeStates[node] == 1:
            return True
        if nodeStates[node] == 2:
            return False
        nodeStates[node] = 1
        for adj in graph[node]:
            if self.dfsCycle(graph, adj, nodeStates):
                return True
        nodeStates[node] = 2
        return False
    
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Form graph
        graph = defaultdict(lambda: [])
        for course, prereq in prerequisites:
            graph[prereq].append(course)
        
        # state = 0, unvisited
        # state = 1, visited locally only
        # state = 2, fully processed -- i.e determined not to be part of a cycle
        nodeStates = [0] * numCourses
        for i in range(numCourses):
            if graph[i] and self.dfsCycle(graph, i, nodeStates):
                    return False
        return True