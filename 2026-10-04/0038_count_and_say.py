# 38. Count and Say
# Difficulty: Medium
# URL: https://leetcode.com/problems/count-and-say/

class Solution:
    def countAndSay(self, n: int) -> str:
        term = "1"
        for _ in range(n - 1):
            next_term: list[str] = []
            i = 0
            while i < len(term):
                j = i
                # Count consecutive identical digits
                while j < len(term) and term[j] == term[i]:
                    j += 1
                next_term.append(str(j - i))
                next_term.append(term[i])
                i = j
            term = ''.join(next_term)
        return term
