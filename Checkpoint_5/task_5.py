import sys
from array import array


def process_trie_operations() -> None:
    """Поддерживает множество слов и находит k-е слово по префиксу."""
    first_line: bytes = sys.stdin.buffer.readline()
    if not first_line:
        return

    q: int = int(first_line)

    next_node: array[int] = array("i", [0] * 26)
    sub_count: array[int] = array("i", [0])
    is_end: bytearray = bytearray(1)

    answers: list[str] = []

    for _ in range(q):
        parts: list[bytes] = sys.stdin.buffer.readline().split()
        operation: bytes = parts[0]
        word: bytes = parts[1]

        if operation == b"ADD":
            node: int = 0
            sub_count[node] += 1

            for char_code in word:
                idx: int = char_code - 97
                edge: int = node * 26 + idx
                nxt: int = next_node[edge]

                if nxt == 0:
                    nxt = len(sub_count)
                    next_node[edge] = nxt
                    next_node.extend([0] * 26)
                    sub_count.append(0)
                    is_end.append(0)

                node = nxt
                sub_count[node] += 1

            is_end[node] = 1

        elif operation == b"REMOVE":
            node = 0
            sub_count[node] -= 1

            for char_code in word:
                idx = char_code - 97
                node = next_node[node * 26 + idx]
                sub_count[node] -= 1

            is_end[node] = 0

        else:
            k: int = int(parts[2])
            node = 0
            possible = True

            for char_code in word:
                idx = char_code - 97
                node = next_node[node * 26 + idx]

                if node == 0 or sub_count[node] < k:
                    possible = False
                    break

            if not possible:
                answers.append("NONE")
                continue

            result: list[str] = [word.decode("ascii")]
            curr = node

            while True:
                if is_end[curr]:
                    if k == 1:
                        break
                    k -= 1

                found_next = False

                for idx in range(26):
                    nxt = next_node[curr * 26 + idx]

                    if nxt == 0 or sub_count[nxt] == 0:
                        continue

                    if k > sub_count[nxt]:
                        k -= sub_count[nxt]
                    else:
                        result.append(chr(97 + idx))
                        curr = nxt
                        found_next = True
                        break

                if not found_next:
                    result = []
                    break

            answers.append("".join(result) if result else "NONE")

    sys.stdout.write("\n".join(answers) + "\n" if answers else "")

process_trie_operations()