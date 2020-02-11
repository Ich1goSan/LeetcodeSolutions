def binaryTreePaths(self, root):
    if not root:
        return []
    result = []
    self.dfs(root, "", result)
    return result


def dfs(self, root, l, res):
    if root.left == None and root.right == None:
        res.append(l + str(root.val))
    if root.left:
        self.dfs(root.left, l+str(root.val)+'->', res)
    if root.right:
        self.dfs(root.right, l+str(root.val)+'->', res)
        
