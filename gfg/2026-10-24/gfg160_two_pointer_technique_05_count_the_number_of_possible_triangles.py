class Solution:
    def countTriangles(self, arr):
        arr = sorted(arr)
        n = len(arr)
        count = 0
        for k in range(2, n):
            i = 0
            j = k - 1
            while i < j:
                if arr[i] + arr[j] > arr[k]:
                    count += j - i
                    j -= 1
                else:
                    i += 1
        return count
