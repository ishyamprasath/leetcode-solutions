class Solution:
    def reformatNumber(self, number: str) -> str:
        digits = [c for c in number if c.isdigit()]
        blocks = []
        i = 0
        while len(digits) - i > 4:
            blocks.append(''.join(digits[i:i + 3]))
            i += 3
        rest = len(digits) - i
        if rest == 4:
            blocks.append(''.join(digits[i:i + 2]))
            blocks.append(''.join(digits[i + 2:i + 4]))
        else:
            blocks.append(''.join(digits[i:]))
        return '-'.join(blocks)
