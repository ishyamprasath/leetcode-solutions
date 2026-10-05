class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        # Every innermost "()" contributes 2^depth, where depth is the
        # number of open parentheses that enclose it.
        score = 0
        depth = 0
        for i, ch in enumerate(s):
            if ch == "(":
                depth += 1
            else:
                depth -= 1
                if s[i - 1] == "(":
                    score += 2 ** depth
        return score
