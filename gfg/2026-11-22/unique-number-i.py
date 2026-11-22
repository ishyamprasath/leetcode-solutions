class Solution:
    def findUnique(self, arr):
        # Paired values cancel out under XOR.
        result = 0
        for x in arr:
            result ^= x
        return result
