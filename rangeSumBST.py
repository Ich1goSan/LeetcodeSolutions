def rangeSumBST(self, root, L, R):
    if root == None:
        return 0
    if root and root.val >= L and root.val <= R:
        return root.val + self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)
    else:
        return self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)
        
