# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        ''' The tree is not sorted, regular binary tree where each node has unique elements.
        Both start, dest guarenteed to exist, and start != dest.

        If we find the Lowest Common Ancestor between the start and dest nodes,
        then the problem transforms into finding the first unmatching char among their
        parent list. Once the different chars are found, we will know the separate
        paths it took.

        It will get simpler when we have to return the answer such that,
        reverse only the subtree paths that leads to start node.
        And adding the paths leads to dest node as it is.

        Together it will return the final answer.
        Edge case: one of them is the parent of the other.

        Time: O(2*N), Space: O(N)
        '''
        def dfs(node, path, target):
            if not node:
                return "" # False
            
            if node.val == target:
                return path
            
            # result could be on either side
            path.append("L")
            res = dfs(node.left, path, target)
            if res: return res

            path.pop()
            path.append("R")
            res = dfs(node.right, path, target)
            if res: return res

            path.pop()
            return ""

        start_path = dfs(root, [], startValue)
        dest_path = dfs(root, [], destValue)

        i = 0
        while i < min(len(start_path), len(dest_path)):
            if start_path[i] != dest_path[i]:
                break
            i += 1
        
        answer = ["U"] * len(start_path[i:]) + dest_path[i:]
        return "".join(answer)
