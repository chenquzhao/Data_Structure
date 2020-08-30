class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2
node2.next = node3

# dummy node: designed to delete head node
dummy = ListNode(None)
dummy.next = node1

prev = dummy
head = node1
while head:
    if head.val == 1:
        prev.next = head.next
        break
    prev = prev.next
    head = head.next

# return dummy -> next
head = dummy.next
while head:
    print(head.val)
    head = head.next
