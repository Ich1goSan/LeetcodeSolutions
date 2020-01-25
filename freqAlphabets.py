def freqAlphabets(self, s: str) -> str:
    result = ''
    s = s[::-1]
    i = 0
    while i != len(s):
        if s[i] == '#':
            k = s[i+1:i+3][::-1]
            result += chr(int(k)+96)
            i = i + 3
        else:
            result += chr(int(s[i])+96)
            i += 1
    return result[::-1]
