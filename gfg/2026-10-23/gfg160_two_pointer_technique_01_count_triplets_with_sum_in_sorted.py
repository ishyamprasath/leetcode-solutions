class Solution:
    def countTriplets(self, arr, target):
        n = len(arr)
        total = 0
        for i in range(n - 2):
            need = target - arr[i]
            l, r = i + 1, n - 1
            while l < r:
                s = arr[l] + arr[r]
                if s < need:
                    l += 1
                elif s > need:
                    r -= 1
                else:
                    if arr[l] == arr[r]:
                        m = r - l + 1
                        total += m * (m - 1) // 2
                        break
                    lv, rv = arr[l], arr[r]
                    lc = 0
                    while l < r and arr[l] == lv:
                        l += 1
                        lc += 1
                    rc = 0
                    while r >= l and arr[r] == rv:
                        r -= 1
                        rc += 1
                    total += lc * rc
        return total
