# Title: Max of Min for Every Window Size
# URL: https://www.geeksforgeeks.org/problems/maximum-of-minimum-for-every-window-size3453/1
# Difficulty: Hard
class Solution:
    def maxOfMins(self, arr):
        n = len(arr)
        left = [-1] * n
        right = [n] * n
        stack = []

        for i, value in enumerate(arr):
            while stack and arr[stack[-1]] >= value:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)

        stack.clear()
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)

        answer = [0] * n
        for i, value in enumerate(arr):
            width = right[i] - left[i] - 1
            answer[width - 1] = max(answer[width - 1], value)

        for i in range(n - 2, -1, -1):
            answer[i] = max(answer[i], answer[i + 1])
        return answer
