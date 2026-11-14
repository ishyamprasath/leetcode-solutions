class Solution:
    def maxEqualSum(self, s1: list[int], s2: list[int], s3: list[int]) -> int:
        stacks = [s1, s2, s3]
        sums = [sum(s) for s in stacks]
        tops = [0, 0, 0]
        while not (sums[0] == sums[1] == sums[2]):
            # remove the top element of the stack with the largest sum
            i = sums.index(max(sums))
            sums[i] -= stacks[i][tops[i]]
            tops[i] += 1
        return sums[0]
