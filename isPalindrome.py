def isPalindrome(self, x: int) -> bool:
    x = str(x)
    for i in range(len(x)):
        if x[i] != x[len(x)-1-i]:
            return False
    return True