def isDiv(self, i):
    isDiv = True
    for j in str(i):
        if j == '0' or i % int(j) != 0:
            isDiv = False
            break
    return isDiv

def selfDividingNumbers(self, left, right):
    arr = []
    for i in range(left, right+1):
        if self.isDiv(i):
            arr.append(i)
    return arr
    
