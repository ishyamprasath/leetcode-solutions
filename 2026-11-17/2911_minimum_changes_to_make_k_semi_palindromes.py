class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        # divisors[L] = proper divisors d of L (1 <= d < L)
        divisors = [[] for _ in range(n + 1)]
        for d in range(1, n + 1):
            for multiple in range(2 * d, n + 1, d):
                divisors[multiple].append(d)

        # cost[i][j] = min changes to make s[i:j] a semi-palindrome
        INF = float('inf')
        cost = [[INF] * (n + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(i + 2, n + 1):
                sub = s[i:j]
                best = INF
                for d in divisors[j - i]:
                    changes = 0
                    for r in range(d):
                        group = sub[r::d]
                        half = len(group) // 2
                        changes += sum(map(str.__ne__, group[:half], group[::-1][:half]))
                        if changes >= best:
                            break
                    if changes < best:
                        best = changes
                cost[i][j] = best

        # dp[j] = min changes to split s[:j] into p semi-palindromes
        dp = [INF] * (n + 1)
        dp[0] = 0
        for p in range(1, k + 1):
            new_dp = [INF] * (n + 1)
            for j in range(2 * p, n - 2 * (k - p) + 1):
                best = INF
                for i in range(2 * (p - 1), j - 1):
                    if dp[i] != INF:
                        value = dp[i] + cost[i][j]
                        if value < best:
                            best = value
                new_dp[j] = best
            dp = new_dp
        return dp[n]
