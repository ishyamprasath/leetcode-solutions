# Intersection of Two arrays with Duplicate Elements (GFG 160 - Hashing)
# https://www.geeksforgeeks.org/batch/gfg-160-problems/track/hashing-gfg-160/problem/intersection-of-two-arrays-with-duplicate-elements

class Solution:
    def intersect(self, a, b):
        # Elements present in both arrays, without duplicates
        return list(set(a) & set(b))
