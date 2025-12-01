from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Time: O(N) BFS can guarantee vertical order of the visits, even covering the third testcase
        where the [node -> leftChild.right -> rightChild.left]
        
        Space: O(N) mark the visited nodes in the Hashmap {col:[nodes]}
        3 => {0:[3]}    map={0:[3]}
        q = [[-1, 9], [1, 20]]
        pop [-1, 9] => process 9 => leaf node =>    map = {0:[3], -1:[9]}
        pop [1, 20] => process 20 => map = {0:[3], -1:[9], [1:[20]]}
                                    add to q => [0, 15], [2, 7] => leaf nodes
        at the end map = {-1:[9], 0:[3, 15], 1:[20], 2:[7]} => sort by key? => [[9],[3,15],[20],[7]]
        (it is easier if we maintain max, min value for range to avoid sorting time complexity it brings)
        """
        if not root:
            return []
        
        vert_map = defaultdict(list)  # returns [] if the key not assigned
        max_col = min_col = curr_col = 0
        q = deque()
        q.append([curr_col, root])  # should be double ended to pop the leftmost
        

        while q: # stops when q is empty
            qlen = len(q)
            for _ in range(qlen):
                curr_col, node = q.popleft()

                # if the key exist, it will add the val at the end of the existing list
                # if the key doesn't exist, it will add the value to [] empty list
                vert_map[curr_col].append(node.val)
                
                # the order is important here, end result order => "root.left, root, rootright"
                if node.left:
                    q.append([curr_col-1, node.left])
                    min_col = min(min_col, curr_col-1)

                if node.right:
                    q.append([curr_col+1, node.right])
                    max_col = max(max_col, curr_col+1)
        
        return [vert_map[col] for col in range(min_col, max_col+1)]