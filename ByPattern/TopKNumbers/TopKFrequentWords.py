# https://leetcode.com/problems/top-k-frequent-words/
'''
    Algorithm: Sorting
    - count frequencies of words
    - sort based on freq then lexicographically
    - extract k items from list
    Time: O(nLogn)
    Space: O(n)
'''
from collections import defaultdict
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # count the frequencies of all the words
        freq = defaultdict(lambda: 0)
        for word in words:
            freq[word] += 1
        # sort words based on frequencies, then lexicographically
        pairs = list(freq.items())
        pairs.sort(key=lambda w: (-w[1], w[0]))
        
        # extract k words from pairs
        return [pairs[i][0] for i in range(k)]