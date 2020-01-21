def findPeakElement(self, nums: List[int]) -> int:
    l = 0
    r = len(nums) - 1
    while l < r:
        mid = l + (r-l)//2
        if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
            return mid
        elif nums[mid] < nums[mid+1]:
            l += 1
        else:
            r -= 1
    return l