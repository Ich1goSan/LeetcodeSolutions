def isPalindromeLinkedList(self, head: ListNode) -> bool:
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr == arr[::-1]