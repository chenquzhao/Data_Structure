class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

node1.next = node2
node2.next = node3

prob = node1
while prob is not None:
    print(prob.val)
    prob = prob.next
