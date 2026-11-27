class Solution:
    def minRepeats(self, s1, s2):
        # s1 must be repeated at least enough times to cover s2's length;
        # one extra copy handles a partial overlap at the start
        times = -(-len(s2) // len(s1))
        repeated = s1 * times
        if s2 in repeated:
            return times
        if s2 in repeated + s1:
            return times + 1
        return -1
