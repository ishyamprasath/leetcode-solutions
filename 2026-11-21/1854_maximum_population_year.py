from typing import List


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        delta = [0] * 101
        for birth, death in logs:
            delta[birth - 1950] += 1
            delta[death - 1950] -= 1
        best_year, best, running = 1950, 0, 0
        for i in range(101):
            running += delta[i]
            if running > best:
                best, best_year = running, 1950 + i
        return best_year
