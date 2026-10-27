# Title: Word Search
# URL: https://www.geeksforgeeks.org/batch/gfg-160-problems/track/recursion-and-backtracking-gfg-160/problem/word-search
# Difficulty: Medium
# Approach: DFS backtracking from each cell, marking visited in place.
class Solution:
    def isWordExist(self, mat, word):
        n = len(mat)
        m = len(mat[0])
        L = len(word)
        if L > n * m:
            return False

        def dfs(i, j, k):
            if mat[i][j] != word[k]:
                return False
            if k == L - 1:
                return True
            ch = mat[i][j]
            mat[i][j] = '#'
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                a = i + di
                b = j + dj
                if 0 <= a < n and 0 <= b < m and mat[a][b] != '#':
                    if dfs(a, b, k + 1):
                        mat[i][j] = ch
                        return True
            mat[i][j] = ch
            return False

        for i in range(n):
            for j in range(m):
                if dfs(i, j, 0):
                    return True
        return False
