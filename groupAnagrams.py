def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    m = {}
    for i, x in enumerate(strs):
        x = ''.join(sorted(x))
        if x not in m:
            m[x] = [i]
        else:
            m[x].append(i)
    result = []
    for i in m.values():
        words = []
        for ind in i:
            words.append(strs[ind])
        result.append(words)
    return result