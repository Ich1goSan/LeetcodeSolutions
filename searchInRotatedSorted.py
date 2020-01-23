def search(self, nums: List[int], target: int) -> int:
    l = 0
    r = len(nums) - 1
    # finding pivot
    while l < r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > nums[r]:
            l = mid + 1
        else:
            r = mid
    left = 0
    right = l - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    left = l
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1