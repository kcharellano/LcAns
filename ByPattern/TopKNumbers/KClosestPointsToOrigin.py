'''
    Algorithm: Heap
    - Get the distance from the origin to every point
    - store distances in a heap and only keep the k-closest points
    Time: O(n * logK)
    Space: O(K)
'''

from math import sqrt
import heapq

class Solution:
    # returns euclidean distance from 0,0 to x,y
    def euclid(self, x, y) -> int:
        return ((0-x)**2 + (0-y)**2)**(.5)
    
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # (dist, x, y)
        distList = []
        
        # fill distList with distance to each point from origin
        size = 0
        for point in points:
            heapq.heappush(distList, (-self.euclid(point[0], point[1]), point))
            if size == k:
                heapq.heappop(distList)
            else:
                size += 1
                
        return [point for d, point in distList]
            
            
        