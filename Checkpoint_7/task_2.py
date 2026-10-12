import sys


class BellmanFordSolver:
    def solve(self, n: int, m: int, s: int, edges: list[tuple[int, int, int]]) -> None:
        """Находит кратчайшие пути в графе с отрицательными весами ребер."""
        inf = float('inf')
        distances = [inf] * (n + 1)
        distances[s] = 0

        for _ in range(n - 1):
            changed = False
            for u, v, w in edges:
                if distances[u] != inf and distances[u] + w < distances[v]:
                    distances[v] = distances[u] + w
                    changed = True
            if not changed:
                break

        results = [str(d) if d != inf else "INF" for d in distances[1:]]
        sys.stdout.write(" ".join(results) + "\n")


line = sys.stdin.buffer.readline()
if line:
    n, m, s = map(int, line.split())
    edges = []
    for _ in range(m):
        u, v, w = map(int, sys.stdin.buffer.readline().split())
        edges.append((u, v, w))

    solver = BellmanFordSolver()
    solver.solve(n, m, s, edges)