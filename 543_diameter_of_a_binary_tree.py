# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root):
        # DFS traversal, O(n) time, O(n) space
        maxd = 0

        # returns height
        def dfs(root):
            if not root: 
                return 0
            
            # height of left and right subtree
            left = dfs(root.left)
            right = dfs(root.right)

            # node itself not included yet
            nonlocal maxd
            maxd = max(maxd, left+right)
            # return current height including the node itself
            return max(left, right) + 1
        
        dfs(root)
        return maxd