class Solution:
    def kClosest(self, points, k):
        return sorted(points, key=lambda a: a[0] * a[0] + a[1] * a[1])[:k]
