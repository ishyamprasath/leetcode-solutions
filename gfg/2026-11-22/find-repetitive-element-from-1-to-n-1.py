class Solution:
    def findDuplicate(self, arr):
        seen = set()
        for x in arr:
            if x in seen:
                return x
            seen.add(x)
        return -1
