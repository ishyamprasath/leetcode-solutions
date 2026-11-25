class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        import random

        n = len(nums)
        mod = (1 << 61) - 1
        base = random.randrange(10**6, mod - 1)
        prefix = [0] * (n + 1)
        power = [1] * (n + 1)
        for i, x in enumerate(nums):
            prefix[i + 1] = (prefix[i] * base + x) % mod
            power[i + 1] = power[i] * base % mod

        def has_unique(length: int) -> bool:
            p = power[length]
            counts = Counter(
                (prefix[i + length] - prefix[i] * p) % mod
                for i in range(n - length + 1)
            )
            return 1 in counts.values()

        # If some subarray of length L is unique, extending it keeps it unique,
        # so the answer is monotone and can be binary searched.
        lo, hi = 1, n
        while lo < hi:
            mid = (lo + hi) // 2
            if has_unique(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
