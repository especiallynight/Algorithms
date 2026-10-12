import sys


class DisjointSetUnion:

    def __init__(self, n: int) -> None:
        """Инициализирует систему непересекающихся множеств."""
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)

    def find(self, i: int) -> int:
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int) -> None:
        """Объединяет два множества по рангу."""
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1


sys.setrecursionlimit(200005)
line = sys.stdin.buffer.readline()
if line:
    n, q = map(int, line.split())
    dsu = DisjointSetUnion(n)
    results = []

    for _ in range(q):
        parts = sys.stdin.buffer.readline().split()
        if not parts:
            break
        t, u, v = int(parts[0]), int(parts[1]), int(parts[2])
        if t == 1:
            dsu.union(u, v)
        else:
            results.append("YES" if dsu.find(u) == dsu.find(v) else "NO")

    sys.stdout.write("\n".join(results) + "\n")