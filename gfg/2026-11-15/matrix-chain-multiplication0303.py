class Solution:
    def matrixMultiplication(self, arr):
        n = len(arr)
        # dp[i][j] = min cost to multiply matrices i..j (matrix k is arr[k-1] x arr[k])
        dp = [[0] * n for _ in range(n)]
        for length in range(2, n):
            for i in range(1, n - length + 1):
                j = i + length - 1
                best = float('inf')
                for k in range(i, j):
                    cost = dp[i][k] + dp[k + 1][j] + arr[i - 1] * arr[k] * arr[j]
                    if cost < best:
                        best = cost
                dp[i][j] = best
        return dp[1][n - 1] if n > 2 else 0
