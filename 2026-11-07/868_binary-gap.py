class Solution:
    def binaryGap(self, n):
        last = ans = -1
        i = 0
        while n:
            if n & 1:
                if last != -1:
                    ans = max(ans, i - last)
                last = i
            n >>= 1
            i += 1
        return max(0, ans)
