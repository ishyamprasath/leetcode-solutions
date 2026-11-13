from collections import deque


class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # next strictly greater element to the right of each index
        nxt = [n] * n
        stack = []
        for i, v in enumerate(nums):
            while stack and nums[stack[-1]] < v:
                nxt[stack.pop()] = i
            stack.append(i)

        # Window [l, r]; cost = sum(prefix max - nums[i]) over the window.
        # dq holds the prefix-maximum chain of the window, left to right.
        dq = deque()
        cost = 0
        r = n - 1
        total = 0
        for l in range(n - 1, -1, -1):
            while dq and nums[dq[0]] <= nums[l]:
                j = dq.popleft()
                length = min(nxt[j], r + 1) - j
                cost += (nums[l] - nums[j]) * length
            dq.appendleft(l)
            while cost > k:
                cost -= nums[dq[-1]] - nums[r]
                if dq[-1] == r:
                    dq.pop()
                r -= 1
            total += r - l + 1
        return total
