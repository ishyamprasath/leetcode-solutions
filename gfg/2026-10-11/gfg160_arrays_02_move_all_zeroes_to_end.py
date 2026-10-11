# GFG 160 - Arrays #2: Move All Zeroes to End
# https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/move-all-zeroes-to-end-of-array0751
class Solution:
    def pushZerosToEnd(self, arr: list[int]) -> None:
        # Stable two-pointer: move each non-zero to the next free slot.
        write = 0
        for read in range(len(arr)):
            if arr[read] != 0:
                arr[write], arr[read] = arr[read], arr[write]
                write += 1
