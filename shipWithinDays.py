def shipWithinDays(self, weights: List[int], D: int) -> int:
    l = max(weights)
    r = sum(weights)
    while l < r:
        mid = (l + r) // 2
        if self.days(weights, mid) >= D:
            l = mid + 1
        else:
            r = mid
    return l


def days(self, weights, k):
    s = 0
    d = 0
    for i in weights:
        s += i
        if s > k:
            d += 1
            s = i
    return d
