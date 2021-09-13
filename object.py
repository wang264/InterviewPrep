class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


node = ListNode(10, next=None)

prev = ListNode(0, next=node)
