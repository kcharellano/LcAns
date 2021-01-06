# https://leetcode.com/problems/fruit-into-baskets
'''
    Algorithm: Dynamic Sliding Window
        - expand right until 3rd type of fruit is encountered
        - if 3rd type of fruit is encountered, remove fruits from basket
        until only one type of fruit exists in basket.
    Time: O(N)
    Space: O(1)
'''
class Solution:
    def addFruit(self, basket, tree, i):
        if tree[i] in basket:
            basket[tree[i]] += 1
            return 0
        else:
            basket[tree[i]] = 1
            return 1
    
    def removeFruit(self, basket, tree, i):
        basket[tree[i]] -= 1
        if basket[tree[i]] == 0:
            del basket[tree[i]]
            return -1
        else:
            return 0

    def totalFruit(self, tree: List[int]) -> int:
        maxSize = 0
        left = 0
        basket = {}
        count = 0
        trees = len(tree)
        for i in range(trees):
            if count == 2 and not tree[i] in basket:
                maxSize = max(maxSize, i - left)
                # new fruit and no room in basket
                while count > 1:
                    # remove fruit in order that it was added until only one
                    # type of fruit is left in the basket
                    count += self.removeFruit(basket, tree, left)
                    left += 1
            # otherwise
            count += self.addFruit(basket, tree, i)
        return max(maxSize, i+1-left) if maxSize != 0 else trees
      