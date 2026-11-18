class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set("aeiouAEIOU")
        half = len(s) // 2
        left = sum(1 for c in s[:half] if c in vowels)
        right = sum(1 for c in s[half:] if c in vowels)
        return left == right
