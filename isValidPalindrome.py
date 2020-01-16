def isValidPalindrome(self, s: str) -> bool:
    x = ""
    for i in s:
        if i.isalnum():
            x+=i.lower()
    return x == x[::-1]