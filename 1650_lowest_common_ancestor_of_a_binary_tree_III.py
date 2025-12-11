"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        """
        Optimal solution: Time: O(N), Space: O(1)
        Idea is the turtle and hare problem
        """
        p_copy = p
        q_copy = q

        while p_copy != q_copy:
            q_copy = q_copy.parent if q_copy else p
            p_copy = p_copy.parent if p_copy else q

        return p_copy
        
        # p = 5, q = 1
        # tree = 3
        #       / \
        #      5   1
        #     / \
        #    6   4
        
        # q_copy = 1 3 N->p 4      5 3
        # p_copy = 4 5      3 N->q 1 3  => p == q

        """
        Approach 1: Time: O(2N), Space: O(N) 
        def dfs(parentset, node):
            if not node:
                # we are at the root
                print("end")
                return parentset
            
            # print(f"{node.val} for {parentset}")
            if node.val in parentset:
                # if q's has shared parent with p
                return node
            
            parentset.add(node.val) # current val will be parent of the prev
            return dfs(parentset, node.parent)

        # collect parent set of p
        parentset = set()
        parentset = dfs(parentset, p)

        # collect parent set of q, but if we see the same val again, that means, we found the LCA
        LCA = dfs(parentset, q)

        return LCA
