# 2160. Minimum Sum of Four Digit Number After Splitting Digits (Easy)


class Solution:
    def minimumSum(self, num: int) -> int:
        d = sorted(int(c) for c in str(num))
        return (d[0] + d[1]) * 10 + d[2] + d[3]
