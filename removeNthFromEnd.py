class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def removeNthFromEnd(self, head, n):
    if not head:
        return None
    if not head.next and n == 1:
        return None
    r = []
    current = head
    while current:
        r.append(current)
        current = current.next
    r.pop(len(r)-n)
    node = r[0]
    r[0].next = None
    r[-1].next = None
    d = node
    for i in range(1, len(r)):
        d.next = r[i]
        d = d.next
    return node
    
