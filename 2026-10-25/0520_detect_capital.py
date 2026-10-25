class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # Valid if all upper, all lower, or only the first letter is upper.
        return word.isupper() or word.islower() or word.istitle()
