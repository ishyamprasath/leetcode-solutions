class Solution:
    def findPattern(self, s):
        n = len(s)
        i = 0
        while i < n:
            # count a run of 'x'
            x_count = 0
            while i < n and s[i] == 'x':
                x_count += 1
                i += 1
            # count the following run of 'y'
            y_count = 0
            while i < n and s[i] == 'y':
                y_count += 1
                i += 1
            if x_count == 0 or x_count != y_count:
                return False
        return True
