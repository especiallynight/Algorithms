import sys


class CycleDetector:

    def solve(
        self, n: int, m: int, s: int, edges: list[tuple[int, int, int]]
    ) -> None:
        """Определяет достижимость и наличие бесконечно уменьшающихся путей."""
        inf = float("inf")
        dist = [inf] * (n + 1)
        dist[s] = 0

        for i in range(n):
            for u, v, w in edges:
                if dist[u] != inf and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    if i == n - 1:

                        dist[v] = -inf

        for _ in range(n):
            for u, v, w in edges:
                if dist[u] == -inf and dist[v] != -inf:
                    dist[v] = -inf

        output = []
        for i in range(1, n + 1):
            if dist[i] == inf:
                output.append("*")
            elif dist[i] == -inf:
                output.append("-")
            else:
                output.append(str(dist[i]))
        sys.stdout.write("\n".join(output) + "\n")


line1 = sys.stdin.buffer.readline()
if line1:
    n, m, s = map(int, line1.split())
    edges = []
    for _ in range(m):
        line = sys.stdin.buffer.readline()
        if not line:
            break
        u, v, w = map(int, line.split())
        edges.append((u, v, w))

    CycleDetector().solve(n, m, s, edges)