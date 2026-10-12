import heapq
import sys


class TaskScheduler:

    def solve(self, n: int, m: int, edges: list[list[int]]) -> str:
        """Топологическая сортировка с использованием алгоритма Кана и min-heap."""
        adj = [[] for _ in range(n + 1)]
        in_degree = [0] * (n + 1)
        for a, b in edges:
            adj[a].append(b)
            in_degree[b] += 1

        heap = [i for i in range(1, n + 1) if in_degree[i] == 0]
        heapq.heapify(heap)

        order = []
        while heap:
            curr = heapq.heappop(heap)
            order.append(str(curr))
            for neighbor in adj[curr]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    heapq.heappush(heap, neighbor)

        return " ".join(order) if len(order) == n else "-1"


line1 = sys.stdin.buffer.readline()
if line1:
    n, m = map(int, line1.split())
    edges = []
    for _ in range(m):
        line = sys.stdin.buffer.readline()
        if not line:
            break
        a, b = map(int, line.split())
        edges.append([a, b])

    scheduler = TaskScheduler()
    sys.stdout.write(scheduler.solve(n, m, edges) + "\n")