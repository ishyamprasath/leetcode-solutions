# Count Subarrays with XOR (GFG 160 - Hashing)
# https://www.geeksforgeeks.org/batch/gfg-160-problems/track/hashing-gfg-160/problem/count-subarray-with-given-xor

class Solution:
    def subarrayXor(self, arr, m):
        # Prefix-xor counting: a subarray ending here has xor m
        # if some earlier prefix equals (current prefix ^ m)
        seen = {0: 1}
        prefix = 0
        count = 0
        for x in arr:
            prefix ^= x
            count += seen.get(prefix ^ m, 0)
            seen[prefix] = seen.get(prefix, 0) + 1
        return count
