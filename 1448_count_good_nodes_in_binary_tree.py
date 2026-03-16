class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # We have to check every possible path => DFS than BFS.
        # The path could contains elems in decreasing order but if it is higher than the max, that still counts [3,1,3] = 2
        # 1. How to pass the max value through DFS?
        # 2. How to count good paths, and this can be returned?
        # Time: O(N) traverses every nodes once
        # Space: O(H) where H is height of the tree

        def dfs(node, curmax):
            # I'm already visiting the parents on my way down.
            # If I just carry the 'Current Max' in my pocket (as a function argument),
            # I don't ever have to look back."
            if not node:
                return 0
            
            count_good = 0
            if node.val >= curmax:
                curmax = node.val
                count_good = 1
            
            # Add the results from left and right subtrees
            return count_good + dfs(node.left, curmax) + dfs(node.right, curmax)


        return dfs(root, root.val) # or dfs(root, -float('inf'))
        # 3 => curmax = 3, node=3, return 1+(1+0)+(1+0+1)
        # [3]