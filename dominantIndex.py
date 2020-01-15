def dominantIndex(self, nums: List[int]) -> int:
    if len(nums) == 1:
        return 0
    sortedNums = sorted(nums, reverse = True)
    if sortedNums[0] // 2 >= sortedNums[1]:
        return nums.index(sortedNums[0])
    return -1