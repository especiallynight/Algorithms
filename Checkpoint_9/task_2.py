import sys
from typing import List


class GridPathsSolver:

    def solve(self, n: int, m: int, grid: List[str]) -> None:
        """Подсчитывает количество путей из (1,1) в (n,m) вправо и вниз по
        модулю."""
        MOD: int = 1_000_000_007

        if grid[0][0] == "#" or grid[n - 1][m - 1] == "#":
            sys.stdout.write("0\n")
            return

        dp: List[int] = [0] * m
        dp[0] = 1

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "#":
                    dp[j] = 0
                else:
                    if j > 0:
                        dp[j] = (dp[j] + dp[j - 1]) % MOD

        sys.stdout.write(str(dp[m - 1]) + "\n")


line1 = sys.stdin.buffer.readline()
if line1:
    n, m = map(int, line1.split())
    grid_rows: List[str] = []
    for _ in range(n):
        row_line = sys.stdin.buffer.readline()
        if not row_line:
            break
        grid_rows.append(row_line.decode().strip())
    GridPathsSolver().solve(n, m, grid_rows)