class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row_count = [sum(row) for row in mat]
        col_count = [sum(col) for col in zip(*mat)]
        count = 0
        for i, row in enumerate(mat):
            for j, val in enumerate(row):
                if val == 1 and row_count[i] == 1 and col_count[j] == 1:
                    count += 1
        return count
