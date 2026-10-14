import sys
from typing import List


class GridKNegativesSolver:

    def solve(
        self, n: int, m: int, k: int, grid: List[List[int]]
    ) -> None:
        """Находит максимально возможную сумму на сетке с возможностью применения экрана к отрицательным клеткам не более k раз."""
        NEG_INF: int = -(10**30)

        dp: List[List[List[int]]] = [
            [[NEG_INF] * (k + 1) for _ in range(m)] for _ in range(n)
        ]

        start_val: int = grid[0][0]
        if start_val >= 0:
            dp[0][0][0] = start_val
        else:
            dp[0][0][0] = start_val
            if k >= 1:
                dp[0][0][1] = 0

        for i in range(n):
            for j in range(m):
                for use in range(k + 1):
                    cur: int = dp[i][j][use]
                    if cur == NEG_INF:
                        continue

                    if i + 1 < n:
                        nxt: int = grid[i + 1][j]
                        if cur + nxt > dp[i + 1][j][use]:
                            dp[i + 1][j][use] = cur + nxt
                        if nxt < 0 and use + 1 <= k:
                            if cur + 0 > dp[i + 1][j][use + 1]:
                                dp[i + 1][j][use + 1] = cur

                    if j + 1 < m:
                        nxt = grid[i][j + 1]
                        if cur + nxt > dp[i][j + 1][use]:
                            dp[i][j + 1][use] = cur + nxt
                        if nxt < 0 and use + 1 <= k:
                            if cur + 0 > dp[i][j + 1][use + 1]:
                                dp[i][j + 1][use + 1] = cur

        ans: int = max(dp[n - 1][m - 1])
        sys.stdout.write(str(ans) + "\n")


line1 = sys.stdin.buffer.readline()
if line1:
    n, m, k = map(int, line1.split())
    grid_matrix: List[List[int]] = []
    for _ in range(n):
        row_line = sys.stdin.buffer.readline()
        if not row_line:
            break
        grid_matrix.append(list(map(int, row_line.split())))
    GridKNegativesSolver().solve(n, m, k, grid_matrix)