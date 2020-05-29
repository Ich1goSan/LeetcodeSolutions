def groupThePeople(self, groupSizes):
    m = {}
    for i, x in enumerate(groupSizes):
        if x not in m:
            m[x] = [i]
        else:
            m[x].append(i)
    r = []
    for i in m:
        while i < len(m[i]):
            r.append(m[i][:i])
            m[i] = m[i][i:]
        r.append(m[i])
    return r
    
