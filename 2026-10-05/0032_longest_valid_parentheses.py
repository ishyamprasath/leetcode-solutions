class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # The stack holds indices. Its bottom element is the index just
        # before the start of the current valid run.
        best = 0
        stack = [-1]
        for i, ch in enumerate(s):
            if ch == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    # Unmatched ")": it becomes the new base.
                    stack.append(i)
                else:
                    best = max(best, i - stack[-1])
        return best
