from typing import List

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        result = [n] * n
        prev = -n
        for i in range(n):
            if s[i] == c:
                prev = i
            result[i] = i - prev
        nxt = 2 * n
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                nxt = i
            result[i] = min(result[i], nxt - i)
        return result
