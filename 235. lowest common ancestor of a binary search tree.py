# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        Time: O(log n) only visit one of the level nodes
        Space: O(log n) only stores halft times the nodes
        Space: O()
        Tip: Think about binary tree rule. lower on the left, higher on the right side.
          6     => Case 1. p=7, q=9 => LCA is in the right subtree
        2   8   => Case 2. p=2, q=4 => LCA is in the left subtree
       0 4 7 9  => Case 3. p=2, q=8 => LCA is the current, when p and q are separate sides.
        3 5
        '''
        
        if not root:
            return None

        if root == p or root == q:
            return root
        
        if root.val <= p.val and root.val <= q.val: # LCA is on the right side
            return self.lowestCommonAncestor(root.right, p, q)
        
        if root.val >= p.val and root.val >= q.val: # LCA is on the left side
            return self.lowestCommonAncestor(root.left, p, q)

        if root.val >= p.val and root.val <= q.val: # LCA is the root itself
            return root
        
