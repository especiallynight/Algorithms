import sys


class ListNode:
    def __init__(self, val: int, next_node=None) -> None:
        self.val = val
        self.next = next_node


class LinkedListManager:
    def reverse(self, head: ListNode) -> ListNode:
        """Разворачивает связи между узлами списка."""
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev


line1 = sys.stdin.buffer.readline()
if line1:
    n = int(line1)
    line2 = sys.stdin.buffer.readline()
    if line2:
        values = list(map(int, line2.decode().split()))

        dummy = ListNode(0)
        curr = dummy
        for v in values:
            curr.next = ListNode(v)
            curr = curr.next

        manager = LinkedListManager()
        new_head = manager.reverse(dummy.next)

        results = []
        curr = new_head
        while curr:
            results.append(str(curr.val))
            curr = curr.next
        sys.stdout.write(" ".join(results) + "\n")