class Solution:
    def digitalRoot(self, n: int) -> int:
        return 9 if n % 9 == 0 else n % 9
