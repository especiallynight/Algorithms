import sys


class BoundedPathSolver:

    def solve(
        self,
        n: int,
        m: int,
        s: int,
        t: int,
        k_limit: int,
        edges: list[tuple[int, int, int]],
    ) -> None:
        """Находит мин. стоимость маршрута длиной <= K и их количество."""
        MOD = 1_000_000_007
        inf = float("inf")

        dp = [inf] * (n + 1)
        ways = [0] * (n + 1)

        dp[s] = 0
        ways[s] = 1

        best_dist = inf
        total_ways = 0

        if s == t:
            best_dist = 0
            total_ways = 1

        for _ in range(k_limit):
            temp_dp = [inf] * (n + 1)
            temp_ways = [0] * (n + 1)

            for u, v, w in edges:
                if dp[u] == inf:
                    continue
                new_d = dp[u] + w
                if new_d < temp_dp[v]:
                    temp_dp[v] = new_d
                    temp_ways[v] = ways[u]
                elif new_d == temp_dp[v]:
                    temp_ways[v] = (temp_ways[v] + ways[u]) % MOD

            for i in range(1, n + 1):
                if temp_dp[i] < best_dist and i == t:
                    best_dist = temp_dp[i]
                    total_ways = temp_ways[i]
                elif temp_dp[i] == best_dist and i == t:
                    total_ways = (total_ways + temp_ways[i]) % MOD

                dp[i] = temp_dp[i]
                ways[i] = temp_ways[i]

        if best_dist == inf:
            sys.stdout.write("IMPOSSIBLE\n")
        else:
            sys.stdout.write(f"{best_dist} {total_ways % MOD}\n")


line1 = sys.stdin.buffer.readline()
if line1:
    n, m, s, t, k = map(int, line1.split())
    edges = []
    for _ in range(m):
        line = sys.stdin.buffer.readline()
        if not line:
            break
        u, v, w = map(int, line.split())
        edges.append((u, v, w))

    BoundedPathSolver().solve(n, m, s, t, k, edges)