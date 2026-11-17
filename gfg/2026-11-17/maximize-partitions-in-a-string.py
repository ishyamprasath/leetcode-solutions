class Solution:
    def maxPartitions(self, s):
        last = {ch: i for i, ch in enumerate(s)}
        count = 0
        end = 0
        for i, ch in enumerate(s):
            end = max(end, last[ch])
            if i == end:
                count += 1
        return count
