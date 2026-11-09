# Problem: Find the Town Judge
# URL: https://leetcode.com/problems/find-the-town-judge/
# Difficulty: Easy
class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        score = [0] * (n + 1)
        for a, b in trust:
            score[a] -= 1
            score[b] += 1
        for person in range(1, n + 1):
            if score[person] == n - 1:
                return person
        return -1
