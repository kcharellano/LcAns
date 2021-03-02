from collections import defaultdict, deque
class Solution:
    # Returns true if cycle is found
    def topoSort(self, graph, node, nodeStates, order):
        if nodeStates[node] == 1:
            return True
    
        nodeStates[node] = 1
        for adj in graph[node]:
            if nodeStates[adj] == 2:
                continue
            if self.topoSort(graph, adj, nodeStates, order):
                return True
        order.appendleft(node)
        nodeStates[node] = 2
        return False
    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build graph
        graph = defaultdict(lambda: [])
        for course, prereq in prerequisites:
            graph[prereq].append(course)
        
        # use topological sort to find ordering
        order = deque()
        # nodeStates: 0 = unvisited, 1 = locally visited, 2 = fully processed
        nodeStates = defaultdict(lambda: 0)
        for course in range(numCourses):
            if nodeStates[course] == 0:
                if self.topoSort(graph, course, nodeStates, order):
                    return []
        return order