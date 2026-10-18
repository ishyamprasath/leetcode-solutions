# GFG 160 - Searching #3: Search in Rotated Sorted Array


class Solution:
    def search(self, arr, key):
        # Binary search on a rotated array: one half is always sorted.
        lo, hi = 0, len(arr) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if arr[mid] == key:
                return mid
            if arr[lo] <= arr[mid]:
                # left half [lo, mid] is sorted
                if arr[lo] <= key < arr[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                # right half [mid, hi] is sorted
                if arr[mid] < key <= arr[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return -1
