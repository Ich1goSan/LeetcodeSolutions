def rotateRight(self, head, k):
    if not head:
        return None
    l = 0
    current = head
    while current:
        l += 1
        current = current.next
    d = k % l
    if d == 0:
        return head

    current = head

    for i in range(l-d-1):
        current = current.next
    temp = current.next
    current.next = None
    tmp = temp
    while tmp.next:
        tmp = tmp.next
    tmp.next = head
    return temp
    
