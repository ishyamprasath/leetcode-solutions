class Solution:
    def digitCount(self, num: str) -> bool:
        return all(num.count(str(i)) == int(c) for i, c in enumerate(num))
