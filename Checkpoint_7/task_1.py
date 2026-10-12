import sys
import heapq


class DijkstraSolver:
    def solve(self, n: int, m: int, s: int, adj: list[list[tuple[int, int]]]) -> None:
        """Находит кратчайшие пути от вершины s с использованием кучи."""
        inf = float('inf')
        distances = [inf] * (n + 1)
        distances[s] = 0

        pq = [(0, s)]

        while pq:
            d, u = heapq.heappop(pq)

            if d > distances[u]:
                continue

            for v, w in adj[u]:
                if distances[u] + w < distances[v]:
                    distances[v] = distances[u] + w
                    heapq.heappush(pq, (distances[v], v))

        results = [str(d) if d != inf else "INF" for d in distances[1:]]
        sys.stdout.write(" ".join(results) + "\n")


line = sys.stdin.buffer.readline()
if line:
    n, m, s = map(int, line.split())
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, sys.stdin.buffer.readline().split())
        adj[u].append((v, w))

    solver = DijkstraSolver()
    solver.solve(n, m, s, adj)