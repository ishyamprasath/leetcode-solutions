class Solution:
    def countPairs(self, arr, target):
        l, r = 0, len(arr) - 1
        count = 0
        while l < r:
            s = arr[l] + arr[r]
            if s < target:
                l += 1
            elif s > target:
                r -= 1
            else:
                if arr[l] == arr[r]:
                    m = r - l + 1
                    count += m * (m - 1) // 2
                    break
                lv, rv = arr[l], arr[r]
                lc = 0
                while arr[l] == lv:
                    l += 1
                    lc += 1
                rc = 0
                while arr[r] == rv:
                    r -= 1
                    rc += 1
                count += lc * rc
        return count
