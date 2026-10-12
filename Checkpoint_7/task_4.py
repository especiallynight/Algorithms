import heapq
import sys


class CouponRouter:

    def solve(
        self, n: int, s: int, t: int, adj: list[list[tuple[int, int]]]
    ) -> None:
        """Кратчайший путь с возможностью один раз применить скидку /2."""
        inf = float("inf")
        dist = [[inf] * 2 for _ in range(n + 1)]
        dist[s][0] = 0
        pq = [(0, s, 0)]

        while pq:
            d, u, state = heapq.heappop(pq)
            if d > dist[u][state]:
                continue

            for v, w in adj[u]:
                if dist[u][state] + w < dist[v][state]:
                    dist[v][state] = dist[u][state] + w
                    heapq.heappush(pq, (dist[v][state], v, state))

                if state == 0:
                    cost_with_coupon = dist[u][0] + (w // 2)
                    if cost_with_coupon < dist[v][1]:
                        dist[v][1] = cost_with_coupon
                        heapq.heappush(pq, (dist[v][1], v, 1))

        ans = min(dist[t][0], dist[t][1])
        sys.stdout.write(f"{ans if ans != inf else -1}\n")


line1 = sys.stdin.buffer.readline()
if line1:
    n, m, s, t = map(int, line1.split())
    adj = [[] for _ in range(n + 1)]

    for _ in range(m):
        line = sys.stdin.buffer.readline()
        if not line:
            break
        u, v, w = map(int, line.split())
        adj[u].append((v, w))

    router = CouponRouter()
    router.solve(n, s, t, adj)