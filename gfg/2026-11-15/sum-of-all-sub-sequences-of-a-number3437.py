class Solution:
    def subsequenceSum(self, s):
        MOD = 10**9 + 7
        n = len(s)
        digit_total = sum(int(c) for c in s)
        # each digit appears in 2^(n-1) non-empty subsequences
        return digit_total * pow(2, n - 1, MOD) % MOD
