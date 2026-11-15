class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        odd_prefix, even_prefix = 0, 1  # empty prefix has even sum
        prefix = 0
        result = 0
        for x in arr:
            prefix += x
            if prefix % 2:
                result += even_prefix
                odd_prefix += 1
            else:
                result += odd_prefix
                even_prefix += 1
        return result % MOD
