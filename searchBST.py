def searchBST(self, root, val):
    if root.val == val:
        return root
    elif val > root.val and root.right:
        return self.searchBST(root.right, val)
    elif val < root.val and root.left:
        return self.searchBST(root.left, val)
    return None
    