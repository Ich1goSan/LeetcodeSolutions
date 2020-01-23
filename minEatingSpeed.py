def minEatingSpeed(self, piles: List[int], H: int) -> int:
    l = 1
    r = max(piles)
    while l <= r:
        mid = l + (r - l) // 2
        if self.canEat(piles, mid, H):
            r = mid - 1
        else:
            l = mid + 1
    return l

def canEat(self, piles, k, h):
    hours = 0
    for pile in piles:
        div = pile // k
        hours += div
        if pile % k != 0:
            hours += 1
    return hours <= h
