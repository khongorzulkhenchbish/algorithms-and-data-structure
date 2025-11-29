# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # time O(n), space O(height of tree)
        def dfs(node, parentSum):
            if not node:
                return 0
            
            # calc parent sum upon passing into dfs
            parentSum = parentSum*10 + node.val

            # leaf node
            if not node.left and not node.right:
                return parentSum
            
            # integrate the possible sums until current level
            return dfs(node.right, parentSum) + dfs(node.left, parentSum)
        
        return dfs(root, 0)
        """
        root = [4,9,0,5,1]
        dfs(4, 0)
            dfs(0, 4)
                parentSum = 4*10+0 => return 40
            dfs(9, 4)
                parentSum = 49
                dfs(1, 49)
                    parentSum += return 491
                dfs(5, 49)
                    parentSum += return 495
        
        [] => 0
        [0, 1, 2] => 3
        
        """
