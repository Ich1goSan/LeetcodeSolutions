def reverseList(self, head: ListNode) -> ListNode:
    node = None
    while head:
        nextElem = head.next
        head.next = node
        node = head
        head = nextElem
    return node
