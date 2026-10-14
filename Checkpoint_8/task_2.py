import sys


class KnapsackSolver:
    def solve(self, n: int, w_limit: int, items: list[tuple[int, int]]) -> None:
        """Решает классическую задачу о рюкзаке 0/1."""
        dp = [0] * (w_limit + 1)

        for weight, value in items:
            for j in range(w_limit, weight - 1, -1):
                if dp[j - weight] + value > dp[j]:
                    dp[j] = dp[j - weight] + value

        sys.stdout.write(f"{max(dp)}\n")


line = sys.stdin.buffer.readline()
if line:
    n, w_limit = map(int, line.split())
    items = []
    for _ in range(n):
        items.append(tuple(map(int, sys.stdin.buffer.readline().split())))
    KnapsackSolver().solve(n, w_limit, items)