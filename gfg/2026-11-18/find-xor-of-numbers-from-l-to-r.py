class Solution:
    def findXOR(self, l: int, r: int) -> int:
        # XOR of 1..n follows a cycle of length 4
        def xor_upto(n):
            rem = n % 4
            if rem == 0:
                return n
            if rem == 1:
                return 1
            if rem == 2:
                return n + 1
            return 0

        return xor_upto(r) ^ xor_upto(l - 1)
