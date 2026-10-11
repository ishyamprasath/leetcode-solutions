# GFG 160 - Arrays #4: Rotate Array
# https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/rotate-array-by-n-elements-1587115621
class Solution:
    def rotateArr(self, arr, d):
        n = len(arr)
        d %= n
        if d == 0:
            return

        # Reversal algorithm: reverse both parts, then reverse the whole array.
        self.reverse(arr, 0, d - 1)
        self.reverse(arr, d, n - 1)
        self.reverse(arr, 0, n - 1)

    def reverse(self, arr, left, right):
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
