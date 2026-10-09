import sys


def find_two_unique_numbers() -> None:
    """Находит два числа, встречающихся один раз."""
    first_line: bytes = sys.stdin.buffer.readline()
    if not first_line:
        return

    n: int = int(first_line)
    numbers: list[int] = [
        int(x) for x in sys.stdin.buffer.readline().split()
    ][:n]

    xor_total: int = 0
    for num in numbers:
        xor_total ^= num

    diff_bit: int = xor_total & -xor_total

    num1: int = 0
    num2: int = 0

    for num in numbers:
        if num & diff_bit:
            num1 ^= num
        else:
            num2 ^= num

    if num1 > num2:
        num1, num2 = num2, num1

    sys.stdout.write(f"{num1} {num2}\n")


find_two_unique_numbers()
