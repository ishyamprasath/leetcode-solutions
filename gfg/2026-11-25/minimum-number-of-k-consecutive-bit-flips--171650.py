class Solution:
    def kBitFlips(self, arr, k):
        n = len(arr)
        diff = [0] * (n + 1)
        cur = 0
        ops = 0
        for i in range(n):
            cur ^= diff[i]
            if arr[i] ^ cur == 0:
                if i + k > n:
                    return -1
                ops += 1
                cur ^= 1
                diff[i + k] ^= 1
        return ops
