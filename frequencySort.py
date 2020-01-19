def frequencySort(self, s: str) -> str:
    m = {}
    for i in s:
        if i not in m:
            m[i] = 1
        else:
            m[i] += 1
    r = ""
    for i in sorted(m, key=m.get, reverse=True):
        r += i * m[i]
    return r