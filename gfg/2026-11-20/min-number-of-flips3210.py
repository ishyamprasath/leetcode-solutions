class Solution:
    def minFlips(self, s):
        # Count mismatches against the pattern starting with '0' ("0101...").
        # The other pattern ("1010...") needs exactly len(s) - that many flips.
        start_zero = 0
        for i, ch in enumerate(s):
            expected = '0' if i % 2 == 0 else '1'
            if ch != expected:
                start_zero += 1
        return min(start_zero, len(s) - start_zero)
