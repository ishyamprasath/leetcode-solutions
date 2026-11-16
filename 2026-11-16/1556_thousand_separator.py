from typing import List

class Solution:
    def thousandSeparator(self, n: int) -> str:
        s = str(n)
        parts = []
        while len(s) > 3:
            parts.append(s[-3:])
            s = s[:-3]
        parts.append(s)
        return '.'.join(reversed(parts))
