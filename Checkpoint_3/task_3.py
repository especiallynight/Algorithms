def has_cycle(next_node: list[int], start: int) -> bool:
    slow = fast = start

    while True:
        if slow == -1:
            return False
        slow = next_node[slow]

        for _ in range(2):
            if fast == -1:
                return False
            fast = next_node[fast]

        if slow == -1 or fast == -1:
            return False

        if slow == fast:
            return True


next_node = [0, 2, 3, 2]
start = 1

print("YES" if has_cycle(next_node, start) else "NO")