# https://leetcode.com/problems/maximum-units-on-a-truck

'''
    Algorithm: Greedy
    - Choose the boxes with the most units first
    Time: O(nlogn)
    Space: O(1)
'''

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        maxUnits = 0
        for box in boxTypes:
            # truck is full
            if truckSize == 0:
                break
            # all boxes of type i fit in truck
            elif truckSize >= box[0]:
                maxUnits += (box[1] * box[0])
                truckSize -= box[0]
            # only some boxes of type i fit in truck
            # we have move boxes than truckSize
            else:
                maxUnits += (truckSize * box[1])
                truckSize -= truckSize
        return maxUnits
                