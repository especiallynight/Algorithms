import sys


class RobotHopper:
    def solve(self, n: int, h: list[int]) -> None:
        """Находит минимальную стоимость пути робота до n-й платформы."""
        if n < 2:
            sys.stdout.write("0\n")
            return

        dp = [0] * n
        dp[1] = abs(h[1] - h[0])

        for i in range(2, n):
            cost1 = dp[i - 1] + abs(h[i] - h[i - 1])
            cost2 = dp[i - 2] + abs(h[i] - h[i - 2])
            dp[i] = min(cost1, cost2)

        sys.stdout.write(f"{dp[n - 1]}\n")


line1 = sys.stdin.buffer.readline()
if line1:
    n = int(line1)
    line2 = sys.stdin.buffer.readline()
    if line2:
        h = list(map(int, line2.split()))
        RobotHopper().solve(n, h)