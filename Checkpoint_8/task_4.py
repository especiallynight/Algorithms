import sys


class ExactWeightKnapsack:
    def solve(self, n: int, capacity: int, items: list[tuple[int, int]]) -> None:
        """Максимизирует прибыль и минимизирует количество грузов для веса C."""
        inf = float('inf')
        dp_profit = [-1] * (capacity + 1)
        dp_count = [inf] * (capacity + 1)
        dp_profit[0] = 0
        dp_count[0] = 0

        for w, p in items:
            for j in range(w, capacity + 1):
                if dp_profit[j - w] != -1:
                    new_profit = dp_profit[j - w] + p
                    new_count = dp_count[j - w] + 1
                    if new_profit > dp_profit[j]:
                        dp_profit[j] = new_profit
                        dp_count[j] = new_count
                    elif new_profit == dp_profit[j]:
                        if new_count < dp_count[j]:
                            dp_count[j] = new_count

        if dp_profit[capacity] == -1:
            sys.stdout.write("-1\n")
        else:
            sys.stdout.write(f"{dp_profit[capacity]} {dp_count[capacity]}\n")


line = sys.stdin.buffer.readline()
if line:
    n, c = map(int, line.split())
    items = [tuple(map(int, sys.stdin.buffer.readline().split())) for _ in range(n)]
    ExactWeightKnapsack().solve(n, c, items)