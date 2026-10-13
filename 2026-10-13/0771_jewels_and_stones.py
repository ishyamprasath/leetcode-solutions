# 771. Jewels and Stones
# https://leetcode.com/problems/jewels-and-stones/


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        j = set(jewels)
        return sum(1 for c in stones if c in j)
