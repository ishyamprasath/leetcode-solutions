# Title: Solve the Sudoku
# URL: https://www.geeksforgeeks.org/batch/gfg-160-problems/track/recursion-and-backtracking-gfg-160/problem/solve-the-sudoku-1587115621
# Difficulty: Hard
# Approach: Backtracking with row/col/box bitmasks and min-remaining-values cell choice.
class Solution:
    def solveSudoku(self, mat: list[list[int]]) -> None:
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        empties = []
        for i in range(9):
            for j in range(9):
                v = mat[i][j]
                if v:
                    b = 1 << v
                    rows[i] |= b
                    cols[j] |= b
                    boxes[(i // 3) * 3 + j // 3] |= b
                else:
                    empties.append((i, j))

        def solve():
            best = -1
            bestmask = 0
            bestcnt = 10
            for k in range(len(empties)):
                i, j = empties[k]
                if mat[i][j]:
                    continue
                used = rows[i] | cols[j] | boxes[(i // 3) * 3 + j // 3]
                free = (~used) & 0x3FE
                cnt = bin(free).count("1")
                if cnt < bestcnt:
                    bestcnt = cnt
                    best = k
                    bestmask = free
                    if cnt <= 1:
                        break
            if best == -1:
                return True
            if bestcnt == 0:
                return False
            i, j = empties[best]
            bi = (i // 3) * 3 + j // 3
            m = bestmask
            while m:
                low = m & -m
                m ^= low
                v = low.bit_length() - 1
                mat[i][j] = v
                rows[i] |= low
                cols[j] |= low
                boxes[bi] |= low
                if solve():
                    return True
                mat[i][j] = 0
                rows[i] ^= low
                cols[j] ^= low
                boxes[bi] ^= low
            return False

        solve()
