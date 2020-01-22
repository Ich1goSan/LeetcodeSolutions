def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
    l = 0
    r = mountain_arr.length() - 1

    savedItems = {}

    # memorize item that already retrieved
    def get(i):
        if i not in savedItems:
            savedItems[i] = mountain_arr.get(i)
        return savedItems[i]

    while l < r:
        mid = l + (r - l) // 2
        if get(mid) < get(mid+1):
            l = mid + 1
        else:
            r = mid

    # increase side
    left = 0
    right = l
    while left <= right:
        mid = left + (right - left) // 2
        val = get(mid)
        if val == target:
            return mid
        if val < target:
            left = mid + 1
        else:
            right = mid - 1

    left = l
    right = mountain_arr.length() - 1

    # decrease side
    while left <= right:
        mid = left + (right - left) // 2
        val = get(mid)
        if val == target:
            return mid
        if val < target:
            right = mid - 1
        else:
            left = mid + 1
    return -1
