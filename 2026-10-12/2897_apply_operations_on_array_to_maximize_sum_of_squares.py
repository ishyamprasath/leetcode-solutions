from typing import List


class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        cnt = [0] * 31
        for x in nums:
            for b in range(31):
                if (x >> b) & 1:
                    cnt[b] += 1
        mod = 10**9 + 7
        ans = 0
        for _ in range(k):
            v = 0
            for b in range(31):
                if cnt[b] > 0:
                    cnt[b] -= 1
                    v |= 1 << b
            ans = (ans + v * v) % mod
        return ans
