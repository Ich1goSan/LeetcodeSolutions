def findUnsortedSubarray(self, nums: List[int]) -> int:
    sortedN = sorted(nums)
    if nums == sortedN:
        return 0

    l = 0
    r = len(nums) - 1

    while nums[l] == sortedN[l]:
        l += 1
    while nums[r] == sortedN[r]:
        r -= 1

    return r - l + 1
