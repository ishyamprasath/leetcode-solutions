class Solution:
    def secondHighest(self, s: str) -> int:
        digits = sorted({int(ch) for ch in s if ch.isdigit()}, reverse=True)
        return digits[1] if len(digits) > 1 else -1
