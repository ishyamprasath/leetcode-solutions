class Solution:
    def largestInteger(self, num: int) -> int:
        digits = [int(c) for c in str(num)]
        evens = sorted((d for d in digits if d % 2 == 0), reverse=True)
        odds = sorted((d for d in digits if d % 2 == 1), reverse=True)
        ei = oi = 0
        result = []
        for d in digits:
            if d % 2 == 0:
                result.append(evens[ei])
                ei += 1
            else:
                result.append(odds[oi])
                oi += 1
        return int("".join(map(str, result)))
