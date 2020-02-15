def deleteDuplicates(self, head):
    if not head:
        return None
    m = {}
    current = head
    while current:
        if current.val not in m:
            m[current.val] = 1
        else:
            m[current.val] += 1
        current = current.next
    distinct = [i for i in m if m[i] == 1]
    if len(distinct) > 0:
        node = ListNode(distinct[0])
        x = node
        for i in range(1, len(distinct)):
            x.next = ListNode(distinct[i])
            x = x.next
        return node
    return None
