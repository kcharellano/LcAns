# https://leetcode.com/problems/group-anagrams

'''
    Algorithm: 
    - Sort each word and add it to a dict entry
    - return all lists in dict
    Time: O(N * slogs), N = # of words, S = length of longest word
    Space: O(N)
'''
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        # map words into groups
        for word in strs:
            sortedWord = "".join(sorted(word))
            d[sortedWord].append(word)
        # format answer
        return [ls for ls in d.values()]

'''
    Algorithm: Slightly faster than above
    - Each word has a letter count i.e a:1,b:0,c:0 ... z:1
    - use those counts to map words to buckets
    Time: O(N * S), N = # of words, S = length of longest word
    Space: O(N)
'''
from collections import defaultdict
from string import ascii_lowercase
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        asciiVal = {}
        d = defaultdict(list)
        for val, char in enumerate(ascii_lowercase, start=0):
            asciiVal[char] = val
        for word in strs:
            count = [0] * 26
            for letter in word:
                count[asciiVal[letter]] += 1
            d[tuple(count)].append(word)
        return [ls for ls in d.values()]
                

