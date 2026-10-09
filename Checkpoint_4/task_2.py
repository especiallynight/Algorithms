import sys
from collections import Counter

def get_top_k_frequent_elements(
    numbers: list[int], k: int) -> list[int]:

    frequency_map = Counter(numbers)

    ranked_numbers = sorted(
        frequency_map.keys(), key=lambda num: (-frequency_map[num], num)
    )

    return ranked_numbers[:k]

def run_frequent_numbers_task() -> None:
    first_line = sys.stdin.readline()
    if not first_line:
        return

    n, k = map(int, first_line.split())

    second_line = sys.stdin.readline()
    sequence = list(map(int, second_line.split()))

    result = get_top_k_frequent_elements(sequence, k)
    print(*result)

run_frequent_numbers_task()