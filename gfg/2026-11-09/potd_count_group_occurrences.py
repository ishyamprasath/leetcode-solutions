# Title: Count Group Occurrences
# URL: https://www.geeksforgeeks.org/problems/count-the-characters1821/1
# Difficulty: Easy
class Solution:
    def getCount(self, s, k):
        groups = {}
        i = 0
        while i < len(s):
            j = i + 1
            while j < len(s) and s[j] == s[i]:
                j += 1
            groups[s[i]] = groups.get(s[i], 0) + 1
            i = j
        return sum(count == k for count in groups.values())
