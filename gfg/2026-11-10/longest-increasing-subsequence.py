# Longest Increasing Subsequence — GFG 160 Dynamic Programming, course position 110 — https://www.geeksforgeeks.org/problems/longest-increasing-subsequence-1587115620/1
from bisect import bisect_left

class Solution:
    def lis(self, arr):
        tails = []
        for value in arr:
            index = bisect_left(tails, value)
            if index == len(tails):
                tails.append(value)
            else:
                tails[index] = value
        return len(tails)
