class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = collections.deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.d.appendleft(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.d.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.d[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.d) == 0
        