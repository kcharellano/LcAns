# https://leetcode.com/problems/fruit-into-baskets
'''
    Algorithm: Dynamic Sliding Window
        - expand right until 3rd type of fruit is encountered
        - if 3rd type of fruit is encountered, shift window 1 index to the right
        - no need to shrink window because a smaller size window will NEVER be the answer
    Time: O(N)
    Space: O(1)
'''
from collections import defaultdict
from math import inf

class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        unique, left = 0, 0
        basket = defaultdict(int)
        maxFruits = 1
        for i in range(len(tree)):
            fruit = tree[i]
            if basket[fruit] == 0:
                # first fruit occurence
                unique += 1
            # add fruit to basket
            basket[fruit] += 1
            # remove fruits from basket until only 2 types of fruit exist
            if unique > 2:
                fruit = tree[left]
                basket[fruit] -= 1
                if basket[fruit] == 0:
                    unique -= 1
                left += 1
            maxFruits = max(maxFruits, i - left + 1)
        return maxFruits
      