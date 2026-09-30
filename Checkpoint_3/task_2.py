from collections import deque
def shortest_path(grid: list[str]) -> int:
    n = len(grid)
    m = len(grid[0])
    start = finish = None

    for r in range(n):
        for c in range(m):
            if grid[r][c] == 'S':
                start = (r, c)
            elif grid[r][c] == 'T':
                finish = (r, c)

    dist = [[-1] * m for _ in range(n)]
    dist[start[0]][start[1]] = 0

    queue = deque([start])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        r, c = queue.popleft()

        if (r, c) == finish:
            return dist[r][c]

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if not (0 <= nr < n and 0 <= nc < m):
                continue
            if grid[nr][nc] == '#' or dist[nr][nc] != -1:
                continue

            dist[nr][nc] = dist[r][c] + 1
            queue.append((nr, nc))

    return -1

grid = [
    "S..#",
    ".#..",
    "...T"
]
print(shortest_path(grid))