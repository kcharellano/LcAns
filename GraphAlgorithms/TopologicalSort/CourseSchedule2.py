'''
    Topological Sort solution
    Time: O(V+E) b/c dfs traverses every edge and vertex once
    Space: O(V+E)
'''
from collections import deque
class Solution:
    
    # accepts a directed graph as an adj list(dictionary?).
    def topologicalSort(self, graph, nodeStates, ordering, currentNode):
        # mark node state as 'in process'
        nodeStates[currentNode] = 1

        # perform dfs on every adj node
        for adjNode in graph[currentNode]:
            if nodeStates[adjNode] == 1:
                # cycle detected -- cannot form topological ordering
                return -1
            elif nodeStates[adjNode] == 2:
                # skip adj nodes that are fully processed.
                continue
            else:
                if self.topologicalSort(graph, nodeStates, ordering, adjNode) == -1:
                    # subroutine detected cycle
                    return -1
        
        # if here currentNode has processed all its neighbors
        nodeStates[currentNode] = 2
        ordering.appendleft(currentNode)
        return 0

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # add nodes to graph
        graph = {}
        nodeStates = {}
        for i in range(numCourses):
            graph[i] = []
            nodeStates[i] = 0
        
        # form directed edges from prerequesites
        for course, prereq in prerequisites:
            graph[prereq].append(course)
        
        # topological sort
        ordering = deque()
        
        # start topolical sort on every node whose state is 0 
        for i in range(numCourses):
            if nodeStates[i] == 0:
                if self.topologicalSort(graph, nodeStates, ordering, i) == -1:
                    return []
        return ordering
