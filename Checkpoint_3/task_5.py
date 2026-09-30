from collections import deque

def min_steps_to_reach_target(grid: list[str]) -> int:
    n = len(grid)
    m = len(grid[0])

    start_r = start_c = -1
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'S':
                start_r, start_c = i, j
                break
        if start_r != -1:
            break

    queue = deque([(start_r, start_c, 0, 0)])

    visited = [[[False] * 1024 for _ in range(m)] for _ in range(n)]
    visited[start_r][start_c][0] = True

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        r, c, mask, dist = queue.popleft()

        if grid[r][c] == 'T':
            return dist

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < n and 0 <= nc < m:
                cell = grid[nr][nc]

                if cell == '#':
                    continue

                new_mask = mask

                if 'a' <= cell <= 'j':
                    key_bit = ord(cell) - ord('a')
                    new_mask |= (1 << key_bit)

                elif 'A' <= cell <= 'J':
                    door_bit = ord(cell) - ord('A')
                    if not (mask & (1 << door_bit)):
                        continue

                if not visited[nr][nc][new_mask]:
                    visited[nr][nc][new_mask] = True
                    queue.append((nr, nc, new_mask, dist + 1))

    return -1

grid = [
    "S.a.#",
    "###.A",
    "T...#"
]

print(min_steps_to_reach_target(grid))