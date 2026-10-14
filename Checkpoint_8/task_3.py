import sys


class LCSSolver:
    def solve(self, s: str, t: str) -> None:
        """Находит длину наибольшей общей подпоследовательности."""
        n, m = len(s), len(t)
        dp = [0] * (m + 1)

        for i in range(1, n + 1):
            prev = 0
            for j in range(1, m + 1):
                temp = dp[j]
                if s[i - 1] == t[j - 1]:
                    dp[j] = prev + 1
                else:
                    dp[j] = max(dp[j], dp[j - 1])
                prev = temp

        sys.stdout.write(f"{dp[m]}\n")


s = sys.stdin.readline().strip()
t = sys.stdin.readline().strip()
if s and t:
    LCSSolver().solve(s, t)