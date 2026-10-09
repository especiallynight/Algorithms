import sys


def find_max_subarray_xor() -> None:
    """Находит максимальный XOR непрерывного фрагмента массива."""
    first_line: bytes = sys.stdin.buffer.readline()
    if not first_line:
        return

    n: int = int(first_line)
    numbers: list[int] = [
        int(x) for x in sys.stdin.buffer.readline().split()
    ]

    next_node: list[list[int]] = [[0, 0]]

    def insert(num: int) -> None:
        node: int = 0
        for i in range(29, -1, -1):
            bit: int = (num >> i) & 1
            if next_node[node][bit] == 0:
                next_node[node][bit] = len(next_node)
                next_node.append([0, 0])
            node = next_node[node][bit]

    def get_max(num: int) -> int:
        node: int = 0
        current_max: int = 0

        for i in range(29, -1, -1):
            bit: int = (num >> i) & 1
            toggled_bit: int = 1 - bit

            if next_node[node][toggled_bit] != 0:
                current_max |= 1 << i
                node = next_node[node][toggled_bit]
            else:
                node = next_node[node][bit]

        return current_max

    insert(0)

    max_xor: int = 0
    current_pref_xor: int = 0

    for num in numbers[:n]:
        current_pref_xor ^= num

        local_max: int = get_max(current_pref_xor)
        if local_max > max_xor:
            max_xor = local_max

        insert(current_pref_xor)

    sys.stdout.write(f"{max_xor}\n")


find_max_subarray_xor()

