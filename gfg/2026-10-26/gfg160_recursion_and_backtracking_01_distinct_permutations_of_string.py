class Solution:
    def findPermutation(self, s: str) -> list[str]:
        chars = sorted(s)
        n = len(chars)
        used = [False] * n
        current = []
        result = []

        def backtrack():
            if len(current) == n:
                result.append("".join(current))
                return
            for i in range(n):
                if used[i]:
                    continue
                # skip a duplicate unless its identical predecessor is in use
                if i > 0 and chars[i] == chars[i - 1] and not used[i - 1]:
                    continue
                used[i] = True
                current.append(chars[i])
                backtrack()
                current.pop()
                used[i] = False

        backtrack()
        return result
