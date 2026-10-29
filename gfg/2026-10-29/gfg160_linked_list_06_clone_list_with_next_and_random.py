"""Clone List with Next and Random (GFG160 Linked List #6)
https://www.geeksforgeeks.org/problems/clone-a-linked-list-with-next-and-random-pointer/1
Approach: hash map old node -> new node, two passes. O(n) time/space.
"""
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
        self.random = None

class Solution:
    def cloneLinkedList(self, head):
        if not head:
            return None
        mp = {}
        cur = head
        while cur:
            mp[cur] = Node(cur.data)
            cur = cur.next
        cur = head
        while cur:
            mp[cur].next = mp.get(cur.next)
            mp[cur].random = mp.get(cur.random)
            cur = cur.next
        return mp[head]
