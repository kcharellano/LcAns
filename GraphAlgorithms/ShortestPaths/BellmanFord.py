'''
    Single Source Shortest Path Algorithm
    Assume graph is given as an edge list
    Note: Optimization is stop searching when no distance value is changed.
    Note: To use this algorithm to detect a negative cycle then run the algorithm
        N times. If any value in the distance table changes during the Nth iteration 
        then a negative cycle is present.
'''
from math import inf
def bellmanFord(edgeList, nodeList, startNode, endNode):
    # create distance table
    d = {}
    for node in nodeList:
        d[node] = inf
    
    # initialize start distance
    d[start] = 0

    # start algorithm
    for i in range(len(nodeList)-1):
        for edge in edgeList:
            d[edge.end] = min(d[edge.to, d[edge.start] + edge.cost])
    return d[endNode]