# LeetCode 921. Minimum Add to Make Parentheses Valid (Medium)
# Problem of the Day: 2026-10-06
#
# Idea: scan left to right, tracking how many "(" are still waiting for a
# match. A ")" either closes one of those, or (if none are open) must get a
# new "(" inserted before it. Whatever "(" remain open at the end each need
# a ")" added. Time O(n), space O(1).


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_needed = 0   # unmatched "(" waiting for a ")"
        close_needed = 0  # unmatched ")" that need a "(" added
        for ch in s:
            if ch == "(":
                open_needed += 1
            elif open_needed > 0:
                open_needed -= 1
            else:
                close_needed += 1
        return open_needed + close_needed


if __name__ == "__main__":
    sol = Solution()
    assert sol.minAddToMakeValid("())") == 1
    assert sol.minAddToMakeValid("(((") == 3
    assert sol.minAddToMakeValid("()))((") == 4
    print("All sample cases pass")
