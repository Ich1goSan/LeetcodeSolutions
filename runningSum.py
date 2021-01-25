def runningSum(self, nums):
    currentSum = nums[0]
    for i in range(1, len(nums)):
        currentSum += nums[i]
        nums[i] = currentSum
    return nums
    