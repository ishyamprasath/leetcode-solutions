# Problem: Find Common Characters
# URL: https://leetcode.com/problems/find-common-characters/
# Difficulty: Easy
from collections import Counter

class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        common = Counter(words[0])
        for word in words[1:]:
            common &= Counter(word)
        return [char for char, count in common.items() for _ in range(count)]
