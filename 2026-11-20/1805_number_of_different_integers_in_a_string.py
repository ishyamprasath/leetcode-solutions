class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        seen = set()
        digits = []
        for ch in word + "a":
            if ch.isdigit():
                digits.append(ch)
            elif digits:
                seen.add(int("".join(digits)))
                digits = []
        return len(seen)
