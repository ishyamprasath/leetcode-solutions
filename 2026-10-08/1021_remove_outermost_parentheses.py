# 1021. Remove Outermost Parentheses (Easy) - LeetCode Problem of the Day, 2026-10-08
# https://leetcode.com/problems/remove-outermost-parentheses/
#
# Idea: walk the string while tracking nesting depth. A '(' seen at depth 0
# opens a new primitive, and a ')' that brings depth back to 0 closes it.
# Those outermost characters are skipped; everything else is kept.
# Time O(n), space O(n) for the output.


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        depth = 0
        for ch in s:
            if ch == "(":
                if depth > 0:
                    result.append(ch)
                depth += 1
            else:
                depth -= 1
                if depth > 0:
                    result.append(ch)
        return "".join(result)


if __name__ == "__main__":
    sol = Solution()
    assert sol.removeOuterParentheses("(()())(())") == "()()()"
    assert sol.removeOuterParentheses("(()())(())(()(()))") == "()()()()(())"
    assert sol.removeOuterParentheses("()()") == ""
    print("all sample cases pass")
