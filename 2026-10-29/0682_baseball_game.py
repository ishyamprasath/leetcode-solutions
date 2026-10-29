# 682. Baseball Game
# https://leetcode.com/problems/baseball-game/
# Difficulty: Easy
# Approach: stack of scores.
from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st = []
        for op in operations:
            if op == "+":
                st.append(st[-1] + st[-2])
            elif op == "D":
                st.append(2 * st[-1])
            elif op == "C":
                st.pop()
            else:
                st.append(int(op))
        return sum(st)
