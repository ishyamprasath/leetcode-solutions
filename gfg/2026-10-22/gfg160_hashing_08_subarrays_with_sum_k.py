# Subarrays with Sum K (GFG 160 - Hashing)
# https://www.geeksforgeeks.org/batch/gfg-160-problems/track/hashing-gfg-160/problem/subarrays-with-sum-k

class Solution:
    def cntSubarrays(self, arr, k):
        # Prefix-sum counting: a subarray ending here sums to k
        # if some earlier prefix equals (current prefix - k)
        seen = {0: 1}
        prefix = 0
        count = 0
        for x in arr:
            prefix += x
            count += seen.get(prefix - k, 0)
            seen[prefix] = seen.get(prefix, 0) + 1
        return count
