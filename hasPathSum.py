def hasPathSum(self, root, sum):
    def binaryTreeSumPaths(root):
        if not root:
            return []
        result = []
        dfs(root, 0, result)
        return result

    def dfs(root, l, res):
        if root.left == None and root.right == None:
            res.append(root.val+l)
        if root.left:
            dfs(root.left, root.val+l, res)
        if root.right:
            dfs(root.right, root.val+l, res)
    pathSums = binaryTreeSumPaths(root)
    return sum in pathSums
