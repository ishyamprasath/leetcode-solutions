import heapq


class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


class Solution:
    def mergeKLists(self, arr):
        heap = []
        for i, node in enumerate(arr):
            if node:
                heapq.heappush(heap, (node.data, i, node))
        dummy = Node(0)
        cur = dummy
        while heap:
            val, i, node = heapq.heappop(heap)
            cur.next = node
            cur = cur.next
            if node.next:
                heapq.heappush(heap, (node.next.data, i, node.next))
        return dummy.next
