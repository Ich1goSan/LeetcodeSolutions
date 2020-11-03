def isSymmetric(self, root):
    def isSymmetricNodes(fNode, sNode):
        if not fNode and not sNode:
            return True
        if fNode and sNode and fNode.val == sNode.val:
            return isSymmetricNodes(fNode.left, sNode.right) and isSymmetricNodes(fNode.right, sNode.left)
        return False
    return isSymmetricNodes(root, root)
