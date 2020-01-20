def singleNonDuplicate(self, nums: List[int]) -> int:
    l, r = 0, len(nums)-1
    while l < r:
        mid = l + (r - l) // 2
        if mid % 2 == 0:
            if nums[mid] == nums[mid+1]:
                l = mid + 2
            else:
                r = mid
        else:
            if nums[mid] == nums[mid-1]:
                l = mid + 1
            else:
                r = mid - 1
    return nums[l]