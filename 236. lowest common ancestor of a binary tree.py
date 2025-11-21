# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        time: O(n) space: O(n)
        Case 1: p and q are in separate branches => LCA node itself
        Case 2: p is parent of q => p is the LCA
        Case 3: q is parent of p => q is the LCA
        """
        if not root:
            return None
        
        if root == p or root == q: # p and q are given as trees themselves
            return root
        
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        if l and r: # p and q exist on separate sides
            return root
        else:
            # The key is that when we use dfs, the parent will be found always first
            return l or r