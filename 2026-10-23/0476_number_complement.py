class Solution:
    def findComplement(self, num: int) -> int:
        # XOR with a mask of all ones covering num's bit length
        mask = (1 << num.bit_length()) - 1
        return num ^ mask
