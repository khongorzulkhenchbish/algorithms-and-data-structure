# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # O(n) time, O(n) space
        if not root:
            return []

        # using deque() enables popleft()
        q = deque()
        q.append(root)
        answer = []
 
        # BFS - Level Order Traversal
        while(q):
            n = len(q)
            rightMost = None
            # 2. at each level, mark the right most from child node's values
            for _ in range(n):
                node = q.popleft()  # usual pop() will pop from the right and cause wrong answer
                
                rightMost=node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            # current level ends, update the answer
            if rightMost != None:   # avoid rightMost being missed with 0 in simple check
                answer.append(rightMost)
        
        # 3. stop when we reach the bottom of the tree
        return answer