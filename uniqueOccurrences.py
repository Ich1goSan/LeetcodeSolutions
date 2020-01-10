def uniqueOccurrences(self, arr: List[int]) -> bool:
    m = {}
    for i in arr:
        if i in m:
            m[i] += 1
        else:
            m[i] = 1
    return len(m.values()) == len(set(m.values()))