# Longest String Chain — GFG 160 Dynamic Programming, course position 111 — https://www.geeksforgeeks.org/problems/longest-string-chain/1
class Solution:
    def longestStringChain(self, words):
        best_chain = {}
        answer = 0

        for word in sorted(words, key=len):
            length = 1
            for i in range(len(word)):
                predecessor = word[:i] + word[i + 1:]
                length = max(length, best_chain.get(predecessor, 0) + 1)
            best_chain[word] = max(best_chain.get(word, 0), length)
            answer = max(answer, best_chain[word])

        return answer
