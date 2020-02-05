def addTwoNumbers(self, l1, l2):
    num1 = ''
    num2 = ''
    while l1:
        num1 = str(l1.val) + num1
        l1 = l1.next
    while l2:
        num2 = str(l2.val) + num2
        l2 = l2.next
    outStr = str(int(num1) + int(num2))
    node = ListNode(int(outStr[-1]))
    current = node
    for i in range(len(outStr)-2, -1, -1):
        newNode = ListNode(int(outStr[i]))
        current.next = newNode
        current = current.next
    return node
