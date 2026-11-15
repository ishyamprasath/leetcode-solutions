class Solution:
    def countWays(self, s):
        symbols = s[0::2]
        operators = s[1::2]
        n = len(symbols)
        true = [[0] * n for _ in range(n)]
        false = [[0] * n for _ in range(n)]
        for i in range(n):
            if symbols[i] == 'T':
                true[i][i] = 1
            else:
                false[i][i] = 1
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                t = f = 0
                for k in range(i, j):
                    lt, lf = true[i][k], false[i][k]
                    rt, rf = true[k + 1][j], false[k + 1][j]
                    op = operators[k]
                    if op == '&':
                        t += lt * rt
                        f += lt * rf + lf * rt + lf * rf
                    elif op == '|':
                        t += lt * rt + lt * rf + lf * rt
                        f += lf * rf
                    else:
                        t += lt * rf + lf * rt
                        f += lt * rt + lf * rf
                true[i][j], false[i][j] = t, f
        return true[0][n - 1]
