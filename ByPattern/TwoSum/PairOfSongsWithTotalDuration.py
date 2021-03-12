# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
'''
    Algorithm: Two Sum
    - Normalize times
    - Use two sum to find two pairs of songs that sum to 60
    Time: O(N)
    Space: O(N)
'''
from collections import defaultdict
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # normalize times
        for i in range(len(time)):
            time[i] = time[i] % 60
        print(time)
        # find two pairs that sum to 60
        seen = defaultdict(lambda: 0)
        count = 0
        for t in time:
            addend = (60 - t) % 60
            if addend in seen:
                count += seen[addend]
            seen[t] += 1
        return count