class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        for day in range(n):
            week, weekday = divmod(day, 7)
            total += week + weekday + 1
        return total
