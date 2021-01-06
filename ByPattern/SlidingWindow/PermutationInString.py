# https://leetcode.com/problems/permutation-in-string

'''
    Algorithm: Static Sliding Window
        - Form a static window of size s1
        - Move window one letter at a time along s2 and
        check if window contains permutation
    Time: O((L2-L1)*L1)) -- L1 = size of s1 and L2 = size of s2. Comparing strings
    Space: O(distinctLetters(s2)) --
'''
class Solution:
    def compare(self, perm, window):
        for key in perm:
            if perm[key] != window.get(key, 0):
                return False
        return True
    
    def removeLetter(self, letter, hmap):
        hmap[letter] -= 1
        if hmap[letter] == 0:
            del hmap[letter]
    
    def addLetter(self, letter, hmap):
        if letter in hmap:
            hmap[letter] += 1
        else:
            hmap[letter] = 1

    def checkInclusion(self, s1: str, s2: str) -> bool:
        # edgecase: the permutation is bigger than the wrapping word
        s2Size = len(s2)
        s1Size = len(s1)
        if s2Size < s1Size:
            return False
        # initialize mapping to compare window
        permMap = {}
        for letter in s1:
            self.addLetter(letter, permMap)
        # initialize starting window
        window = {}
        for i in range(s1Size):
            self.addLetter(s2[i], window)
        # edgecase: first s1Size letters contain the permutation
        if self.compare(permMap, window):
            return True
        left = 0
        for j in range(i+1, s2Size):
            # remove leftMost letter from window
            self.removeLetter(s2[left], window)
            left += 1
            # add new letter
            self.addLetter(s2[j], window)
            if self.compare(window, permMap):
                return True
        return False

'''
    Algorithm: Brute Force
        - At every index that starts with a letter in the permString
        loop until all perm letters have been found.
    Time: O(N^2)
    Space: O(N) -- b/c of the hashmap
'''
class Solution:
    def checkForPerm(self, index, permMapCopy, s2Length):
        j = index
        while permMapCopy:
            if j >= s2Length:
                # s1 cant be in s2 if j reaches out of bounds
                return False
            letter = s2[j]
            if letter in permMapCopy:
                # decr letter count or remove letter from permMapCopy
                permMapCopy[letter] -= 1
                if permMapCopy[letter] == 0:
                    del permMapCopy[letter]
                j += 1
            else:
                return False

    def checkInclusion(self, s1: str, s2: str) -> bool:
        # create a letterMap
        permMap = {}
        for letter in s1:
            if letter in permMap:
                permMap[letter] += 1
            else:
                permMap[letter] = 1
        
        s2Length = len(s2)
        for i in range(s2Length):
            if s2[i] in permMap:
                permMapCopy = permMap.copy()
                if self.checkForPerm(self, i, permMapCopy, s2Length):
                    return True
        return False