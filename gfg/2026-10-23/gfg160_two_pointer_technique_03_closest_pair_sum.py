class Solution:
    def sumClosest(self, arr, target):
        if len(arr) < 2:
            return []
        a = sorted(arr)
        l, r = 0, len(a) - 1
        best = None
        bestDiff = float('inf')
        while l < r:
            s = a[l] + a[r]
            d = abs(s - target)
            # strict improvement only: earlier pairs have larger spread
            if d < bestDiff:
                bestDiff = d
                best = [a[l], a[r]]
            if s < target:
                l += 1
            elif s > target:
                r -= 1
            else:
                break
        return best if best is not None else []
