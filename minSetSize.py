def minSetSize(self, arr):
    l = len(arr)
    m = {}
    for i in arr:
        if i not in m:
            m[i] = 1
        else:
            m[i] += 1
    c = 0
    lst = {k: v for k, v in sorted(
        m.items(), key=lambda item: item[1], reverse=True)}
    while l > len(arr)//2:
        current = next(iter(lst))
        l -= lst[current]
        del lst[current]
        c += 1
    return c
    
