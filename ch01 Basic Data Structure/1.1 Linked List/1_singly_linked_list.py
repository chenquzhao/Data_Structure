class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def reverse(self, head):
        newHead = None
        while head:
            # head delete for old linked list
            node = head
            head = head.next

            # head insert for new linked list
            node.next = newHead
            newHead = node
        return newHead
