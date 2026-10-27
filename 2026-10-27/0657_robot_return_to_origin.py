# 657. Robot Return to Origin
# https://leetcode.com/problems/robot-return-to-origin/
# Difficulty: Easy
# Approach: counts of U/D and L/R must match.
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')
