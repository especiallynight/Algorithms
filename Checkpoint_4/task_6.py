import sys
import heapq
from collections import defaultdict


def compute_sliding_window_medians(
    numbers: list[int], n: int, k: int
) -> list[float]:
    if k <= 0 or k > n or len(numbers) < n:
        raise ValueError("Должно выполняться 1 <= k <= n и len(numbers) >= n")

    left_max_heap = []   # Отрицательные значения для max-heap
    right_min_heap = []

    delayed_left = defaultdict(int)
    delayed_right = defaultdict(int)

    left_valid_size = 0
    right_valid_size = 0
    target_left_size = (k + 1) // 2

    def prune(heap, delayed, is_max_heap):
        while heap:
            value = -heap[0] if is_max_heap else heap[0]
            if delayed[value] == 0:
                break

            delayed[value] -= 1
            heapq.heappop(heap)

    def balance_heaps():
        nonlocal left_valid_size, right_valid_size

        # При заполнении первого окна слева может быть меньше элементов,
        # чем target_left_size.
        desired_left_size = min(
            left_valid_size + right_valid_size,
            target_left_size,
        )

        while left_valid_size > desired_left_size:
            prune(left_max_heap, delayed_left, is_max_heap=True)
            value = -heapq.heappop(left_max_heap)
            heapq.heappush(right_min_heap, value)
            left_valid_size -= 1
            right_valid_size += 1

        while left_valid_size < desired_left_size:
            prune(right_min_heap, delayed_right, is_max_heap=False)
            value = heapq.heappop(right_min_heap)
            heapq.heappush(left_max_heap, -value)
            right_valid_size -= 1
            left_valid_size += 1

    def insert_value(value):
        nonlocal left_valid_size, right_valid_size

        prune(left_max_heap, delayed_left, is_max_heap=True)

        if left_valid_size == 0 or value <= -left_max_heap[0]:
            heapq.heappush(left_max_heap, -value)
            left_valid_size += 1
        else:
            heapq.heappush(right_min_heap, value)
            right_valid_size += 1

        balance_heaps()

    def remove_value(value):
        nonlocal left_valid_size, right_valid_size

        prune(left_max_heap, delayed_left, is_max_heap=True)

        if left_valid_size > 0 and value <= -left_max_heap[0]:
            delayed_left[value] += 1
            left_valid_size -= 1
            prune(left_max_heap, delayed_left, is_max_heap=True)
        else:
            delayed_right[value] += 1
            right_valid_size -= 1
            prune(right_min_heap, delayed_right, is_max_heap=False)

        balance_heaps()

    def get_current_median():
        prune(left_max_heap, delayed_left, is_max_heap=True)

        if k % 2 == 1:
            return float(-left_max_heap[0])

        prune(right_min_heap, delayed_right, is_max_heap=False)
        return (-left_max_heap[0] + right_min_heap[0]) / 2.0

    for i in range(k):
        insert_value(numbers[i])

    medians = [get_current_median()]

    for i in range(k, n):
        insert_value(numbers[i])
        remove_value(numbers[i - k])
        medians.append(get_current_median())

    return medians

numbers = [1, 3, -1, -3, 5, 3, 6, 7]
n = len(numbers)
k = 3

print(compute_sliding_window_medians(numbers, n, k))
