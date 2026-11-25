class Solution:
    def getLastMoment(self, n, left, right):
        a = max(left) if left else 0
        b = max(n - x for x in right) if right else 0
        return max(a, b)
