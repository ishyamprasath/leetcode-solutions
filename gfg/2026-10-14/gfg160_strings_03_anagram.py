# GFG 160 Strings 3: Anagram
# Two strings are anagrams when they have the same character counts.
from collections import Counter


class Solution:
    def areAnagrams(self, s1, s2):
        return len(s1) == len(s2) and Counter(s1) == Counter(s2)
