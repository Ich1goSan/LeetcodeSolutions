def searchRange(self, nums, target):
    l = 0
    r = len(nums)
    first = len(nums)
    while l < r:
        mid = l + (r - l) // 2
        if nums[mid] >= target:
            first = mid
            r = mid
        elif nums[mid] < target:
            l = mid + 1
    left = 0
    right = len(nums)
    last = len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] >= target+1:
            last = mid
            right = mid
        elif nums[mid] < target+1:
            left = mid + 1
    if first <= last-1:
        return [first, last-1]
    return [-1, -1]
    
