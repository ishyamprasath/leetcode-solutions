# GFG 160 - Sorting 7: Merge Without Extra Space (Medium) - gap method


class Solution:
    def mergeArrays(self, a, b):
        n, m = len(a), len(b)
        gap = (n + m + 1) // 2
        while gap > 0:
            i = 0
            j = gap
            while j < n + m:
                if i < n:
                    x = a[i]
                else:
                    x = b[i - n]
                if j < n:
                    y = a[j]
                else:
                    y = b[j - n]
                if x > y:
                    if i < n:
                        a[i] = y
                    else:
                        b[i - n] = y
                    if j < n:
                        a[j] = x
                    else:
                        b[j - n] = x
                i += 1
                j += 1
            if gap == 1:
                break
            gap = (gap + 1) // 2
