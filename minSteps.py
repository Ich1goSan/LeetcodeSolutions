def minSteps(self, s, t):
    m1 = {}
    m2 = {}
    for i in s:
        if i not in m1:
            m1[i] = 1
        else:
            m1[i] += 1
    for i in t:
        if i not in m2:
            m2[i] = 1
        else:
            m2[i] += 1

    diff = 0

    for i in m2:
        if i in m1:
            diff += abs(m2[i] - m1[i])
            del m1[i]
        else:
            diff += m2[i]
    for i in m1:
        diff += m1[i]

    return diff//2
