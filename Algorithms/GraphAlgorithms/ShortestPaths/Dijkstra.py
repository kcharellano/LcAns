'''
    Single Source Shortest Path
    Time: O(|E| * log(|V|))
    Space: O(N)
'''
from math import inf
import heapq

def dijkstra(graph, start, end):
    # create distance table
    d = {}
    for node in graph:
        d[node] = inf
    
    # initialize start distance
    d[start] = 0

    # initialize processed table to avoid processing the same node twice
    processed = set()
    
    # intialize minheap --> (distance, node, tiebreaker)
    tb = 1
    minheap = [(0, start, 0)]
    while minheap:
        i, node, j = heapq.heappop(minheap)
        if node in processed:
            continue
        processed.add(node)
        for neighbor,cost in graph[node]:
            if d[neighbor] > d[node] + cost:
                d[neighbor] = d[node] + cost
                heapq.heappush(minheap, (d[neighbor], neighbor, tb))
                tb += 1
    return d[end]
