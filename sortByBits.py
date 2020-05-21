from functools import cmp_to_key

def sortByBits(self, arr):
    arr.sort(key=cmp_to_key(self.compare))
    return arr

def compare(self, x, y):
    xBin = str(bin(x)[2:])
    yBin = str(bin(y)[2:])
    xCount = xBin.count('1')
    yCount = yBin.count('1')
    if xCount == yCount:
        return 1 if x > y else -1
    return 1 if xCount > yCount else -1
    
