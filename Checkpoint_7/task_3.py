import heapq
import sys


class HelpPointFinder:

    def solve(
        self,
        n: int,
        m: int,
        k: int,
        help_points: list[int],
        adj: list[list[tuple[int, int]]],
    ) -> None:
        """Находит ближайший пункт помощи для каждой вершины."""
        inf = float("inf")
        dist = [inf] * (n + 1)
        closest_node = [-1] * (n + 1)

        pq = []
        for p in help_points:
            dist[p] = 0
            closest_node[p] = p
            heapq.heappush(pq, (0, p, p))

        while pq:
            d, p_id, u = heapq.heappop(pq)

            if d > dist[u]:
                continue

            for v, w in adj[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    closest_node[v] = p_id
                    heapq.heappush(pq, (dist[v], p_id, v))
                elif dist[u] + w == dist[v]:
                    if p_id < closest_node[v]:
                        closest_node[v] = p_id
                        heapq.heappush(pq, (dist[v], p_id, v))

        output = []
        for i in range(1, n + 1):
            if closest_node[i] == -1:
                output.append("-1 -1")
            else:
                output.append(f"{closest_node[i]} {dist[i]}")
        sys.stdout.write("\n".join(output) + "\n")


line1 = sys.stdin.buffer.readline()
if line1:
    n, m, k = map(int, line1.split())

    line2 = sys.stdin.buffer.readline()
    help_points = list(map(int, line2.split()))

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        line = sys.stdin.buffer.readline()
        if not line:
            break
        u, v, w = map(int, line.split())
        adj[u].append((v, w))
        adj[v].append((u, w))

    finder = HelpPointFinder()
    finder.solve(n, m, k, help_points, adj)