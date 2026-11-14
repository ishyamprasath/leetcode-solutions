class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        row_mins = {min(row) for row in matrix}
        col_maxes = {max(col) for col in zip(*matrix)}
        return list(row_mins & col_maxes)
