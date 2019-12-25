def getDecimalValue(self, head: ListNode) -> int:
        x = ""
        while(head):
            x+=str(head.val)
            head = head.next
        return int(x, 2)