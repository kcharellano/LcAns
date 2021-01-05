'''
    https://leetcode.com/problems/word-ladder/solution/
'''

'''
    Algorithm:
        - Form bidirectional graph using beginWord and wordList
            - Each node is a word, each edge represents a one letter transformation
        - Use dijkstra's algorithm to find shortest path from beginWord to endWord
    NOTE: leetcode doesn't accept bc of runtime, need to find a better methods for oneAway.
'''
from math import inf
import heapq
class Solution:
    # determines if two words differ by atmost one letter
    def oneAway(self, word1, word2):
        flag = False
        for w1, w2 in zip(word1, word2):
            if w1 != w2:
                if flag:
                    return False
                else:
                    flag = True
        return True
    
    def dijkstra(self, graph, table, start, end):
        # initialize start distance
        table[start] = 1
        
        # create minheap
        minheap = []
        
        # processed table to avoid processing the same node twice
        processed = set()
        
        # initialize minheap --> (distance, tiebreaker, node)
        heapq.heappush(minheap, (1, 0, start))
        tb = 1
        
        # algoriithm
        cost = 1
        while minheap:
            # pop minimum element
            distance, i, word = heapq.heappop(minheap)
            
            # skip processed nodes
            if word in processed:
                continue
            processed.add(word)
            
            # attempt to relax each edge if the cost from word to neighbor is less than 
            # the tables current distance from start to neighbor
            for neighbor in graph[word]:
                if table[neighbor] > table[word] + cost:
                    table[neighbor] = table[word] + cost
                    heapq.heappush(minheap, (table[neighbor], tb, neighbor))
                    tb += 1
        return table[end]

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # form bidirectional graph from wordlist
        graph = {}
        d = {}
        
        # fill graph with nodes and form distance array for dijstra's algo
        graph[beginWord] = []
        d[beginWord] = inf
        for listWord in wordList:
            graph[listWord] = []
            d[listWord] = inf
            
        # add bidirectional edges
        for listWord in wordList:
            for graphWord in graph:
                if self.oneAway(listWord, graphWord):
                    graph[graphWord].append(listWord)
                    graph[listWord].append(graphWord)
        
        # edgecase: endword not in graph
        if not endWord in graph:
            return 0
        
        # perform dijkstra's shortest path algortihm
        ans = self.dijkstra(graph, d, beginWord, endWord)
        return 0 if ans == inf else ans
        
                    