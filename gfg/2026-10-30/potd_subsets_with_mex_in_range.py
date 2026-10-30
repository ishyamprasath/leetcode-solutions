from typing import List


# GFG Problem of the Day (2026-10-30): Subsets with MEX in Range
class Solution:
    def cntSubsets(self, arr: List[int], l: int, r: int) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        cnt = [0] * (n + 2)
        for x in arr:
            cnt[x] += 1
        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow2[i] = pow2[i - 1] * 2 % MOD
        ans = 0
        prod = 1  # product of (2^cnt[i] - 1) for i < m
        used = 0  # number of elements with value <= m
        for m in range(0, r + 1):
            used += cnt[m]
            if m >= l:
                ans = (ans + prod * pow2[n - used]) % MOD
            if cnt[m] == 0:
                break
            prod = prod * (pow2[cnt[m]] - 1) % MOD
        return ans
