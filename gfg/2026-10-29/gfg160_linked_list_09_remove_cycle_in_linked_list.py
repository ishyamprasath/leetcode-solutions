"""Remove Cycle in Linked List (GFG160 Linked List #9)
https://www.geeksforgeeks.org/problems/remove-loop-in-linked-list/1
Approach: Floyd detection; find the last node of the loop (node whose next is loop start) and cut it. O(n), O(1).
"""
class Solution:
    def removeLoop(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                break
        else:
            return
        if slow is head:
            while fast.next is not head:
                fast = fast.next
            fast.next = None
            return
        slow = head
        while slow.next is not fast.next:
            slow = slow.next
            fast = fast.next
        fast.next = None
