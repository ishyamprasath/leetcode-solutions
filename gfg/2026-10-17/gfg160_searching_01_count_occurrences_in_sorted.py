# GFG 160 - Searching 1: Count Occurrences in Sorted (Medium)
from bisect import bisect_left, bisect_right


class Solution:
    def countFreq(self, arr, target):
        return bisect_right(arr, target) - bisect_left(arr, target)
