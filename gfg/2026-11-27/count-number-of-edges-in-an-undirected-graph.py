class Solution:
    def countEdges(self, adj: list[list[int]]) -> int:
        # every undirected edge appears in the lists of both endpoints
        total = sum(len(neighbours) for neighbours in adj)
        return total // 2
