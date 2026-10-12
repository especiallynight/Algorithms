import sys


class CompatibilityChecker:

    def __init__(self, n: int) -> None:
        """DSU с 2N вершинами для проверки непротиворечивости условий (2-SAT)."""
        self.parent = list(range(2 * n + 1))
        self.n = n

    def find(self, i: int) -> int:
        """Поиск корня элемента с сжатием путей."""
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int) -> None:
        """Объединение двух множеств."""
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j

    def process_query(self, u: int, v: int, r: int) -> bool:
        """Обработка одного утверждения и проверка на противоречие."""
        if r == 0:
            self.union(u, v)
            self.union(u + self.n, v + self.n)
        else:
            self.union(u, v + self.n)
            self.union(v, u + self.n)

        return self.find(u) != self.find(u + self.n)


sys.setrecursionlimit(400005)
line1 = sys.stdin.buffer.readline()
if line1:
    n, q = map(int, line1.split())
    checker = CompatibilityChecker(n)
    is_failed = False
    results = []

    for _ in range(q):
        line = sys.stdin.buffer.readline()
        if not line:
            break
        u, v, r = map(int, line.split())
        if is_failed:
            results.append("NO")
        else:
            if not checker.process_query(u, v, r):
                is_failed = True
                results.append("NO")
            else:
                results.append("YES")
    sys.stdout.write("\n".join(results) + "\n")