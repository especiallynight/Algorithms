import heapq
import sys


class AlienAlphabet:

    def find_order(self, n: int, k: int, words: list[str]) -> str:
        """Определяет порядок букв с помощью графа и топологической
        сортировки."""
        adj = [[] for _ in range(k)]
        in_degree = [0] * k
        nodes = set()
        for word in words:
            for char in word:
                nodes.add(ord(char) - ord("a"))

        for i in range(n - 1):
            w1, w2 = words[i], words[i + 1]
            length = min(len(w1), len(w2))
            found_diff = False
            for j in range(length):
                if w1[j] != w2[j]:
                    u, v = ord(w1[j]) - ord("a"), ord(w2[j]) - ord("a")
                    adj[u].append(v)
                    in_degree[v] += 1
                    found_diff = True
                    break
            if not found_diff and len(w1) > len(w2):
                return "IMPOSSIBLE"

        queue = [i for i in range(k) if in_degree[i] == 0]
        heapq.heapify(queue)

        res = []
        while queue:
            u = heapq.heappop(queue)
            res.append(chr(u + ord("a")))
            for v in adj[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    heapq.heappush(queue, v)

        return "".join(res) if len(res) == k else "IMPOSSIBLE"


line1 = sys.stdin.buffer.readline()
if line1:
    n, k = map(int, line1.split())
    words = []
    for _ in range(n):
        words.append(sys.stdin.buffer.readline().decode().strip())

    alien = AlienAlphabet()
    sys.stdout.write(alien.find_order(n, k, words) + "\n")