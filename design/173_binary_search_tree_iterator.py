# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    # Optimal Approach: Time: O(N), Space: O(H) due to the stack changing 
    def __init__(self, root: Optional[TreeNode]):
        # store the nodes to be processed next
        self.stack = []
        # add all the possible left nodes
        while root:
            self.stack.append(root)
            root = root.left


    def next(self) -> int:
        # we pop the leftmost child
        # but before, we check if it has right child, if so, we will add that to the stack
        # when we add, we have to add only the left/smallest ones one by one
        # and on the way back (by popping), we will check their right child values
        nxt = self.stack.pop()
        cur = nxt.right
        while cur:
            self.stack.append(cur)
            cur = cur.left
        return nxt.val
        

    def hasNext(self) -> bool:
        return self.stack != []
    """
      7     
     / \
    3  15
      /  \
     9    20
    
    stack = [7, 3]
    next => 3, stack=[7]
    next => 7, stack=[15, 9]
    hasNext => True
    next => 9, stack=[15]
    hasNext => True
    next => 15, stack=[20]
    next => 20
    hasNext False
    """

    # Approach 1: time: O(N), space: O(N) 
    # def __init__(self, root: Optional[TreeNode]):
    #     self.bitree = [-inf]
    #     self.index = 0

    #     def traverse(node):
    #         if not node: # leaf node
    #             return
            
    #         tmplist = []
    #         if node.left:
    #             tmplist += traverse(node.left)
    #         tmplist += [node.val]
    #         if node.right:
    #             tmplist += traverse(node.right)

    #         return tmplist

    #     self.bitree += traverse(root)
    #     self.length = len(self.bitree)


    # def next(self) -> int:
    #     self.index += 1
    #     return self.bitree[self.index]

    # def hasNext(self) -> bool:
    #     return self.index+1 < self.length


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()