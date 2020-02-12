def calPoints(self, ops):
    stack = []
    for i in range(len(ops)):
        if ops[i] == 'C':
            stack.pop()
        elif ops[i] == 'D':
            l = stack.pop()
            stack.append(l)
            stack.append(l * 2)
        elif ops[i] == '+':
            stack.append(sum(stack[-2:]))
        else:
            stack.append(int(ops[i]))
    return sum(stack)
    
