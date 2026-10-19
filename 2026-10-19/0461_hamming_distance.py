# LeetCode 461. Hamming Distance (Easy)


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count("1")
