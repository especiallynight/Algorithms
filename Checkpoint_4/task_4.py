import sys
sys.setrecursionlimit(300000)

def calculate_max_tree_path_sum(
    values: list[int], left: list[int], right: list[int], n: int
) -> int:
    """Вычисляет максимально возможную стоимость маршрута в бинарном дереве."""
    global_max_sum = float("-inf")

    def find_max_branch_gain(node_idx: int) -> int:
        nonlocal global_max_sum
        if node_idx == -1:
            return 0

        left_branch_gain = max(find_max_branch_gain(left[node_idx]), 0)
        right_branch_gain = max(find_max_branch_gain(right[node_idx]), 0)

        current_full_path_price = (
            values[node_idx] + left_branch_gain + right_branch_gain
        )

        global_max_sum = max(global_max_sum, current_full_path_price)

        return values[node_idx] + max(left_branch_gain, right_branch_gain)

    find_max_branch_gain(0)
    return int(global_max_sum)


def run_maximum_path_sum_task() -> None:
    first_line = sys.stdin.readline()
    if not first_line:
        return

    n = int(first_line.strip())
    if n == 0:
        print(0)
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

    max_sum = calculate_max_tree_path_sum(values, left, right, n)
    print(max_sum)

run_maximum_path_sum_task()
