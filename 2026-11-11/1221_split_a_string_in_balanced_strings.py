class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balance = 0
        splits = 0
        for char in s:
            balance += 1 if char == "L" else -1
            if balance == 0:
                splits += 1
        return splits
