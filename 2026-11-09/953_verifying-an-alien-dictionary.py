# Problem: Verifying an Alien Dictionary
# URL: https://leetcode.com/problems/verifying-an-alien-dictionary/
# Difficulty: Easy
class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        rank = {char: i for i, char in enumerate(order)}
        for a, b in zip(words, words[1:]):
            for x, y in zip(a, b):
                if rank[x] != rank[y]:
                    if rank[x] > rank[y]:
                        return False
                    break
            else:
                if len(a) > len(b):
                    return False
        return True
