def findAndReplacePattern(self, words, pattern):
    result = []
    for i in words:
        if len(i) != len(pattern):
            continue
        if self.isMatch(i, pattern):
            result.append(i)
    return result


def isMatch(self, word, pattern):
    m = {}
    word = list(word)
    for i in range(len(pattern)):
        if pattern[i] in m:
            if m[pattern[i]] != word[i]:
                return False
        else:
            m[pattern[i]] = word[i]
    return len(set(m.values())) == len(m.values())
    
