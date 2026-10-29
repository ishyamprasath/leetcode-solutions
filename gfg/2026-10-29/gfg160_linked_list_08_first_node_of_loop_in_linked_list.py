"""First Node of Loop in Linked List (GFG160 Linked List #8)
https://www.geeksforgeeks.org/problems/find-the-first-node-of-loop-in-linked-list--170645/1
Approach: Floyd detection, then reset one pointer to head and advance both. O(n), O(1).
"""
class Solution:
    def cycleStart(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                slow = head
                while slow is not fast:
                    slow = slow.next
                    fast = fast.next
                return slow.data
        return -1
