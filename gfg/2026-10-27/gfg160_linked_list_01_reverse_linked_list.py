# Title: Reverse Linked List
# URL: https://www.geeksforgeeks.org/batch/gfg-160-problems/track/linked-list-gfg-160/problem/reverse-a-linked-list
# Difficulty: Easy
# Approach: Iterative pointer reversal, O(n) time O(1) space.
"""
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
"""
class Solution:
    def reverseList(self, head):
        prev = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev
