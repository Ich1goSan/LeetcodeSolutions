def getIntersectionNode(self, headA, headB):
    a = headA
    b = headB
    l1 = 0
    l2 = 0
    while a:
        l1 += 1
        a = a.next
    while b:
        l2 += 1
        b = b.next
    a = headA
    b = headB
    x = l2 > l1
    for i in range(abs(l2-l1)):
        if x:
            b = b.next
        else:
            a = a.next
    while a != b:
        a = a.next
        b = b.next
    return a

