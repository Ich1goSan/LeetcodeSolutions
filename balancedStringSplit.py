def balancedStringSplit(self, s: str) -> int:
        l, r = 0, 0
        c = 0
        for i in range(len(s)):
            if s[i] == "L":
                l += 1
            if s[i] == "R":
                r+=1
            if l == r:
               c+=1
        return c