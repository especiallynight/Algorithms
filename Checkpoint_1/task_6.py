from collections import Counter

def min_window(source: str, target: str) -> str:
    required = Counter(target)

    formed = 0
    need = len(required)

    window = {}

    left = 0
    best_start = 0
    best_length = float("inf")

    for right, char in enumerate(source):
        window[char] = window.get(char, 0) + 1

        if char in required and window[char] == required[char]:
            formed += 1

        while formed == need:
            current_length = right - left + 1

            if current_length < best_length:
                best_length = current_length
                best_start = left

            left_char = source[left]
            window[left_char] -= 1

            if (
                left_char in required
                and window[left_char] < required[left_char]
            ):
                formed -= 1

            left += 1

    if best_length == float("inf"):
        return ""

    return source[best_start:best_start + best_length]
print(min_window("ADOBECODEBANC", "ABC"))
