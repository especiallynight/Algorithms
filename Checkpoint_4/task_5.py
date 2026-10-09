import sys

def count_pairs_with_sum_less_or_equal(
    array_a: list[int], array_b: list[int], target_sum: int
) -> int:
    """Подсчитывает количество пар (A[i], B[j]), сумма которых <= target_sum.

    Используется метод двух указателей за O(len(A) + len(B)).
    """
    total_pairs = 0
    pointer_b = len(array_b) - 1

    for a_val in array_a:
        while pointer_b >= 0 and a_val + array_b[pointer_b] > target_sum:
            pointer_b -= 1

        if pointer_b < 0:
            break

        total_pairs += pointer_b + 1

    return total_pairs


def find_kth_smallest_pair_sum(
    array_a: list[int], array_b: list[int], k: int
) -> int:
    """Находит k-ю наименьшую сумму пары методом бинарного поиска по ответу."""
    low_sum = array_a[0] + array_b[0]
    high_sum = array_a[-1] + array_b[-1]
    result_kth_sum = high_sum

    while low_sum <= high_sum:
        mid_sum = (low_sum + high_sum) // 2

        if count_pairs_with_sum_less_or_equal(array_a, array_b, mid_sum) >= k:
            result_kth_sum = mid_sum
            high_sum = mid_sum - 1
        else:
            low_sum = mid_sum + 1

    return result_kth_sum


def run_kth_pair_sum_task() -> None:
    first_line = sys.stdin.readline()
    if not first_line:
        return

    n, m, k = map(int, first_line.split())

    second_line = sys.stdin.readline()
    array_a = list(map(int, second_line.split()))

    third_line = sys.stdin.readline()
    array_b = list(map(int, third_line.split()))

    ans = find_kth_smallest_pair_sum(array_a, array_b, k)
    print(ans)

run_kth_pair_sum_task()
