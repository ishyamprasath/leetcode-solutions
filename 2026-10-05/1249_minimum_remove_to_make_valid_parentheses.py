class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        chars = list(s)
        open_indices = []

        # First pass: drop every ")" that has no matching "(".
        for i, ch in enumerate(chars):
            if ch == "(":
                open_indices.append(i)
            elif ch == ")":
                if open_indices:
                    open_indices.pop()
                else:
                    chars[i] = ""

        # Any "(" still on the stack was never closed, so drop it too.
        for i in open_indices:
            chars[i] = ""

        return "".join(chars)
