# LeetCode 301. Remove Invalid Parentheses (Hard)
# Problem of the Day: 2026-10-07
#
# Idea: breadth-first search over strings, one removal per level. Start with
# s itself; at each level try removing every single parenthesis from every
# string in the current level. The first level that contains any valid
# string uses the minimum number of removals, so collect all valid strings
# there and stop. A set de-duplicates candidates at each level.
# With at most 20 parentheses this stays fast in practice.

from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(t: str) -> bool:
            balance = 0
            for ch in t:
                if ch == "(":
                    balance += 1
                elif ch == ")":
                    balance -= 1
                    if balance < 0:
                        return False
            return balance == 0

        level = {s}
        while level:
            valid = [t for t in level if is_valid(t)]
            if valid:
                return valid
            next_level = set()
            for t in level:
                for i, ch in enumerate(t):
                    if ch in "()":
                        next_level.add(t[:i] + t[i + 1:])
            level = next_level
        return [""]


if __name__ == "__main__":
    sol = Solution()
    assert sorted(sol.removeInvalidParentheses("()())()")) == ["(())()", "()()()"]
    assert sorted(sol.removeInvalidParentheses("(a)())()")) == ["(a())()", "(a)()()"]
    assert sol.removeInvalidParentheses(")(") == [""]
    print("All sample cases pass")
