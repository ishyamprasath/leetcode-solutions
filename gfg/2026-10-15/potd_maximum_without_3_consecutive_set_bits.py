# GFG POTD 2026-10-15: Maximum Without 3 Consecutive Set Bits
# From the high bit down, keep set bits unless that would make three in a row.


class Solution:
    def maxValue(self, n: int) -> int:
        res = 0
        cnt = 0
        for i in range(31, -1, -1):
            if (n >> i) & 1:
                cnt += 1
                if cnt == 3:
                    cnt = 0
                else:
                    res |= 1 << i
            else:
                cnt = 0
        return res
