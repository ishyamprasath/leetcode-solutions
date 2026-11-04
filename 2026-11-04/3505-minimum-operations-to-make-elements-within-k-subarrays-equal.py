# LeetCode 3505. Minimum Operations to Make Elements Within K Subarrays Equal (POD 2026-11-04)
from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        # cost[i] = ops to make nums[i:i+x] equal (sum of distances to median),
        # computed with Fenwick trees over compressed values; then DP picks k windows.
        n = len(nums)
        vals = sorted(set(nums))
        idx = {v: i + 1 for i, v in enumerate(vals)}
        m = len(vals)
        cnt = [0] * (m + 1)
        sm = [0] * (m + 1)
        LOG = 1
        while (1 << LOG) <= m:
            LOG += 1

        def update(p, dc, ds):
            while p <= m:
                cnt[p] += dc
                sm[p] += ds
                p += p & -p

        def query(p):
            c = s = 0
            while p > 0:
                c += cnt[p]
                s += sm[p]
                p -= p & -p
            return c, s

        def kth(t):
            pos = 0
            for b in range(LOG, -1, -1):
                np_ = pos + (1 << b)
                if np_ <= m and cnt[np_] < t:
                    pos = np_
                    t -= cnt[np_]
            return pos + 1

        cost = []
        total = 0
        for i in range(n):
            update(idx[nums[i]], 1, nums[i])
            total += nums[i]
            if i >= x:
                update(idx[nums[i - x]], -1, -nums[i - x])
                total -= nums[i - x]
            if i >= x - 1:
                p = kth((x + 1) // 2)
                med = vals[p - 1]
                c, s = query(p)
                cost.append(med * c - s + (total - s) - med * (x - c))

        INF = float('inf')
        # dp over windows: prev[i] = min cost using j-1 windows within first i elements
        prev = [0] * (n + 1)
        for j in range(1, k + 1):
            cur = [INF] * (n + 1)
            for i in range(j * x, n + 1):
                cur[i] = min(cur[i - 1], prev[i - x] + cost[i - x])
            prev = cur
        return prev[n]
