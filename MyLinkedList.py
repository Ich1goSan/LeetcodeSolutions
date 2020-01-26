class Node(object):

    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyLinkedList:

    def __init__(self):
        self.head = None
        
    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        current = self.head
        if not current:
            return -1
        ind = 0
        while ind != index:
            ind += 1
            if not current.next:
                return -1
            current = current.next
        return current.val


    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        node = Node(val)
        if self.head:
            current = self.head
            node.next = current
            self.head = node
        else:
            self.head = node
        

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        """
        node = Node(val)
        current = self.head
        if self.head:
            while current.next:
                current = current.next
        current.next = node  

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        ind = 0
        if ind == index:
            self.addAtHead(val)
            return
        element = Node(val)
        current = self.head
        while ind != index - 1:
            ind += 1
            if not current.next:
                return
            current = current.next
        element.next = current.next
        current.next = element
        

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        current = self.head
        if index < 0 or not current:
            return
        ind = 0

        if ind == index:
            self.head = self.head.next
            return

        while ind != index-1:
            ind += 1
            if not current.next:
                return
            current = current.next
        if current and current.next:
            current.next = current.next.next