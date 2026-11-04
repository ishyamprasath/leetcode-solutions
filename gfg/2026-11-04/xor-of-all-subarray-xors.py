# GFG POTD 2026-11-04: XOR of All Subarray XORs
# https://www.geeksforgeeks.org/problems/game-of-xor1541/1


class Solution:
    def subarrayXor(self, arr):
        # Element i lies in (i+1)*(n-i) subarrays; it counts only if that is odd,
        # which happens only when n is odd and i is even.
        n = len(arr)
        res = 0
        if n % 2 == 1:
            for i in range(0, n, 2):
                res ^= arr[i]
        return res
