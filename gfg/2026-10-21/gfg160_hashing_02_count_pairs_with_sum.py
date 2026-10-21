# Count Pairs with Sum
# https://www.geeksforgeeks.org/batch/gfg-160-problems/track/hashing-gfg-160/problem/count-pairs-with-given-sum--150253
class Solution:
    def countPairs(self, arr, target):
        freq = {}
        count = 0
        for x in arr:
            count += freq.get(target - x, 0)
            freq[x] = freq.get(x, 0) + 1
        return count
