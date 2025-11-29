if root:
    return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) 
else:
    return []

