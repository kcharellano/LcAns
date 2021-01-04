'''
    Disjoint sets are collections of nodes where there is no overlap between sets.
'''

    
class SetNodeNaive:
    def __init__(self, value):
        self._repr = self
        self._value = value

    # create a new set
    def makeSet(self, value):
        return self.SetNode(value)

    # get repr by following path from node to root
    # NOTE: time: O(N) where N is the # of nodes from node to root    
    def find(self):
        if self._repr != self:
            return self._repr.find()
        return self._repr

    # merge two disjoint sets
    # NOTE: naive for reasons, you want to merge smaller to larger set
    def union(self, other):
        self.find()._repr = other.find()._repr

class SetNodeOpt:
    def __init__(self, value):
        self._repr = self
        self._value = value
        self._size = 1
    
    # Path compression, maintain the repr of each setNode to
    # point to the absolute repr
    # NOTE: O(1) armotized
    def find(self):
        if self._repr != self:
            self._repr = self.find()._repr
        return self._repr
    
    # Merge two sets based on sizes
    # Merge smaller set with larger set
    def union(self, other):
        myAbsRepr = self.find()
        otherAbsRepr = other.find()
        # merge and update size of new repr
        if myAbsRepr._size > otherAbsRepr._size:
            otherAbsRepr._repr = myAbsRepr
            myAbsRepr._size += otherAbsRepr._size
        else:
            myAbsRepr._repr = otherAbsRepr
            otherAbsRepr._size += myAbsRepr._size