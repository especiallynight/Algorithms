import sys
from typing import List


class TreeKnapsackSolver:

    def solve(self, n: int, k: int, v: List[int], edges: List[List[int]]) -> None:
        adj: List[List[int]] = [[] for _ in range(n + 1)]
        for u, w in edges:
            adj[u].append(w)
            adj[w].append(u)

        dp: List[List[int]] = [[-float("inf")] * (k + 1) for _ in range(n + 1)]

        def dfs(curr: int, parent: int) -> None:
            dp[curr][1] = v[curr - 1]

            for neighbor in adj[curr]:
                if neighbor != parent:
                    dfs(neighbor, curr)
                    for sz in range(k, 0, -1):
                        for sub_sz in range(1, sz):
                            if dp[curr][sz - sub_sz] != -float("inf") and dp[neighbor][sub_sz] != -float("inf"):
                                val = dp[curr][sz - sub_sz] + dp[neighbor][sub_sz]
                                if val > dp[curr][sz]:
                                    dp[curr][sz] = val

        dfs(1, 0)
        max_val: int = max(dp[i][k] for i in range(1, n + 1))
        sys.stdout.write(str(max_val) + "\n")


line1 = sys.stdin.buffer.readline()
if line1:
    n, k = map(int, line1.split())
    line2 = sys.stdin.buffer.readline()
    v_vals = list(map(int, line2.split()))
    tree_edges: List[List[int]] = []
    for _ in range(n - 1):
        line = sys.stdin.buffer.readline()
        if not line:
            break
        u, w = map(int, line.split())
        tree_edges.append([u, w])
    TreeKnapsackSolver().solve(n, k, v_vals, tree_edges)