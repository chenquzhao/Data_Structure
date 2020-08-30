class DListNode:
    def __init__(self, val):
        self.val = val
        self.prev = self.next = None

    def reverse(self, head):
        newHead = None
        while head:
            newHead = head
            head = head.next
            newHead.next = newHead.prev
            newHead.prev = head
        return newHead
