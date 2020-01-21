def peakIndexInMountainArray(self, A: List[int]) -> int:
    l = 0
    r = len(A) - 1
    while l < r:
        mid = l + (r-l)//2
        if A[mid] > A[mid+1] and A[mid] > A[mid-1]:
            return mid
        elif A[mid] > A[mid-1]:
            l += 1
        else:
            r -= 1
    return l