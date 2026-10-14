import sys
from typing import List


class OptimalMergeSolver:

    def solve(self, n: int, a: List[int]) -> None:
        """Находит минимальную стоимость объединения фрагментов в один."""
        if n == 1:
            sys.stdout.write("0\n")
            return

        inf: int = float("inf")
        dp: List[List[int]] = [[0] * n for _ in range(n)]
        pref: List[int] = [0] * (n + 1)

        for i in range(n):
            pref[i + 1] = pref[i] + a[i]

        def get_sum(i: int, j: int) -> int:
            return pref[j + 1] - pref[i]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j: int = i + length - 1
                dp[i][j] = inf
                s_val: int = get_sum(i, j)
                for k in range(i, j):
                    cost: int = dp[i][k] + dp[k + 1][j] + s_val
                    if cost < dp[i][j]:
                        dp[i][j] = cost

        sys.stdout.write(str(dp[0][n - 1]) + "\n")


line1 = sys.stdin.buffer.readline()
if line1:
    n = int(line1)
    line2 = sys.stdin.buffer.readline()
    if line2:
        a_arr = list(map(int, line2.split()))
        OptimalMergeSolver().solve(n, a_arr)