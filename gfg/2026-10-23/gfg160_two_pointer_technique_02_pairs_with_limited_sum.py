class Solution:
    #Complete the below function
    def countPairs(self, arr, target):
        a = sorted(arr)
        l, r = 0, len(a) - 1
        count = 0
        while l < r:
            if a[l] + a[r] < target:
                count += r - l
                l += 1
            else:
                r -= 1
        return count
