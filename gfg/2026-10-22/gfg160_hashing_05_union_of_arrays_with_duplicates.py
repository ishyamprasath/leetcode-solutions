# Union of Arrays with Duplicates (GFG 160 - Hashing)
# https://www.geeksforgeeks.org/batch/gfg-160-problems/track/hashing-gfg-160/problem/union-of-two-arrays3538

class Solution:
    def findUnion(self, a, b):
        # Distinct elements present in either array
        return list(set(a) | set(b))
