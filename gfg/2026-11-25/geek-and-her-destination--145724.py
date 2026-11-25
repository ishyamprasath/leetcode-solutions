class Solution:
    def minTime(self, a: int, b: int, d: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        c = a - b  # net progress per full cycle of a + b seconds

        # Using the jump is never worse than walking, so for jump j the time is
        # f(d - j) + 1, where f(x) is the first moment Geek stands at x.
        # Reaching x happens in the forward part of cycle k = ceil((x - a) / c)
        # (or k = 0 when x <= a), so f(x) = x + 2 * b * k.
        def ceil_sum(n: int) -> int:
            # sum of ceil(y / c) for y = 1..n
            if n <= 0:
                return 0
            q, rem = divmod(n, c)
            return c * q * (q + 1) // 2 + rem * (q + 1)

        low, high = d - r, d - l
        count = high - low + 1
        sum_x = (low + high) * count // 2
        sum_k = ceil_sum(high - a) - ceil_sum(low - 1 - a)
        return (sum_x + 2 * b * sum_k + count) % MOD
