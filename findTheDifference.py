def findTheDifference(self, s, t):
    t = list(t)
    for i in s:
        t.remove(i)
    return t[0]
