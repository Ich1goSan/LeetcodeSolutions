def lengthOfLastWord(self, s: str) -> int:
    return len(s.split()[-1]) if any(c.isalpha() for c in s) else 0