class Solution:
    def longestPalinSubseq(self, s):
        n = len(s)
        dp = [1] * n
        for i in range(n - 2, -1, -1):
            diagonal = 0
            for j in range(i + 1, n):
                old = dp[j]
                if s[i] == s[j]:
                    dp[j] = diagonal + 2
                else:
                    dp[j] = max(dp[j], dp[j - 1])
                diagonal = old
        return dp[-1]
