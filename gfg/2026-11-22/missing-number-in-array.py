class Solution:
    def missingNum(self, arr: list[int]) -> int:
        # XOR of 1..n with all elements leaves only the missing number.
        n = len(arr) + 1
        result = 0
        for i in range(1, n + 1):
            result ^= i
        for x in arr:
            result ^= x
        return result
