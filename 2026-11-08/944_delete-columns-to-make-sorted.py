# 944. Delete Columns to Make Sorted (Easy)
class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        rows, cols = len(strs), len(strs[0])
        return sum(any(strs[r][c] > strs[r + 1][c] for r in range(rows - 1)) for c in range(cols))
