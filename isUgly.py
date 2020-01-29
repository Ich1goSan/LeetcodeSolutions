def isUgly(self, num):
    if num == 0:
        return False

    while True:
        if num % 2 == 0:
            num = num // 2
        else:
            break
    while True:
        if num % 3 == 0:
            num = num // 3
        else:
            break

    while True:
        if num % 5 == 0:
            num = num // 5
        else:
            break

    if num == 1:
        return True

    return False
