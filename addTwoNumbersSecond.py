def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    s1, s2 = '', ''
    while l1:
        s1 += str(l1.val)
        l1 = l1.next
    while l2:
        s2 += str(l2.val)
        l2 = l2.next
    res = str(int(s1) + int(s2))
    newHead = ListNode(int(res[0]))
    current = newHead
    for i in range(1, len(res)):
        current.next = ListNode(int(res[i]))
        current = current.next
    return newHead
