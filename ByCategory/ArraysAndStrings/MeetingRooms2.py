'''
    https://leetcode.com/problems/meeting-rooms-ii/
'''

import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if intervals == []:
            return 0
        
        # sort meeting rooms by their start times in descending order
        # NOTE: Logically, we will be looking at rooms with the earliest start times
        intervals.sort(reverse=True)
        
        roomCounter = 0
        # rooms are sorted based on their endtime
        roomHeap = []
        while intervals:
            # get interval with earliest start time
            interval = intervals.pop()
            
            # check if any rooms are available
            if roomHeap:
                # peek earliest endtime
                if roomHeap[0] <= interval[0]:
                    # the next meeting starts after the earliest endtime -- reuse room
                    heapq.heappop(roomHeap)
                    heapq.heappush(roomHeap, interval[1])
                    continue

            heapq.heappush(roomHeap, interval[1])
            roomCounter += 1
        return roomCounter            