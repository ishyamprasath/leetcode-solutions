# Arrange Anagrams Together (GFG 160 - Hashing)
# https://www.geeksforgeeks.org/batch/gfg-160-problems/track/hashing-gfg-160/problem/print-anagrams-together

class Solution:
    def anagrams(self, arr):
        # Group words by their sorted letters, keeping original order inside each group
        groups = {}
        for word in arr:
            key = ''.join(sorted(word))
            groups.setdefault(key, []).append(word)
        return list(groups.values())
