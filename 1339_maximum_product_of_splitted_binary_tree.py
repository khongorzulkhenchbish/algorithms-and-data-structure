# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        """ The intuition is to understand that by the cutting of the edges,
        we are separating the tree into 3 types of independent shapes.
        1. The node is leaf and separated itself. Sum = 0
        2. The node has 1 or 2 children and separated from the root with its children.
        Separated tree. Subtree sum be enough to find.
        The main idea is the find all possible subtree sums that it could later calculate the
        max prod by subsum * (total - subsum)

        root = [1,2,3,4,5,6] => possible splits would make sums [4, 5, 6, 11, 9, 21]
        1. find tree sum = X (21) => (21-6) * 6
                                  => (21-5) * 5
                                  => (21-subtree_sum(4)) * subtree_sum(4) = 6 * 15
        Time: O(N) Space: O(N)
        """
        allsum = []

        def subtreesum(node):
            if not node:
                return 0
            
            leftSum = subtreesum(node.left)
            rightSum = subtreesum(node.right)
            subtree = node.val + leftSum + rightSum

            # if the node is leaf, or has just 1 children, then the subtree sum will be
            # just sum of the node values.
            allsum.append(subtree)
            return subtree

        # returns the sum of original tree
        total = subtreesum(root)
        
        maxprod = 0
        for s in allsum:
            maxprod = max( maxprod, (total-s) * s )

        return maxprod % (10**9+7)