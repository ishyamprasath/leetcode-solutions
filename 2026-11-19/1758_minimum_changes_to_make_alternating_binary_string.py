class Solution:
    def minOperations(self, s: str) -> int:
        start_zero = 0
        for i, ch in enumerate(s):
            expected = '0' if i % 2 == 0 else '1'
            if ch != expected:
                start_zero += 1
        return min(start_zero, len(s) - start_zero)
