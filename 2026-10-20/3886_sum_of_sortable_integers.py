# 3886. Sum of Sortable Integers (Hard) - Problem of the Day 2026-10-20
class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        descent = [0] * n
        for i in range(n - 1):
            descent[i + 1] = descent[i] + (nums[i] > nums[i + 1])
        total = 0
        for k in range(1, n + 1):
            if n % k:
                continue
            ok = True
            prev_max = 0
            for start in range(0, n, k):
                end = start + k
                drops = descent[end - 1] - descent[start]
                if nums[end - 1] > nums[start]:
                    drops += 1
                if drops > 1:
                    ok = False
                    break
                block = nums[start:end]
                if min(block) < prev_max:
                    ok = False
                    break
                prev_max = max(block)
            if ok:
                total += k
        return total
