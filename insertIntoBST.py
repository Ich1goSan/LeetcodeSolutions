def insertIntoBST(self, root, val):
    if val < root.val:
        if root.left:
            self.insertIntoBST(root.left, val)
        else:
            root.left = TreeNode(val)
    elif val > root.val:
        if root.right:
            self.insertIntoBST(root.right, val)
        else:
            root.right = TreeNode(val)
    return root
    
