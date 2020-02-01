def mostCommonWord(self, paragraph, banned):
    lst = ''.join([i.lower() if i.isalpha() or i.isspace()
                   else " " for i in paragraph]).split()
    m = {}
    for i in lst:
        if i not in m:
            m[i] = 1
        else:
            m[i] += 1
    s = sorted(m, key=m.get, reverse=True)
    for i in banned:
        try:
            s.remove(i)
        except:
            continue
    return s[0]
