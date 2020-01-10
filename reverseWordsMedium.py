def reverseWords(self, s: str) -> str:
    return ' '.join(reversed(s.lstrip().rstrip().split()))