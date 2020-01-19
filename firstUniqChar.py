def firstUniqChar(self, s: str) -> int:
    m = {}
    for i in s:
        if i not in m:
            m[i] = 1
        else:
            m[i] += 1
    for i, v in m.items():
        if v == 1:
            return s.index(i)
    return -1