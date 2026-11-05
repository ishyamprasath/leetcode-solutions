# GFG POTD 2026-11-05: Minimum Days
# https://www.geeksforgeeks.org/problems/minimum-days--170646/1


class Solution:
    def getMinimumDays(self, s: str, p: list[int]) -> int:
        # pos[i] = day on which index i becomes '?'. An adjacent equal pair is
        # broken once either index is replaced, i.e. after min(day) + 1 days.
        pos = {idx: d for d, idx in enumerate(p)}
        return max(
            [min(pos[i], pos[i + 1]) + 1 for i in range(len(s) - 1) if s[i] == s[i + 1]],
            default=0,
        )
