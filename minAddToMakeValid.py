def minAddToMakeValid(self, S):
    l = '('
    r = ')'
    stack = []
    c = 0
    for i in S:
        if i in l:
            stack.append(i)
        elif i in r:
            if len(stack) == 0:
                c += 1
            elif r.index(i) != l.index(stack.pop()):
                c += 1
    return c + len(stack)
    
