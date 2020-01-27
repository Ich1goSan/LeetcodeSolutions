class MyCircularQueue:

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.q = [None] * (k+1)
        self.front, self.rear = -1, -1

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        elif self.isEmpty():
            self.front, self.rear = 0, 0
        else:
            self.rear = (self.rear + 1) % self.size()

        self.q[self.rear] = value
        
        return True

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        if self.front == self.rear:
            self.front, self.rear = -1, -1
        else:
            self.front = (self.front + 1) % self.size()
        return True

    def Front(self):
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1
        
        item = self.q[self.front]
        
        return item

    def Rear(self):
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1
        
        item = self.q[self.rear]
        
        return item

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        """
        return self.front == -1 and self.rear == -1

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        """
        return (self.rear + 1) % self.size() == self.front
    
    def size(self):
        return len(self.q) - 1
