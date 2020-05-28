class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def constructMaximumBinaryTree(nums):
    if not nums:
        return None
    maxVal = nums[0]
    index = 0
    for i in range(1, len(nums)):
        if maxVal < nums[i]:
            maxVal = nums[i]
            index = i

    root = TreeNode(maxVal)
    root.left = constructMaximumBinaryTree(nums[:index])
    root.right = constructMaximumBinaryTree(nums[index+1:])
    return root
    
