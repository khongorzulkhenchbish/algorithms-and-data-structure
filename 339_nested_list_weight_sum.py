# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        The result is undefined if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        The result is undefined if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        """
        time: O(N), Space: O(height)
        sum = 0
        [[1,1],2,[1,1]]
        => d = 1
        [1,1] => isInteger => false => dfs(list, d+1)
            1, 1 isInteger => true => sum = 4
        2 => int => true => sum  = 6
        [1,1] ... => 4 => sum = 10
        """
        def dfs(lst, depth):
            total = 0

            for elem in lst:
                if elem.isInteger(): # calc sum
                    total += elem.getInteger() * depth
                else: # calc sublists sum separately
                    total += dfs(elem.getList(), depth + 1)
            
            return total
        
        return dfs(nestedList, 1)
        """
        nestedList = [0] => 0
        nestedList = [1,[4,[6]]]
            1 => total = 1
            [4,[6]] => 4 => 4*2 => total = 9
            [6] => dfs([6], 3) => 3*6 => total = 27
        """
