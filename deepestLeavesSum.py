class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
def deepestLeavesSum(self, root):
    maxD = [0]
    sumD = [0]
    self.find(root, maxD, sumD, 1)
    return sumD[0]

def find(self, root, maxD, sumD, currentD):
    if not root:
        return
    if not root.left and not root.right:
        if maxD[0] == currentD:
            sumD[0] += root.val
            return
        if currentD < maxD[0]:
            return
        else:
            sumD[0] = root.val
            maxD[0] = currentD
            return
    self.find(root.left, maxD, sumD, currentD+1)
    self.find(root.right, maxD, sumD, currentD+1)
    return

