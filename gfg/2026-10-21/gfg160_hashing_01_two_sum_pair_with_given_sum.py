# Two Sum - Pair with Given Sum
# https://www.geeksforgeeks.org/batch/gfg-160-problems/track/hashing-gfg-160/problem/key-pair5616
class Solution:
    def twoSum(self, arr, target):
        seen = set()
        for x in arr:
            if target - x in seen:
                return True
            seen.add(x)
        return False
