from functools import cmp_to_key

class Solution:
    def findLargest(self, arr):
        nums = list(map(str, arr))
        # x goes before y if x+y forms a bigger number than y+x
        nums.sort(key=cmp_to_key(lambda x, y: (y + x > x + y) - (y + x < x + y)))
        result = "".join(nums)
        return "0" if result[0] == "0" else result
