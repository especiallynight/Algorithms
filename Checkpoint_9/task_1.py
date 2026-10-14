import sys
from typing import List


class PalindromePartitionSolver:

    def solve(self, s: str) -> None:
        """Находит минимальное количество палиндромных частей в строке."""
        n: int = len(s)
        is_pal: List[List[bool]] = [[False] * n for _ in range(n)]

        for i in range(n):
            is_pal[i][i] = True

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j: int = i + length - 1
                if s[i] == s[j]:
                    if length == 2 or is_pal[i + 1][j - 1]:
                        is_pal[i][j] = True

        dp: List[int] = [0] * n
        for i in range(n):
            if is_pal[0][i]:
                dp[i] = 1
            else:
                min_cuts: int = i + 1
                for j in range(i):
                    if is_pal[j + 1][i]:
                        if dp[j] + 1 < min_cuts:
                            min_cuts = dp[j] + 1
                dp[i] = min_cuts

        sys.stdout.write(str(dp[n - 1]) + "\n")


s_input: str = sys.stdin.readline().strip()
if s_input:
    PalindromePartitionSolver().solve(s_input)