class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def swapPairs(self, head):
    if not head:
        return None
    l = 1
    k = []
    current = head
    while current:
        if l % 2 != 0:
            k.append(current)
        else:
            k.insert(len(k) - 1, current)
        current = current.next
        l += 1
    node = k[0]
    k[-1].next = None
    d = node
    for i in range(1, len(k)):
        d.next = k[i]
        d = d.next
    return node
    
