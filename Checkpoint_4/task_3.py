import heapq
import sys


def find_running_medians(numbers: list[int]) -> list[float]:
    """Вычисляет текущую медиану для каждого шага с использованием двух куч.

    - max_back: куча для левой половины чисел.
    - min_front: куча для правой половины чисел.
    """
    max_back = []
    min_front = []
    medians = []

    for num in numbers:
        heapq.heappush(max_back, -num)

        heapq.heappush(min_front, -heapq.heappop(max_back))

        if len(min_front) > len(max_back):
            heapq.heappush(max_back, -heapq.heappop(min_front))

        if len(max_back) > len(min_front):
            current_median = float(-max_back[0])
        else:
            current_median = (-max_back[0] + min_front[0]) / 2.0

        medians.append(current_median)

    return medians


def run_medians_stream_task() -> None:
    first_line = sys.stdin.readline()
    if not first_line:
        return

    n = int(first_line.strip())

    second_line = sys.stdin.readline()
    sequence = list(map(int, second_line.split()))

    result_medians = find_running_medians(sequence)

    formatted_output = [f"{median:.1f}" for median in result_medians]
    print(*(formatted_output))

run_medians_stream_task()
