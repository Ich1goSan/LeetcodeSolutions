def maxSubArray(self, nums):
    currentSum = nums[0]
    maxSum = nums[0]
    for i in range(1, len(nums)):
        currentSum = max(currentSum + nums[i], nums[i])
        maxSum = max(currentSum, maxSum)
    return maxSum
    
