from typing import List

class Solution:
    def modifyString(self, s: str) -> str:
        chars = list(s)
        for i, ch in enumerate(chars):
            if ch == '?':
                for c in 'abc':
                    if (i > 0 and chars[i - 1] == c) or (i + 1 < len(chars) and chars[i + 1] == c):
                        continue
                    chars[i] = c
                    break
        return ''.join(chars)
