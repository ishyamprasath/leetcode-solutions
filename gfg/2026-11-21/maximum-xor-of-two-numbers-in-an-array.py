class Solution:
    def maxXor(self, arr):
        best = 0
        mask = 0
        for bit in range(20, -1, -1):
            mask |= 1 << bit
            prefixes = {x & mask for x in arr}
            candidate = best | (1 << bit)
            # Keep this bit if two prefixes XOR to the candidate.
            if any(candidate ^ p in prefixes for p in prefixes):
                best = candidate
        return best
