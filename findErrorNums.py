def findErrorNums(self, nums: List[int]) -> List[int]:
    nums.sort()
    n = len(nums)
    sumA = n * (n+1) // 2
    sumArr = sum(nums)
    diff = sumA - sumArr
    for i in range(len(nums)-1):
        if(nums[i] >= nums[i+1]):
            return [nums[i], nums[i]+diff]