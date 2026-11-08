# 917. Reverse Only Letters (Easy)
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        letters = iter(ch for ch in reversed(s) if ch.isalpha())
        return ''.join(next(letters) if ch.isalpha() else ch for ch in s)
