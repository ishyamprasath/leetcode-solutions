class Solution:
    def countEven(self, num: int) -> int:
        count = 0
        for x in range(1, num + 1):
            if sum(int(c) for c in str(x)) % 2 == 0:
                count += 1
        return count
