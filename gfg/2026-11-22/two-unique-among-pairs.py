class Solution:
    def singleNum(self, arr):
        xor_all = 0
        for x in arr:
            xor_all ^= x
        # The lowest set bit separates the two unique numbers into different groups.
        low_bit = xor_all & -xor_all
        a = 0
        b = 0
        for x in arr:
            if x & low_bit:
                a ^= x
            else:
                b ^= x
        return sorted([a, b])
