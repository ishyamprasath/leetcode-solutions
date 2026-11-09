# Title: Postfix Evaluation
# URL: https://www.geeksforgeeks.org/problems/evaluation-of-postfix-expression1735/1
# Difficulty: Medium
class Solution:
    def evaluatePostfix(self, arr):
        stack = []
        for token in arr:
            if token not in {"+", "-", "*", "/", "^"}:
                stack.append(int(token))
                continue

            right = stack.pop()
            left = stack.pop()
            if token == "+":
                stack.append(left + right)
            elif token == "-":
                stack.append(left - right)
            elif token == "*":
                stack.append(left * right)
            elif token == "/":
                stack.append(left // right)
            else:
                stack.append(left ** right)
        return stack[-1]
