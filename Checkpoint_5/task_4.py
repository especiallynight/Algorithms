import sys


def count_queen_placements() -> None:
    """Подсчитывает допустимые расстановки ферзей."""
    first_line: bytes = sys.stdin.buffer.readline()
    if not first_line:
        return

    params: list[int] = [int(x) for x in first_line.split()]
    n: int = params[0]
    b: int = params[1]

    blocked: list[int] = [0] * n

    for _ in range(b):
        line: bytes = sys.stdin.buffer.readline()
        coords: list[int] = [int(x) for x in line.split()]
        r: int = coords[0] - 1
        c: int = coords[1] - 1
        blocked[r] |= 1 << c

    total: int = 0
    full_mask: int = (1 << n) - 1

    def backtrack(
        row: int,
        cols: int,
        diag1: int,
        diag2: int,
    ) -> None:
        nonlocal total

        if row == n:
            total += 1
            return

        available: int = (
            full_mask & ~(cols | diag1 | diag2 | blocked[row])
        )

        while available:
            position: int = available & -available
            available &= available - 1

            backtrack(
                row + 1,
                cols | position,
                (diag1 | position) << 1,
                (diag2 | position) >> 1,
            )

    backtrack(0, 0, 0, 0)
    sys.stdout.write(f"{total}\n")

count_queen_placements()