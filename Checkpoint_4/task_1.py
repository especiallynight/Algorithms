import sys
from collections import deque

def sum_tree() -> list[int] | None:
    first_line = sys.stdin.readline()
    if not first_line:
        return

    n = int(first_line.strip())
    if n == 0:
        return

    values = [0] * n
    left = [-1] * n
    right = [-1] * n

    for i in range(n):
        line = sys.stdin.readline()
        parts = list(map(int, line.split()))
        values[i] = parts[0]
        left[i] = parts[1]
        right[i] = parts[2]

    queue = deque([0])
    level_sums = []

    while queue:
        level_size = len(queue)
        current_level_sum = 0

        for _ in range(level_size):
            node = queue.popleft()
            current_level_sum += values[node]

            if left[node] != -1:
                queue.append(left[node])
            if right[node] != -1:
                queue.append(right[node])

        level_sums.append(current_level_sum)
    print(*(level_sums))

sum_tree()