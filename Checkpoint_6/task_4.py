import sys


class ListNode:

    def __init__(self, val: int, next_node=None) -> None:
        self.val = val
        self.next = next_node


class BlockReverser:

    def reverse_k_nodes(self, head: ListNode, k: int, n: int) -> ListNode:
        """Разворачивает узлы списка блоками по k элементов."""
        if k <= 1 or k > n:
            return head

        dummy = ListNode(0, head)
        prev_group_end = dummy
        curr = head

        for _ in range(n // k):
            group_start = curr
            prev = None
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            prev_group_end.next = prev
            group_start.next = curr
            prev_group_end = group_start

        return dummy.next


line1 = sys.stdin.buffer.readline()
if line1:
    n, k = map(int, line1.split())
    line2 = sys.stdin.buffer.readline()
    values = list(map(int, line2.decode().split()))

    dummy = ListNode(0)
    it = dummy
    for v in values:
        it.next = ListNode(v)
        it = it.next

    reverser = BlockReverser()
    new_head = reverser.reverse_k_nodes(dummy.next, k, n)

    res = []
    while new_head:
        res.append(str(new_head.val))
        new_head = new_head.next
    sys.stdout.write(" ".join(res) + "\n")