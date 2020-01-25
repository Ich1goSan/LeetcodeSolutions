def sumZero(self, n: int) -> List[int]:
    r = []
    for i in range(1, n//2 + 1):
        r.append(i)
        r.append(-i)
    if n % 2 != 0:
        r.append(0)
    return r
