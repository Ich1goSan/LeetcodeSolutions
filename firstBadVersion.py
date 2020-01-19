def firstBadVersion(self, n):
    l = 1
    r = n
    while l < r:
        mid = l + (r-l) // 2
        if not isBadVersion(mid):
            l = mid + 1
        else:
            r = mid     
    return l