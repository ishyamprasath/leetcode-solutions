# GFG 160 Sorting 3: Count Inversions
# Modified merge sort: when taking from right half, add (mid - i + 1) inversions.


class Solution:
    def inversionCount(self, arr):
        temp = [0] * len(arr)
        return self._merge_sort(arr, temp, 0, len(arr) - 1)

    def _merge_sort(self, arr, temp, left, right):
        if left >= right:
            return 0
        mid = (left + right) // 2
        inv = self._merge_sort(arr, temp, left, mid)
        inv += self._merge_sort(arr, temp, mid + 1, right)
        inv += self._merge(arr, temp, left, mid, right)
        return inv

    def _merge(self, arr, temp, left, mid, right):
        i, j, k = left, mid + 1, left
        inv = 0
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp[k] = arr[i]
                i += 1
            else:
                temp[k] = arr[j]
                j += 1
                inv += mid - i + 1
            k += 1
        while i <= mid:
            temp[k] = arr[i]
            i += 1
            k += 1
        while j <= right:
            temp[k] = arr[j]
            j += 1
            k += 1
        for idx in range(left, right + 1):
            arr[idx] = temp[idx]
        return inv
