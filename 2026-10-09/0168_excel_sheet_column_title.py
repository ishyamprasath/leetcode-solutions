# 168. Excel Sheet Column Title (Easy)
# https://leetcode.com/problems/excel-sheet-column-title/
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        letters = []
        while columnNumber > 0:
            columnNumber -= 1
            letters.append(chr(ord('A') + columnNumber % 26))
            columnNumber //= 26
        return ''.join(reversed(letters))
