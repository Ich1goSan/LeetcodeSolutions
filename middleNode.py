def middleNode(self, head: ListNode) -> ListNode:
    current = head
    ln = 0
    while current:
        ln += 1
        current = current.next
    current = head
    ind = 0
    while current and ind != ln//2:
        ind += 1
        current = current.next
    return current
