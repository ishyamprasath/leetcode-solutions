# All Triplets with Zero Sum
# https://www.geeksforgeeks.org/batch/gfg-160-problems/track/hashing-gfg-160/problem/find-all-triplets-with-zero-sum
class Solution:
    def findTriplets(self, arr):
        n = len(arr)
        pos = {}
        for idx, v in enumerate(arr):
            pos.setdefault(v, []).append(idx)
        res = []
        for i in range(n):
            for j in range(i + 1, n):
                need = -arr[i] - arr[j]
                if need in pos:
                    for k in pos[need]:
                        if k > j:
                            res.append([i, j, k])
        return res
