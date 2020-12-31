'''
    Algorithm: Give candy to lowest rated kids first
        - In ascending order distribute candy to kids based on their neighbors
    Time: O(nLogn) --> because of the heap to sort kids in ascending order
    Space: O(N)
    NOTE: Another solution is to do a left pass and right pass following the candy rules
    only for one direction. Then do a final pass and the index is equal to max(left, right)
'''

import heapq
class Solution:
    def candy(self, ratings: List[int]) -> int:
        minHeap = []
        candyList = []
        length = len(ratings)
        # do a first pass on children ratings to store them on heap
        for index, rating in enumerate(ratings):
            heapq.heappush(minHeap, (rating, index))
            candyList.append(0)
        
        candies = 0
        while minHeap:
            # pop the kid with the lowest rating
            rating, currIndex = heapq.heappop(minHeap)
            minGive = 1
            # check left neighbor
            if currIndex-1 >= 0 and candyList[currIndex-1] != 0:
                if ratings[currIndex-1] < ratings[currIndex]:
                    minGive = max(minGive, candyList[currIndex-1]+1)

            # check right neighbor
            if currIndex+1 < length and candyList[currIndex+1] != 0:
                if ratings[currIndex] > ratings[currIndex+1]:
                    minGive = max(minGive, candyList[currIndex+1]+1)
            
            # give candy
            candyList[currIndex] = minGive
            candies += minGive
        return candies
                
            