class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        # drop consecutive duplicates, then count local peaks and dips
        vals = [nums[0]]
        for x in nums[1:]:
            if x != vals[-1]:
                vals.append(x)
        count = 0
        for i in range(1, len(vals) - 1):
            if (vals[i] > vals[i - 1] and vals[i] > vals[i + 1]) or \
               (vals[i] < vals[i - 1] and vals[i] < vals[i + 1]):
                count += 1
        return count
