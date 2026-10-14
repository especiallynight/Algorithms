import sys
from typing import List


class SCSSolver:
    def solve(self, s: str, t: str) -> None:
        """Находит лексикографически наименьшую кратчайшую общую суперпоследовательность."""
        n: int = len(s)
        m: int = len(t)

        dp: List[List[int]] = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n, -1, -1):
            dp[i][m] = n - i
        for j in range(m, -1, -1):
            dp[n][j] = m - j

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j + 1])

        res: List[str] = []
        i: int = 0
        j: int = 0

        while i < n and j < m:
            if s[i] == t[j]:
                res.append(s[i])
                i += 1
                j += 1
            elif dp[i + 1][j] < dp[i][j + 1]:
                res.append(s[i])
                i += 1
            elif dp[i + 1][j] > dp[i][j + 1]:
                res.append(t[j])
                j += 1
            else:
                if s[i] < t[j]:
                    res.append(s[i])
                    i += 1
                else:
                    res.append(t[j])
                    j += 1

        while i < n:
            res.append(s[i])
            i += 1

        while j < m:
            res.append(t[j])
            j += 1

        sys.stdout.write("".join(res) + "\n")


s_input: str = sys.stdin.readline().strip()
t_input: str = sys.stdin.readline().strip()

if s_input is not None and t_input is not None:
    solver: SCSSolver = SCSSolver()
    solver.solve(s_input, t_input)