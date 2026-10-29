"""Detect Loop in Linked List (GFG160 Linked List #7)
https://www.geeksforgeeks.org/problems/detect-loop-in-linked-list/1
Approach: Floyd slow/fast pointers. O(n) time, O(1) space.
"""
class Solution:
    def detectLoop(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False
