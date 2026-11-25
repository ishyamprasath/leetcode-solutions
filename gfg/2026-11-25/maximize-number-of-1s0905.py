class Solution:
    def maxOnes(self, arr, k):
        l = 0
        zeros = 0
        best = 0
        for r in range(len(arr)):
            if arr[r] == 0:
                zeros += 1
            while zeros > k:
                if arr[l] == 0:
                    zeros -= 1
                l += 1
            best = max(best, r - l + 1)
        return best
