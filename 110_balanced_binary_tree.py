class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # height-balanced: depth of two subtree never differs by more than one
        # To solve it in one traversal O(N), the DFS needs to return 2 information at once:
        # 1. Is this subtree balanced?
        # 2. What is the height of this subtree?
        # The trick to avoid conflicting return is to use sentinel value. If a subtree is balanced, return -1
        # Otherwise, return its actual height.

        def check_height(node):
            if not node:
                return 0 # base case
            
            # Left subtree
            left = check_height(node.left)
            if left == -1: return -1 # Already unbalanced below

            # Right subtree
            right = check_height(node.right)
            if right == -1: return -1 # Already unbalanced below

            # Check current nodes balance
            if abs(left - right) > 1:
                return -1 # Unbalanced at this node
            
            # Return actual height to the caller
            return 1 + max(left, right)
        
        return check_height(root) != -1 # If it is balanced, it will return "True"

        # Brute force
        # Time: O(N^2), dfs_height will be called for every node
        # Space: O(N^2)
        def dfs_height(root, height=0):
            if not root:
                return height
            
            return max(dfs_height(root.left, height+1), dfs_height(root.right, height+1))
        
        # isbalanced main function
        if not root:
            return True
        
        # for every node left and right children, calculate the height difference
        if abs(dfs_height(root.left, 0) - dfs_height(root.right, 0)) > 1:
            return False