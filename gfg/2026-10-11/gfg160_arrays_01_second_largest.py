# GFG 160 - Arrays #1: Second Largest
# https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/second-largest3735
class Solution:
    def getSecondLargest(self, arr):
        largest = -1
        second = -1
        for x in arr:
            if x > largest:
                second = largest
                largest = x
            elif x != largest and x > second:
                second = x
        return second
