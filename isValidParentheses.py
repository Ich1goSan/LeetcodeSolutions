def isValid(self, s):
    l = '({['
    r = ')}]'
    stack = []
    for i in s:
        if i in l:
            stack.append(i)
        elif i in r:
            if len(stack) == 0:
                return False
            if r.index(i) != l.index(stack.pop()):
                return False
    return len(stack) == 0
    
