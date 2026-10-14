import sys
from typing import List, Tuple


class TreeMaxIndependentSet:

    def solve(self, n: int, v: List[int], edges: List[Tuple[int, int]]) -> None:
        """Находит максимальную ценность независимого множества на дереве."""
        sys.setrecursionlimit(300005)
        adj: List[List[int]] = [[] for _ in range(n + 1)]
        for u, w in edges:
            adj[u].append(w)
            adj[w].append(u)

        def dfs(curr: int, parent: int) -> Tuple[int, int]:
            include_val: int = v[curr - 1]
            exclude_val: int = 0

            for neighbor in adj[curr]:
                if neighbor != parent:
                    child_inc, child_exc = dfs(neighbor, curr)
                    include_val += child_exc
                    exclude_val += max(child_inc, child_exc)

            return include_val, exclude_val

        inc, exc = dfs(1, 0)
        sys.stdout.write(str(max(inc, exc)) + "\n")


line1 = sys.stdin.buffer.readline()
if line1:
    n = int(line1)
    line2 = sys.stdin.buffer.readline()
    v_vals = list(map(int, line2.split()))
    tree_edges: List[Tuple[int, int]] = []
    for _ in range(n - 1):
        line = sys.stdin.buffer.readline()
        if not line:
            break
        u, w = map(int, line.split())
        tree_edges.append((u, w))
    TreeMaxIndependentSet().solve(n, v_vals, tree_edges)