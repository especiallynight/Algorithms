import sys
from bisect import bisect_left


class LISAdvanced:
    def solve(self, n: int, a: list[int]) -> None:
        """Находит длину и количество наибольших возрастающих подпоследовательностей."""
        if not a:
            sys.stdout.write("0 0\n")
            return

        MOD = 1_000_000_007
        coords = sorted(list(set(a)))
        rank = {val: i + 1 for i, val in enumerate(coords)}
        m = len(coords)

        bit_len = [0] * (m + 1)
        bit_cnt = [0] * (m + 1)

        def update(i, length, count):
            while i <= m:
                if length > bit_len[i]:
                    bit_len[i] = length
                    bit_cnt[i] = count
                elif length == bit_len[i]:
                    bit_cnt[i] = (bit_cnt[i] + count) % MOD
                i += i & (-i)

        def query(i):
            res_l, res_c = 0, 1
            while i > 0:
                if bit_len[i] > res_l:
                    res_l = bit_len[i]
                    res_c = bit_cnt[i]
                elif bit_len[i] == res_l and res_l > 0:
                    res_c = (res_c + bit_cnt[i]) % MOD
                i -= i & (-i)
            return res_l, res_c

        for x in a:
            r = rank[x]
            l, c = query(r - 1)
            update(r, l + 1, c)

        sys.stdout.write(f"{query(m)[0]} {query(m)[1]}\n")


line1 = sys.stdin.buffer.readline()
if line1:
    n = int(line1)
    a = list(map(int, sys.stdin.buffer.readline().split()))
    LISAdvanced().solve(n, a)