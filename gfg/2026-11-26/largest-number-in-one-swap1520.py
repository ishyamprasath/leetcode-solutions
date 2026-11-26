class Solution:
    def largestSwap(self, s):
        digits = list(s)
        n = len(digits)
        # best[i] = index of the largest digit in digits[i:],
        # taking the rightmost one when there are ties
        best = [0] * n
        best[n - 1] = n - 1
        for i in range(n - 2, -1, -1):
            j = best[i + 1]
            best[i] = i if digits[i] > digits[j] else j
        for i in range(n - 1):
            j = best[i + 1]
            if digits[j] > digits[i]:
                digits[i], digits[j] = digits[j], digits[i]
                break
        return "".join(digits)
