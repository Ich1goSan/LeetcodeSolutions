def getAllElements(self, root1, root2):
    arr1 = self.preorder(root1, [])
    arr2 = self.preorder(root2, [])
    return sorted(arr1 + arr2)

def preorder(self, root, result):
    if root:
        result.append(root.val)
        if root.left:
            self.preorder(root.left, result)
        if root.right:
            self.preorder(root.right, result)
    return result
    
