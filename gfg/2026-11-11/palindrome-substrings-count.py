class Solution:
    def countPS(self, s):
        n = len(s)
        count = 0
        for center in range(n):
            left, right = center - 1, center + 1
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            left, right = center, center + 1
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
        return count
