# Title: Get Min from Stack
# URL: https://www.geeksforgeeks.org/problems/get-minimum-element-from-stack/1
# Difficulty: Medium
class SpecialStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x):
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        if self.stack:
            value = self.stack.pop()
            if value == self.min_stack[-1]:
                self.min_stack.pop()

    def peek(self):
        return self.stack[-1] if self.stack else -1

    def isEmpty(self):
        return not self.stack

    def getMin(self):
        return self.min_stack[-1] if self.min_stack else -1
