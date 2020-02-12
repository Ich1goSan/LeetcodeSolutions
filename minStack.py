class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []

    def push(self, x):
        if len(self.data) == 0:
            self.data.append((x, x))
        else:
            self.data.append((x, min(x, self.data[-1][1])))

    def pop(self):
        if self.data:
            self.data.pop()

    def top(self):
        if self.data:
            return self.data[-1][0]
        return None

    def getMin(self):
        if self.data:
            return self.data[-1][1]
        return None
        
